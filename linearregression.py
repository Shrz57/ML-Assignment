import numpy as np
from typing import List, Tuple
from numpy.typing import ArrayLike

class LinearRegression():
    def __init__(self,lr:float,epoch:int,Shape:int):
        """Construct

        Args:
            lr (Float): smfsofs
            epoch (Int): _description_
            Shape (Int): _description_
        """        
        self.lr=lr
        self.epoach=epoch
        self.Shape=Shape
        self.weight,self.bias=self.initialize_parameter()
    def initialize_parameter(self)->Tuple:
        """ Initializes Parameters of weight and bias for linerar regression
        where Weight is initialized randomly.
        whereas Bias is inialized with zero.

        Returns:
            Tuple: Two elements weights and bias initalized randomly
        """        
        weight=np.random.rand()
        bias = 0
        return weight, bias

    def predict(self, x:ArrayLike)->ArrayLike:
        """Predict the output on the basis of input feature

        Args:
            x (ArrayLike): Input feature

        Returns:
            ArrayLike: Predicted Output
        """        
        y_pred= self.bias + np.dot(self.weights,x)
        return y_pred
    def cal_loss(self,y:ArrayLike,y_pred:ArrayLike)->float:
        """Calcutale and retuern the mean squared error 

        Args:
            y (ArrayLike): True value
            y_pred (ArrayLike): predicted value

        Returns:
            float: Mean square 
        """        
        mse = np.mean(np.sum((y-y_pred)**2))*1/2
        return mse
    def calculate_del_parm(self,y:ArrayLike,y_pred:ArrayLike,x:ArrayLike):
        """ Calculates the delta value

        Args:
            y (ArrayLike): Actual value
            y_pred (ArrayLike): Predicted value
            x (ArrayLike): input feature
        """        
        self.del_bias=np.mean(np.sum(y-y_pred))
        self.del_weight=np.mean(np.sum(y-y_pred)*x)

    def update_prams(self):
        """ Updates the weights and bias w.r.t learning rate , del_weight, and del_bias
        """        
        self.bias=self.bias-self.lr*self.del_bias
        self.wight=self.weight - self.lr*self.del_weight
    def disp_param(self):
        """ Display the parameters weights and bias.
        """        
        print(self.weight,self.bias)

    def fit (self,x:ArrayLike,y:ArrayLike,y_pred:ArrayLike):
        """ This function trains the model based on the input features and their labels.

        Args:
            x (ArrayLike): Input features
            y (ArrayLike): output value 
            y_pred (ArrayLike): Predicated value
        """        
        for i in range(self.epoch):
            y_pred=self.predict(x,y)
            loss=self.cal_loss(y,y_pred)
            self.calculate_del_parm(x,y,y_pred)
            self.update_prams()
            self.disp_param()