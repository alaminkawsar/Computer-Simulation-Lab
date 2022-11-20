from ast import Num


def middle_square_method(intitial_number, digit, numOfIteration):

    num = intitial_number
    for i in range(0,numOfIteration):

        num = num*num
        st = str(num)
        length = len(st)
        abduct = length-digit
        print("{} Number is=".format(i+1),end=" ")
        if abduct<=0:
            print(num)
        else:
            left = int(abduct/2)
            new_number = st[left:left+digit]
            num = int(new_number)
            print(num)


    

if __name__ == '__main__':

    initial_number = 1444
    digit_num = 4
    numOfIteration = 20
    middle_square_method(initial_number, digit_num, numOfIteration)