from matplotlib import pyplot
import csv

# ----------------------------------------------------------------------------------------------------------------------
import numpy as np

# Setting the random seed, feel free to change it and see different solutions.
np.random.seed(42)


def stepFunction(t):
    if t >= 0:
        return 1
    return 0


def prediction(X, W, b):
    return stepFunction((np.matmul(X, W) + b)[0])


# TODO: Fill in the code below to implement the perceptron trick.
# The function should receive as inputs the data X, the labels y,
# the weights W (as an array), and the bias b,
# update the weights and bias W, b, according to the perceptron algorithm,
# and return W and b.
def perceptronStep(X, y, W, b, learn_rate = 0.01):
    for i in range(len(X)):
        y_hat = prediction(X[i],W,b)
        if y[i]-y_hat == 1:
            W[0] += X[i][0]*learn_rate
            W[1] += X[i][1]*learn_rate
            b += learn_rate
        elif y[i]-y_hat == -1:
            W[0] -= X[i][0]*learn_rate
            W[1] -= X[i][1]*learn_rate
            b -= learn_rate
    return W, b

# This function runs the perceptron algorithm repeatedly on the dataset,
# and returns a few of the boundary lines obtained in the iterations,
# for plotting purposes.
# Feel free to play with the learning rate and the num_epochs,
# and see your results plotted below.
def trainPerceptronAlgorithm(X, y, learn_rate=0.01, num_epochs=25):
    x_min, x_max = min(X.T[0]), max(X.T[0])
    y_min, y_max = min(X.T[1]), max(X.T[1])
    W = np.array(np.random.rand(2, 1))
    b = np.random.rand(1)[0] + x_max
    # These are the solution lines that get plotted below.
    boundary_lines = []
    for i in range(num_epochs):
        # In each epoch, we apply the perceptron step.
        W, b = perceptronStep(X, y, W, b, learn_rate)
        boundary_lines.append((-W[0] / W[1], -b / W[1]))
    return boundary_lines
# ----------------------------------------------------------------------------------------------------------------------


if __name__ == '__main__':

    X = []
    X1 = []
    X2 = []
    y = []

    with open('data.csv', newline='\n') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        for row in data:
            point = row[0:2]
            X.append(point)
            label = row[2:3][0]
            y.append(label)
            if label == '1':
                X1.append(point)
            if label == '0':
                X2.append(point)

    npX = np.mat(X, dtype='float')
    npy = np.mat(y, dtype='float')
    lines = trainPerceptronAlgorithm(np.array(npX), npy.tolist()[0])
    pyplot.plot(np.array(np.mat(X1, dtype='float').T[0]).tolist()[0],
                np.array(np.mat(X1, dtype='float').T[1]).tolist()[0], 'b.', color='red')
    pyplot.plot(np.array(np.mat(X2, dtype='float').T[0]).tolist()[0],
                np.array(np.mat(X2, dtype='float').T[1]).tolist()[0], 'b.', color='blue')
    minX = min(np.array(npX.T[0]).tolist()[0]) - 0.5
    maxX = max(np.array(npX.T[0]).tolist()[0]) + 0.5

    minY = min(np.array(npX.T[1]).tolist()[0]) - 0.5
    maxY = max(np.array(npX.T[1]).tolist()[0]) + 0.5

    x = np.linspace(minX, maxX)
    for line in lines:
        pyplot.plot(x, line[0]*x+line[1], '--', color='green')

    pyplot.plot(x, lines[len(lines)-1][0]*x+lines[len(lines)-1][1], color='black')

    pyplot.xlim(minX, maxX)
    pyplot.ylim(minX, maxY)
    pyplot.show()
