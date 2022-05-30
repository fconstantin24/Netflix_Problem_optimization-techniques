from scipy import spatial
import matplotlib.pyplot as plt

if __name__ == '__main__':

    x = [1, 2, 3, 4, 5]
    y = [1, 2, 3, 4, 5]

    # plotting the points
    plt.plot(0, 0)
    plt.plot(5, 5)
    plt.plot(1.0, 5.0, 'ro')
    plt.plot([1.0, 0.0], [5.0, 0.0], 'r')
    plt.plot(3.0, 4.0, 'ro')
    plt.plot([3.0, 0.0], [4.0, 0.0], 'r')
    plt.plot(2.0, 3.0, 'bo')
    plt.plot([2.0, 0.0], [3.0, 0.0], 'b')
    plt.plot(4.0, 2.0, 'bo')
    plt.plot([4.0, 0.0], [2.0, 0.0], 'b')
    plt.xlabel('Titanic')
    plt.ylabel('Matrix')
    plt.title('Collaborative filtering')
    plt.show()
