import matplotlib.pyplot as plt
import argparse

def main():
    parser = argparse.ArgumentParser(description="Plots numbers as a barplot and saves them to the current working directory.")
    parser.add_argument('integers', metavar='number', type=int, nargs='+', help='The numbers to plot. Need to be integers.')
    args = parser.parse_args()

    plt.figure()
    plt.bar(range(len(args.integers)), args.integers, color='blue')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title('Fancy Bar Plot')

    print('Very nice numbers. Saving the resulting plot to barplot.png.')
    plt.savefig('barplot.png')
