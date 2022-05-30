import numpy as np
import time
import matplotlib.pyplot as plt
import scipy.optimize as spo

r = [[3.0, 0.0, 2.0, 0.0, 5.0, 0.0],
       [2.0, 4.0, 1.0, 0.0, 3.0, 5.0],
       [2.0, 0.0, 0.0, 5.0, 1.0, 0.0],
       [2.0, 2.0, 4.0, 0.0, 0.0, 4.0],
       [5.0, 0.0, 0.0, 0.0, 2.0, 0.0],
       [1.0, 0.0, 3.0, 5.0, 4.0, 0.0]]

user_number = 6
movie_number = 6
genres_number = 4
u = np.random.rand(user_number, genres_number)
m = np.random.rand(genres_number, movie_number)
r = np.array(r)


#     steps: iterations
#     alpha: learning rate
#     beta: regularization parameter
def matrix_factorization(x):
    start_time = time.time()
    g = 4
    alpha = 0.0002
    beta = 0.2
    steps = 10000

    for step in range(steps):
        for i in range(0, 6):
            for j in range(0, 6):
                if r[i][j] > 0:
                    eij = r[i][j] - np.dot(u[i, :], m[:, j])

                    for k in range(g):
                        u[i][k] = u[i][k] + alpha * (2 * eij * m[k][j] - beta * u[i][k])
                        m[k][j] = m[k][j] + alpha * (2 * eij * u[i][k] - beta * m[k][j])

        e = 0

        for i in range(len(r)):
            for j in range(len(r[i])):
                if r[i][j] > 0:
                    e = e + pow(r[i][j] - np.dot(u[i, :], m[:, j]), 2)

                    for k in range(g):
                        e = e + (beta / 2) * (pow(u[i][k], 2) + pow(m[k][j], 2))

        if e < 0.001:
            break

    res = np.dot(u, m)
    res = np.array(res)
    for row in range(0, user_number):
        for column in range(0, movie_number):
                    if r[row][column] > 0:
                        res[row][column] = r[row][column]
                    elif res[row][column] > 5:
                        res[row][column] = 5.0
                    res[row][column] = round(res[row][column], 1)
    print(res)
    print(start_time - time.time())
    return res


if __name__ == '__main__':
    # result = []
    # steps1 = 10000
    # steps2 = 15000
    # steps3 = 20000
    # x = [steps1, steps2, steps3]
    # y = []

    # for count in range(0, 3):
    #     # matricea necompletata de ratinguri
    #     ratings = [[3.0, 0.0, 2.0, 0.0, 5.0, 0.0],
    #                [2.0, 4.0, 1.0, 0.0, 3.0, 5.0],
    #                [2.0, 0.0, 0.0, 5.0, 1.0, 0.0],
    #                [2.0, 2.0, 4.0, 0.0, 0.0, 4.0],
    #                [5.0, 0.0, 0.0, 0.0, 2.0, 0.0],
    #                [1.0, 0.0, 3.0, 5.0, 4.0, 0.0]]
    #     ratings = np.array(ratings)
    #     users = np.random.rand(user_number, genres_number)
    #     movies = np.random.rand(genres_number, movie_number)
    #
    #     start_time = time.time()
    #
    #     rezultat = matrix_factorization(ratings, users, movies, genres_number, x[count])
    #
    #     for row in range(0, user_number):
    #         for column in range(0, movie_number):
    #             if ratings[row][column] > 0:
    #                 rezultat[row][column] = ratings[row][column]
    #             elif rezultat[row][column] > 5:
    #                 rezultat[row][column] = 5.0
    #             rezultat[row][column] = round(rezultat[row][column], 1)
    #
    #     print(time.time() - start_time)
    #     print(rezultat)
    #     y.append(time.time() - start_time)
    #
    # # plotting the points
    # plt.plot(x, y)
    # # naming the x axis
    # plt.xlabel('steps')
    # # naming the y axis
    # plt.ylabel('y - time')
    # # giving a title to my graph
    # plt.title('Collaborative filtering')
    # # function to show the plot
    # plt.show()

    r0 = [[3.0, 4.0, 2.0, 5.0, 5.0, 5.0],
          [2.0, 4.0, 1.0, 5.0, 3.0, 5.0],
          [2.0, 3.0, 2.0, 5.0, 1.0, 4.0],
          [2.0, 2.0, 4.0, 5.0, 4.0, 4.0],
          [5.0, 4.0, 1.0, 5.0, 2.0, 5.0],
          [1.0, 2.0, 3.0, 5.0, 4.0, 4.0]]

    start_time = time.time()
    r0 = np.array(r0)
    result = spo.minimize(matrix_factorization, r0)
    print(start_time - time.time())
    if result.success:
        print(result.res)
    else:
        print("Nu")
