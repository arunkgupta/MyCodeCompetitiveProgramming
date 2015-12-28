

def largest_number():
    l = []
    for i in range(999,100,-1):
        for j in range(999,100,-1):
            if is_pallindrom(i*j):
                print i, j, i*j
                l.append((i * j))
    return max(l)

def is_pallindrom(number):
    now_string = str(number)
    return now_string == now_string[::-1]

if __name__ == '__main__':
     p = largest_number()
     print p