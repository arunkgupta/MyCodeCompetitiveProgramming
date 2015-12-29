def pythagorean_triplet(sides_sum):
    for c in range(2, sides_sum):
        for a in range(1, c):
            b = sides_sum - c - a

            if c**2 == b**2 + a**2:
                print "a = {}, b = {}, c = {}, product of abc = {}".format(a, b, c, a*b*c)
                return

if __name__=="__main__":
    sum_of_sides = 1000
    pythagorean_triplet(sum_of_sides)