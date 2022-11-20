
def LCM(initial_seed, m, a, c, randomNums, noOfIteration):
    randomNums[0] = initial_seed
    for i in range(1, noOfIteration):
        randomNums[i] = ((randomNums[i - 1] * a) + c) % m



if __name__ == '__main__':
        
    initital_number = 13
    m = 7
    a = 3
    c = 3
    noOfIteration = 10

    randomNums = [0] * (noOfIteration)

    LCM(initital_number, m, a, c, randomNums, noOfIteration)

    for i in range(len(randomNums)):
        print("{}-Random Number is {}".format(i+1,randomNums[i]))
