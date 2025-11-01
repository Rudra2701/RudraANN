import Neuron
from Neuron import makearr


class Layer:
    def __init__(self,inputs,outputs,lower=-1,upper=1):
        self.outputs=outputs
        x=makearr(inputs,lower,upper)
        self.weights=[]

        for i in range(outputs):
            self.weights.append(x)
        self.bias=makearr(outputs,lower,upper) #weight[output][input]
    def feedforward(self,inputs):
        o=[]
        for i in range(self.outputs):
             o.append(Neuron.neuron(inputs,self.weights[i],self.bias[i]))
        return o
    def weight(self,weight):
        self.weights=weight
    def bias(self,bias):
        self.bias=bias
    def train(self,inp,err,n=0.1):
        for outnum in range(len(self.weights)):
            for inpnum in range(len(self.weights[outnum])):
                self.weights[outnum][inpnum]=n*inp[inpnum]*err[outnum] #change of data