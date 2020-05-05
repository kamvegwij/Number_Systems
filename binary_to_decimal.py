class Number_Sys:

    def __init__(self, num):
        self.num = str(num)

    def binary_to_decimal(self):
        ''' Funtion will take in a binary number and convert it to decimal '''
        exp = len(self.num)-1 # raise self.num to exp. We don't know the largest val of exp that's why it's set to the length of the number
        my_list = []
        for ik in range(len(self.num)):
            ind_num = int(self.num[ik])
            prod_num = ind_num * 2**exp
            if ind_num == 0:
                continue # skips if condition is not met
            else:
                my_list.append(prod_num)
            exp = exp - 1
        total = 0
        print(my_list)
        for val in my_list:
            total += val
        return 'Decimal value of binary number: {0} is {1}'.format(self.num, total)
# logical error that needs to be fixed in the function binary_to_decimal..

    def to_binary(self):
        ''' Converts a number to binary. Parameter will take a number and the base '''
        remainder = 0
        my_list = []
        binary = []
        bin_digs = [0, 0, 0, 0]
        while int(self.num) > 0:
            remainder = int(self.num) % 2
            my_list.append(remainder)
            self.num = int(self.num)//2

        if len(my_list) == 5:
            my_list.extend(bin_digs)
        
        my_list.reverse()  # reverse because you read remainders from the bottom up
        return my_list
    
    def from_hex(self):
        pass




 #instantiation of the class objects and testing of the program here:

my_var = input('Enter the number: ')
my_var2 = int(input('Enter the base you want to change to(2 or 10): '))

if my_var2 == 10:
    MyInstance = Number_Sys(my_var)
    print(MyInstance.binary_to_decimal())

if my_var2 == 2:
    MyInstance = Number_Sys(int(my_var))
    print(MyInstance.to_binary())

    





        
