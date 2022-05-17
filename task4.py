import numpy as np

class perceptron:
    def __init__(self,alpha=0.5,iteration=10):
        self.alpha = alpha
        self.iteration= iteration
        self.w = []
        self.bias = 0

    def summation(self,x):
        y=np.dot(x,self.w)+ self.bias
        return y
    def predict(self,x):
        return np.where(self.summation(x)>=0,1,0)
    def train(self,x,y):
        self.w=np.zeros(shape=(x.shape[1],))
        epoch = 1 

        for _ in range(self.iteration):
            flag =0
            print(f"*************epoch {epoch}********")
            for inputs, target in zip(x,y): 
                # basically combines two array
                pred_output = self.predict(inputs)
                error = target - pred_output
                print(error)
                if error !=0:
                    flag =1
                    self.w+=self.alpha*error*inputs
                    self.bias+=self.alpha*error
            epoch += 1


            if flag == 0:
                return self

ann = perceptron(0.5,10)

x= np.array([
    [0,0],
    [0,1],
    [1,0],
    [1,1],

])
y =np.array([0,0,0,1]) 
 
ann.train(x,y)

predict_data= ann.predict([1,1])
print("Predicted Ouput for given input is {}".format(predict_data))

