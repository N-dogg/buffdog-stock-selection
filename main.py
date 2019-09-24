import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder

from model import DNN

def preprocessing(data):
    #ugly data preprocessing based on the example dataset
    X = data.iloc[:, :-1].values
    y = data.iloc[:, -1]
    dummy_sector = pd.get_dummies(X[:,0], drop_first = True)
    dummy_country = pd.get_dummies(X[:, 1], drop_first = True)
    X = pd.DataFrame((X[:,2:]))
    X = X.merge(dummy_sector, left_index = True, right_index = True)
    X = X.merge(dummy_country, left_index = True, right_index = True)
    x_train, x_valid, y_train, y_valid = train_test_split(X, y, test_size = 0.2, shuffle = False)
    y_valid = pd.DataFrame(y_valid)
    y_train = pd.DataFrame(y_train)
    X_scale = StandardScaler()
    x_train = X_scale.fit_transform(x_train)
    x_valid = X_scale.transform(x_valid)

    assert x_train.shape[0]==y_train.shape[0]

    return(x_train, x_valid, y_train, y_valid, X, y)

def train_plot(training_data):
    #plot the training data
    plt.plot(training_data['loss'], linewidth=2, label='Train')
    plt.plot(training_data['val_loss'], linewidth=2, label='Valid')
    plt.legend(loc='upper right')
    plt.title('Model Loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.show()


if __name__ == '__main__':

    #import data
    df = pd.read_csv('Book1.csv', index_col = 0)
    x_train, x_valid, y_train, y_valid, X, y = preprocessing(df)
    input_dim = x_train.shape[1]

    #create an instance of the model class
    model = DNN(input_dim)
    model.summary()

    #set save path and train
    model.set_save_path('dnn_v1.h5')
    output = model.fit(x_train, y_train, x_valid, y_valid)
    train_plot(output)

    #load model and predict
    model.load_model('dnn_v1.h5')
    result = model.predict(X)
