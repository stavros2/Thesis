import random
from matplotlib import pyplot as plt
from statistics import mean;


if __name__ == "__main__":
    i = 0;
    y = [];
    while i < 1000:
        a = random.randrange(0,100) + random.random();
        y.append(a);
        i += 1;
    x = range(1000);
    print(mean(y))
    plt.scatter(x,y)