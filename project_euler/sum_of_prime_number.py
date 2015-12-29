def sum_of_prime(number):
    prime = []
    for n in xrange(2,number + 1):
        for p in prime:
            if n % p == 0:
                break
            if n < p * p:
                prime.append(n)
                break
        else:
            prime.append(n)
    return sum(prime)

if __name__ == "__main__":
    a = sum_of_prime(2000000)
    print a