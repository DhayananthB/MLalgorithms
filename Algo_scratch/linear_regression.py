class SLR:
    def __init__(self) -> None:
        self.m= None
        self.b=None
    def fit(self,X_train,y_train):
        num=0
        den =0
        for i in range(X_train.shape[0]):
            num+=((X_train[i]-X_train.mean())*(y_train[i]-y_train.mean()))
            den+=(X_train[i]-X_train.mean())**2
        self.m=num/den
        self.b = y_train.mean()-(self.m * X_train.mean())
        #y = mx + b      
        print(self.m)
        print(self.b)
    def predict(self,X):
        print(X)
        return self.m*X + self.b          