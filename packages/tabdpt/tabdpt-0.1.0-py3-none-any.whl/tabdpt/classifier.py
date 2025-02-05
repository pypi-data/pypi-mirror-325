import numpy as np
import torch
import math
from sklearn.base import ClassifierMixin
from .estimator import TabDPTEstimator
from .utils import pad_x


class TabDPTClassifier(TabDPTEstimator, ClassifierMixin):
    def __init__(self, path: str = '', inf_batch_size: int = 512, device: str = 'cuda:0', use_flash: bool = True, compile: bool = True):
        super().__init__(path=path, mode='cls', inf_batch_size=inf_batch_size, device=device, use_flash=use_flash, compile=compile)
        
    def fit(self, X, y):
        super().fit(X, y)
        self.num_classes = len(np.unique(self.y_train))
        assert self.num_classes > 1, "Number of classes must be greater than 1"
        
    def _predict_large_cls(self, X_train, X_test, y_train):
        num_digits = math.ceil(math.log(self.num_classes, self.max_num_classes))
        
        digit_preds = []
        for i in range(num_digits):
            y_train_digit = (y_train // (self.max_num_classes ** i)) % self.max_num_classes
            pred = self.model(
                x_src=torch.cat([X_train, X_test], dim=1),
                y_src=y_train_digit.unsqueeze(-1),
                task='cls',
            )
            digit_preds.append(pred.float())

        full_pred = torch.zeros((X_test.shape[0], X_test.shape[1], self.num_classes), device=X_train.device)
        for class_idx in range(self.num_classes):
            class_pred = torch.zeros_like(digit_preds[0][:, :, 0])
            for digit_idx, digit_pred in enumerate(digit_preds):
                digit_value = (class_idx // (self.max_num_classes ** digit_idx)) % self.max_num_classes
                class_pred += digit_pred[:, :, digit_value]
            full_pred[:, :, class_idx] = class_pred

        return full_pred

    @torch.no_grad()
    def predict_proba(self, X: np.ndarray, temperature: float = 0.8, context_size: int = 128):
        train_x, train_y, test_x = self._prepare_prediction(X)

        if context_size >= self.n_instances:
            X_train = pad_x(train_x[None, :, :], self.max_features).to(self.device)
            X_test = pad_x(test_x[None, :, :], self.max_features).to(self.device)
            y_train = train_y[None, :].float()
            
            if self.num_classes <= self.max_num_classes:
                pred = self.model(
                    x_src=torch.cat([X_train, X_test], dim=1),
                    y_src=y_train.unsqueeze(-1),
                    task=self.mode,
                )
            else:
                pred = self._predict_large_cls(X_train, X_test, y_train)
            
            pred = pred[..., :self.num_classes] / temperature
            pred = torch.nn.functional.softmax(pred, dim=-1)
            return pred.float().squeeze().detach().cpu().numpy()
        else:
            pred_list = []
            for b in range(math.ceil(len(self.X_test) / self.inf_batch_size)):
                start = b * self.inf_batch_size
                end = min(len(self.X_test), (b + 1) * self.inf_batch_size)

                indices_nni = self.faiss_knn.get_knn_indices(
                    self.X_test[start:end], k=context_size
                )
                X_nni = train_x[torch.tensor(indices_nni)]
                y_nni = train_y[torch.tensor(indices_nni)]

                X_nni, y_nni = (
                    pad_x(torch.Tensor(X_nni), self.max_features).to(self.device),
                    torch.Tensor(y_nni).to(self.device),
                )
                X_eval = test_x[start:end]
                X_eval = pad_x(X_eval.unsqueeze(1), self.max_features).to(self.device)
                
                if self.num_classes <= self.max_num_classes:
                    pred = self.model(
                        x_src=torch.cat([X_nni, X_eval], dim=1),
                        y_src=y_nni.unsqueeze(-1),
                        task=self.mode,
                    )
                else:
                    pred = self._predict_large_cls(X_nni, X_eval, y_nni)

                pred = pred[..., :self.num_classes].float() / temperature
                pred = torch.nn.functional.softmax(pred, dim=-1)

                pred_list.append(pred.squeeze())

            
            return torch.cat(pred_list, dim=0).squeeze().detach().cpu().numpy()
        
    def predict(self, X, temperature: float = 0.8, context_size: int = 128):
        return self.predict_proba(X, temperature=temperature, context_size=context_size).argmax(axis=-1)