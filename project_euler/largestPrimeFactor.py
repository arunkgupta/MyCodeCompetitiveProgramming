from math import sqrt
from sys import argv


def largest_prime_factor(number):
    if not number%2:
        print "2"
        number /= 2
    for i in range(3,int(sqrt(number)),2):
        while not number%i:
            print i
            number /= i
    if number > 2:
        print number

if __name__ == '__main__':
    largest_prime_factor(int(argv[1]))
