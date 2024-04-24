import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

'''
plotNum
0 - Epitrochoid
1 - Butterfly curve
2 - Heart curve
3 - Hypocycloid
4 - Lissajous curve
'''
plotNum: int = 4

# 2D
def Epitrochoid(array: np.array) -> tuple[np.array, np.array]:
    xCoords: np.array = 11*np.cos(array) - np.cos(11 * array / 10)
    yCoords: np.array = 11*np.sin(array) - np.sin(11 * array / 10)

    return (xCoords, yCoords)

def Butterfly(array: np.array) -> tuple[np.array, np.array]:
    xCoords: np.array = np.sin(array) * (np.exp(np.cos(array)) - 2 * np.cos(4 * array) - np.sin(array / 12)**5)
    yCoords: np.array = np.cos(array) * (np.exp(np.cos(array)) - 2 * np.cos(4 * array) - np.sin(array / 12)**5)

    return (xCoords, yCoords)

def Heart(array: np.array) -> tuple[np.array, np.array]:
    xCoords: np.array = 16 * np.sin(array)**3
    yCoords: np.array = 13 * np.cos(array) - 5 * np.cos(2 * array) - 2 * np.cos(3 * array) - np.cos(4 * array)

    return (xCoords, yCoords)

# 3D
def Hypocycloid(array: np.array) -> tuple[np.array, np.array, np.array]:
    xCoords: np.array = 4 * np.cos(array) + np.cos(4 * array)
    yCoords: np.array = 4 * np.sin(array) - np.sin(4 * array)
    zCoords: np.array = array / 5

    return (xCoords, yCoords, zCoords)

def Lissajous(array: np.array) -> tuple[np.array, np.array, np.array]:
    xCoords: np.array = np.sin(2 * array / 3 + np.pi / 4)
    yCoords: np.array = np.sin(array)
    zCoords: np.array = array

    return (xCoords, yCoords, zCoords)

names: list[str] = ["Epitrochoid", "Butterfly curve", "Heart curve", "Hypocycloid", "Lissajous curve"]
coords: list[tuple] = []

coords.append(Epitrochoid(np.arange(0, 20*np.pi, 0.01)))
coords.append(Butterfly(np.arange(0, 12*np.pi, 0.01)))
coords.append(Heart(np.arange(0, 2*np.pi, 0.01)))
coords.append(Hypocycloid(np.arange(0, 10*np.pi, 0.01)))
coords.append(Lissajous(np.arange(0, 50*np.pi, 0.01)))

if plotNum < 3:
    plt.figure(figsize=(15, 15))
    plt.title(names[plotNum])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.plot(coords[plotNum][0], coords[plotNum][1], color = "red")
    plt.show()
else:
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter3D(coords[plotNum][0], coords[plotNum][1], coords[plotNum][2], c = coords[plotNum][2], cmap='viridis')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(names[plotNum])
    plt.show()