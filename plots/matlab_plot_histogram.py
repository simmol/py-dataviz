from data import airports, routes
from utils import calc_dist

import matplotlib.pyplot as plt

route_lengths = routes.apply(calc_dist, args=(airports, ), axis=1)

if __name__ == "__main__":
    plt.hist(route_lengths, bins=20)
    plt.show()
