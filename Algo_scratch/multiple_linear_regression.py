class MLR:
    def __init__(self):
        self.coef = None
        self.intercept =None
    def fit(self,X_train,y_train):
        X_train = np.insert(X_train,0,1,axis=1)
        # axis=1 column
        betas = np.linalg.inv(np.dot(X_train.T,X_train)).dot(X_train.T).dot(y_train)
        self.intercept=betas[0]
        self.coef=betas[1:]
    def predict(self,X_test):
        y_pred=np.dot(X_test,self.coef)+self.intercept
        return y_pred
