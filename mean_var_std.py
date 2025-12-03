import numpy as np # pyright: ignore[reportMissingImports]

def calculate(inputList):
    if not isinstance(inputList, list):
        raise TypeError("The input must be a list containing nine numbers.")
    elif len(inputList) != 9:
        raise ValueError("List must contain nine numbers.")
    
    newArray = np.array([[inputList[0],inputList[1],inputList[2]],[inputList[3],inputList[4],inputList[5]],[inputList[6],inputList[7],inputList[8]]])

    mean = [np.mean(newArray, axis=0, dtype=float).tolist(), np.mean(newArray, axis=1, dtype=float).tolist(), np.mean(newArray, dtype=float)]
    variance = [np.var(newArray, axis=0, dtype=float).tolist(), np.var(newArray, axis=1, dtype=float).tolist(), np.var(newArray, dtype=float)]
    standardDev = [np.std(newArray, axis=0, dtype=float).tolist(), np.std(newArray, axis=1, dtype=float).tolist(), np.std(newArray, dtype=float)]
    maximum = [np.max(newArray, axis=0).tolist(), np.max(newArray, axis=1).tolist(), np.max(newArray).tolist()]
    minimum = [np.min(newArray, axis=0).tolist(), np.min(newArray, axis=1).tolist(), np.min(newArray).tolist()]
    total = [np.sum(newArray, axis=0).tolist(), np.sum(newArray, axis=1).tolist(), np.sum(newArray).tolist()]

    calculations = {"mean": mean, "variance": variance, "standard deviation": standardDev, "max": maximum, "min": minimum, "sum": total}

    return calculations