import matplotlib.pyplot as plt
import numpy as np
import util

from linear_model import LinearModel


def main(tau, train_path, eval_path):
    """Problem 5(b): Locally weighted regression (LWR)

    Args:
        tau: Bandwidth parameter for LWR.
        train_path: Path to CSV file containing dataset for training.
        eval_path: Path to CSV file containing dataset for evaluation.
    """
    # Load training set
    x_train, y_train = util.load_dataset(train_path, add_intercept=True)

    # *** START CODE HERE ***
    clf=LocallyWeightedLinearRegression(0.5)
    clf.fit(x_train,y_train)
    print(clf.predict(x_train))
    # Fit a LWR model
    # Get MSE value on the validation set
    # Plot validation predictions on top of training set
    # No need to save predictions
    # Plot data
    # *** END CODE HERE ***


class LocallyWeightedLinearRegression(LinearModel):
    """Locally Weighted Regression (LWR).

    Example usage:
        > clf = LocallyWeightedLinearRegression(tau)
        > clf.fit(x_train, y_train)
        > clf.predict(x_eval)
    """

    def __init__(self, tau):
        super(LocallyWeightedLinearRegression, self).__init__()
        self.tau = tau
        self.x = None
        self.y = None

    def fit(self, x, y):
        """Fit LWR by saving the training set.

        """
        # *** START CODE HERE ***
        self.x=x
        self.y=y
        # *** END CODE HERE ***

    def predict(self, x):
        """Make predictions given inputs x.

        Args:
            x: Inputs of shape (m, n).

        Returns:
            Outputs of shape (m,).
        """
        # *** START CODE HERE ***
        m,n=x.shape
        y_pred=np.zeros(m)
        for i in range(m):
            w=np.exp(-np.sum((self.x-self.x[i])**2,axis=1)/(2*self.tau**2))
            theta=np.linalg.inv((self.x.T*w)@self.x)@(self.x.T@self.y)
            y_pred[i]=theta.T@self.x[i]

        # for i in range(m):
        #     W_i = np.exp(-np.sum((self.x - x[i])**2, axis = 1)/(2*self.tau**2))
        #     theta = np.linalg.inv((self.x.T * W_i)@self.x) @ (self.x.T * W_i) @ self.y
        #     y_pred[i] = theta.T@x[i]
        return y_pred
            
        # *** END CODE HERE ***
tau=0.5
train_path='../data/ds5_train.csv'
main(tau,train_path,'e')