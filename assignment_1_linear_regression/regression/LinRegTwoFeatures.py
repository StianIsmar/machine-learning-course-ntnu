#Two feature linear regression

#!/usr/local/bin/python3
import csv
import numpy as np
import os
import matplotlib.pyplot as plt


class LinearRegressOneFeatureTraining():
    def __init__(self):
        dataArray, numOfObs = self.readCsv()
        weights, X, Y = self.constructMatrix(dataArray, numOfObs)
        self.weights = weights
        self.X = X
        self.Y = Y
        # self.calculateError(weights, X, Y)

    def readCsv(self):
        os.chdir('../regression')
        cwd = os.getcwd()  # Get the current working directory (cwd)
        files = os.listdir(cwd)  # Get all the files in that directory

        with open("train_2d_reg_data.csv") as f:
            reader = csv.reader(f)
            counter = 0
            dataArray = []
            for row in reader:
                dataArray.append(row)
                counter += 1
            # number of observations in the CSV-file.
            counter = counter - 1
        return dataArray, counter


    def constructMatrix(self, dataArray, numOfObs):
        # print(numOfObs) # 325 rows of observations!
        dataArray = np.delete(dataArray, 0, axis = 0 )

        # M has numOfObs rows and 3 columns!
        M = np.ones((numOfObs, 3),dtype=float)

        # X has numOfObs rows and 3 columns!
        X = np.ones((numOfObs, 3),dtype=float)

        # Y is just 1-d array:
        Y = np.zeros([],dtype=float)

        # Filling M, X and Y with the actual data from the CSV:
        # **** Y:
        for obs in dataArray:
            Y = np.append(Y, obs[2])
        # Remove the two first elements, they should not be there:
        Y =  np.delete(Y,0)

        Y = Y.astype(np.float)


        # *** M: Should have 3 columns, with each having row 1,x1,x2. Create X:
        place = 0
        for obs in dataArray:
            X[place,1]= obs[1]
            X[place,2] = obs[2]
            place += 1

        # Calculating the weights for two features:
        print(X)
        Xtrans = np.transpose(X)

        XtransDotX = np.dot(Xtrans, X)
        # inverse of this result:
        matrix1 = np.matrix(XtransDotX)
        # Inverse it
        matrix1 = matrix1.I

        # Xtrans dotted with Y:
        XtransDotY = np.dot(Xtrans, Y)

        # Finally, to get w:
        w = np.dot(matrix1, XtransDotY)
        print(w)
        return w, X, Y


    # Calculating the model error using the mean squared error given in the assignment:
def calculateError(weights, X, Y):

    # Need to transpose the weights so that X can be multiplied with X.
    # X needs is a 325x3 matrix, whilst weights is a 3x1 matrix after it is transposed!
    weights = weights.T
    Xw = np.dot(X,weights)

    # Continue with the linear algebra to calculate the error:

    error = (1/len(Y)) * (np.linalg.norm(np.subtract(Xw,Y)))**2
    return error
# Main:
l1 = LinearRegressOneFeatureTraining()
Xtrain = l1.X
Ytrain = l1.Y
Wtrain = l1.weights

errorTrainingData = calculateError(Wtrain, Xtrain,Ytrain)
print(errorTrainingData)

# Loading the test-data

data = np.loadtxt('train_1d_reg_data.csv', delimiter=',', skiprows=1, unpack=False)
xarray = data[...,0] # Need to get this on a matrix-form!
Y = data[...,1]
# print(data)
print(" ")

