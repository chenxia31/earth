import numpy as np
import util

from linear_model import LinearModel


def main(train_path, eval_path, pred_path):
    """Problem 1(b): Logistic regression with Newton's Method.

    Args:
        train_path: Path to CSV file containing dataset for training.
        eval_path: Path to CSV file containing dataset for evaluation.
        pred_path: Path to save predictions.
    """
    x_train, y_train = util.load_dataset(train_path, add_intercept=True)

    # *** START CODE HERE ***
    x_eval,y_eval=util.load_dataset(eval_path,add_intercept=True)
    clf=LogisticRegression()
    clf.fit(x_train,y_train)
    clf.predict(x_eval)
    print(np.mean(clf.predict(x_train) == y_train))
    util.plot(x_train,y_train,theta=clf.theta)
    # *** END CODE HERE ***


class LogisticRegression(LinearModel):
    """Logistic regression with Newton's Method as the solver.

    Example usage:
        > clf = LogisticRegression()
        > clf.fit(x_train, y_train)
        > clf.predict(x_eval)
    """

    def fit(self, x, y):
        """Run Newton's Method to minimize J(theta) for logistic regression.

        Args:
            x: Training example inputs. Shape (m, n).
            y: Training example labels. Shape (m,).
        """
        def g(theta,x):
            ''' define of the hypothesis
            
            Args:
                theta: Model parameters,shape(n,1)
                x: model example inputs,shape(m,n)
            
            Returns:
                probability of the logisitic regression 
            
            '''
            return 1/(1+np.exp(-x @ theta)) 
        
        def dJ(theta,x,y):
            ''' define of the gradient for the loss function'''
            m,_=x.shape
            return 1/m*x.T@(g(theta,x)-y)
        
        def Hessian(theta,x):
            m, _ = x.shape
            Z = g(theta, x)
            Z = Z*(1-Z) # (m,)
            return 1/m * Z * x.T @ x 

        def dist(x, y):
            ''' return the abs value of all predict'''
            return np.sum(np.abs(x-y))

        # *** START CODE HERE ***
        m, n = x.shape
        if self.theta is None:
            self.theta = np.zeros(n)
    
        for i in range(self.max_iter):
            theta_new = self.theta - np.linalg.inv(Hessian(self.theta, x)) @ dJ(self.theta, x, y)
            if dist(theta_new, self.theta) < self.eps:
                self.theta = theta_new
                break
            else:
                self.theta = theta_new
        # *** END CODE HERE ***

    def predict(self, x):
        """Make a prediction given new inputs x.

        Args:
            x: Inputs of shape (m, n).

        Returns:
            Outputs of shape (m,).
        """
        # *** START CODE HERE ***
        return x@self.theta>=0
        # *** END CODE HERE ***
train_path='../data/ds1_train.csv'
eval_path='../data/ds1_valid.csv'
store_path='../data'
main(train_path=train_path,eval_path=eval_path,pred_path=store_path)