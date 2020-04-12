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

    # numx = np.array(x).reshape(-1, 1)
    # numy = np.array(y).reshape(-1, 1)
    #
    # regressor = LinearRegression()
    #
    # regressor.fit(numx, numy)
    #
    # # intercept
    # print(regressor.intercept_)
    # # slope
    # print(regressor.coef_)
    #
    # pred_y = regressor.predict(np.array(timeCharged).reshape(-1, 1))
    # print(pred_y)
    #
    # pred_error = y - pred_y
    # print(pred_error)
