import numpy as np
import util

from linear_model import LinearModel


def main(train_path, eval_path, pred_path):
    """Problem 1(e): Gaussian discriminant analysis (GDA)

    Args:
        train_path: Path to CSV file containing dataset for training.
        eval_path: Path to CSV file containing dataset for evaluation.
        pred_path: Path to save predictions.
    """
    # Load dataset
    x_train, y_train = util.load_dataset(train_path, add_intercept=False)
    x_eval,y_eval=util.load_dataset(eval_path,add_intercept=False)

    # *** START CODE HERE ***
    clf = GDA()
    clf.fit(x_train, y_train)
    print(clf.predict(x_eval))
    # *** END CODE HERE ***


class GDA(LinearModel):
    """Gaussian Discriminant Analysis.

    Example usage:
        > clf = GDA()
        > clf.fit(x_train, y_train)
        > clf.predict(x_eval)
    """

    def fit(self, x, y):
        """Fit a GDA model to training set given by x and y.

        Args:
            x: Training example inputs. Shape (m, n).
            y: Training example labels. Shape (m,).

        Returns:
            theta: GDA model parameters.
        """
        # *** START CODE HERE ***
        m,_=x.shape
        self.phi=1/m*sum(y==1)
        index0=y==0
        index1=y==1
        self.mu0=np.sum(x[index0,:],axis=0)/sum(index0)
        self.mu1=np.sum(x[index1,:],axis=0)/sum(index1)
        mu = ((1-y).reshape(-1,1) * self.mu0 + y.reshape(-1,1) * self.mu1)
        self.Sigma = 1/m * (x- mu).T@(x- mu)
        Sigma_inv = np.linalg.inv(self.Sigma)
        theta = Sigma_inv @ (self.mu1 - self.mu0)
        theta_0 = (1/2 * (self.mu0.T @ Sigma_inv @ self.mu0 - 
                         self.mu1.T @ Sigma_inv @ self.mu1) - 
                         np.log((1-self.phi)/self.phi) 
                        )
        
        
        self.theta = np.insert(theta, 0, theta_0)
        # *** END CODE HERE ***       
        

    def predict(self, x):
        """Make a prediction given new inputs x.

        Args:
            x: Inputs of shape (m, n).

        Returns:
            Outputs of shape (m,).
        """
        # *** START CODE HERE ***
        return util.add_intercept(x)  @ self.theta >= 0
        # *** END CODE HERE
train_path='../data/ds1_train.csv'
eval_path='../data/ds1_valid.csv'
store_path='../data'
main(train_path=train_path,eval_path=eval_path,pred_path=store_path)