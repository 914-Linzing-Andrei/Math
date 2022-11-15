import matplotlib.pyplot as plt
import numpy as np

def normal():
    x = np.arange(1,1000) #here we set the Ox axis to have all values from [1,1000]
    y = np.cumsum([(-1) ** (i + 1) / i for i in range(1,1000)]) # calculates the sum at certain points paralel to the Oy axi
    y2 = np.array([np.log(2) for i in range(1,1000)]) # puts ln(2) for every paralel axis to the Ox

    plt.title("Line graph")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")

    plt.plot(x,y, color='green', marker="o")
    plt.plot(y2,color = 'red',marker = '*')

    plt.show() #print the plot

def rearanged():
    x = np.arange(1,1000)
    y = np.cumsum([(1 / i - 1 / (2 * i) - 1 / (2 * i + 2)) for i in range(1,1998) if i % 2 != 0])
    y2 = np.array([np.log(2) for i in range(1,1000)])

    plt.title("Line graph")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")

    plt.plot(x,y, color='green', marker="o")
    plt.plot(y2,color = 'red',marker = '*')

    plt.show()

def print_options():
    print("1. Normal series")
    print("2. Rearanged series")
    print("x. Exit")

def run_menu():
    #this is a menu for easier navigation
    while(True):
        print_options()
        x = input("Choose one option: ")
        if x == 'x':
            break
        x = int(x)
        if(x == 1):
            normal()
        if(x == 2):
            rearanged()

if __name__ == '__main__':
    run_menu()
