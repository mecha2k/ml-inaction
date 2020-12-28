from numpy import *
import matplotlib.pyplot as plt
from matplotlib.patches import Circle


def open_file(filename="testSet.txt"):
    xcord0 = []
    ycord0 = []
    xcord1 = []
    ycord1 = []

    fr = open(filename)

    for line in fr.readlines():
        lineSplit = line.strip().split("\t")
        xPt = float(lineSplit[0])
        yPt = float(lineSplit[1])
        label = int(lineSplit[2])
        if label == -1:
            xcord0.append(xPt)
            ycord0.append(yPt)
        else:
            xcord1.append(xPt)
            ycord1.append(yPt)

    fr.close()

    return xcord0, ycord0, xcord1, ycord1


def plotSVM():
    xcord0, ycord0, xcord1, ycord1 = open_file()

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord0, ycord0, marker="s", s=90)
    ax.scatter(xcord1, ycord1, marker="o", s=50, c="red")
    plt.title("Support Vectors Circled")
    circle = Circle(
        (4.66, 3.51),
        0.5,
        facecolor="none",
        edgecolor=(0, 0.8, 0.8),
        linewidth=3,
        alpha=0.5,
    )
    ax.add_patch(circle)
    circle = Circle(
        (3.46, -0.08),
        0.5,
        facecolor="none",
        edgecolor=(0, 0.8, 0.8),
        linewidth=3,
        alpha=0.5,
    )
    ax.add_patch(circle)
    circle = Circle(
        (6.08, 0.42),
        0.5,
        facecolor="none",
        edgecolor=(0, 0.8, 0.8),
        linewidth=3,
        alpha=0.5,
    )
    ax.add_patch(circle)
    # plt.plot([2.3,8.5], [-6,6]) #seperating hyperplane
    b = -3.75567
    w0 = 0.8065
    w1 = -0.2761
    x = arange(-2.0, 12.0, 0.1)
    y = (-w0 * x - b) / w1
    ax.plot(x, y)
    ax.axis([-2, 12, -8, 6])
    plt.show()
