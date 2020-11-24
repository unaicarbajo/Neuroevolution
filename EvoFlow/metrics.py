"""
Auxiliary predefined functions. Can be expanded by the user.
"""
import numpy as np

evals = []
best = 1


def mse(true, prediction):
    return np.mean((true-prediction)**2)


def accuracy_error(true, prediction):
    global evals
    true = np.argmax(true, axis=1)
    prediction = np.argmax(prediction, axis=1)
    if len(evals) % 1000 == 0:
        np.save("temp_evals.npy", np.array(evals))
    evals += [1-np.sum(true == prediction)/true.shape[0]]
    return 1-np.sum(true == prediction)/true.shape[0]


def ret_evals():
    global evals
    return evals
