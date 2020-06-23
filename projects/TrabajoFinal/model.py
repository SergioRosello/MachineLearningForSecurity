# example of one hot encoding for a neural network
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from keras.models import Sequential
from keras.layers import Dense

# load the dataset
def load_dataset(filename):
        # load the dataset as a pandas DataFrame
        data = read_csv(filename, header=0, 
                dtype={'ip.src': str,
                    'ip.dst': str,
                    '_ws.col.Protocol': str,
                    'frame.len': str,
                    '_ws.col.Info': str})
        print("Data head:")
        print(data.head())
        print("Data tail:")
        print(data.tail())
        print("Data sample:")
        print(data.sample(10))
        print("Data types:")
        print(data.dtypes)
        print("Data info:")
        print(data.info())
        print("Data description:")
        print(data.describe)
	# retrieve numpy array
        dataset = data.values
	# split into input (X) and output (y) variables
        X = dataset[:, :-1]
        y = dataset[:,-1]
	# format all fields as string
        X = X.astype(str)
	# reshape target to be a 2d array
        y = y.reshape((len(y), 1))
        return X, y

# prepare input data
def prepare_inputs(X_train, X_test):
	ohe = OneHotEncoder()
	ohe.fit(X_train)
	X_train_enc = ohe.transform(X_train)
	X_test_enc = ohe.transform(X_test)
	return X_train_enc, X_test_enc

# prepare target
def prepare_targets(y_train, y_test):
	le = LabelEncoder()
	le.fit(y_train)
	y_train_enc = le.transform(y_train)
	y_test_enc = le.transform(y_test)
	return y_train_enc, y_test_enc

# load the dataset
X, y = load_dataset('./sorted_sanitized_no-frame-length_network_traffic.csv')
print("Hemos cargado el dataset")
# split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=1)
print("Hemos entrenado el modelo un poco :/")
# prepare input data
X_train_enc, X_test_enc = prepare_inputs(X_train, X_test)
print("Hemos preparado los datps de entrada al modelo")
# prepare output data
y_train_enc, y_test_enc = prepare_targets(y_train, y_test)
print("Hemos preparado los datos de salida")
# define the  model
model = Sequential()
model.add(Dense(10, input_dim=X_train_enc.shape[1], activation='relu', kernel_initializer='he_normal'))
model.add(Dense(1, activation='sigmoid'))
# compile the keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit the keras model on the dataset
model.fit(X_train_enc, y_train_enc, epochs=100, batch_size=16, verbose=2)
# evaluate the keras model
_, accuracy = model.evaluate(X_test_enc, y_test_enc, verbose=0)
print('Accuracy: %.2f' % (accuracy*100))

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
