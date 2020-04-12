import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    timeCharged = float(input("Charging time: "))


    training_data = np.loadtxt("trainingdata.txt", delimiter=",")

    x = training_data[:, 0]
    y = training_data[:, 1]

    plt.scatter(x, y)
    plt.show()

    print(*x, sep=";")
    print(*y, sep=";")

    res = (timeCharged * 2) if timeCharged <= 4 else max(y)
    print("{:.2f}".format(res))
