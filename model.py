import pandas as pd

from keras.models import Sequential, Model, load_model
from keras.layers import Dense
from keras.callbacks import ModelCheckpoint

class DNN(object):

    def __init__(self, input_dim):
        self.input_dim = input_dim
        self.save_path = 'dnn_v1.h5'
        self.model = Sequential()
        self.model.add(Dense(50, input_dim = self.input_dim, activation = 'relu'))
        self.model.add(Dense(30, activation = 'tanh'))
        self.model.add(Dense(1, activation = 'sigmoid'))
        self.model.compile(loss = 'binary_crossentropy', optimizer = 'adam', metrics = ['accuracy'])

    def summary(self):
        #return model architecture
        return self.model.summary()

    def set_save_path(self, path):
        #set the save path
        self.save_path = path

    def fit(self, x_train, y_train, x_valid, y_valid, n_epochs = 20, batch_size = 500):
        #train the model
        cp = ModelCheckpoint(filepath=self.save_path,
                            save_best_only=True,
                            verbose=0)

        history = self.model.fit(x_train, y_train,
                            epochs=n_epochs,
                            batch_size=batch_size,
                            shuffle=True,
                            validation_data=(x_valid, y_valid),
                            verbose=1,
                            callbacks=[cp]).history

        return history

    def predict(self, x):
        #use the trained model to predict
        return pd.DataFrame(self.model.predict(x))

    def load_model(self, path):
        #load a pre-trained model
        self.model = load_model(path)
