"""
Write code that can tell if a number is prime.
A prime number is a number that is only divisible by 1 and itself.
"""
from tkinter import messagebox, simpledialog, Tk


if __name__ == '__main__':
    window=Tk()
    window.withdraw()
    # TODO)
    #  1. Ask the user for a number
    num1=simpledialog.askstring(title=None, prompt= "What number do you want to test for it being prime or not?")
    #  2. Use a for loop, if statement, and modulo to find if the number
    #     is prime.
    num_2=2
    while num_2<99999999999999999999999999:

        if num1/num_2 == 1 and num1:
            var_1 = True
        if num1 % num_2 == 0:
            var_2 = True

        if var_1 == True and var_2 == False:
            messagebox.showinfo(title=None, prompt= "Your number ' + str(num1) + ' is prime.")
            exit()

        elif var_1 == True and var_2 == True:
                messagebox.showinfo(title=None, prompt="Your number ' +  str(num1) + ' isn't prime")
                exit()

        else:
            num_2=num_2+1

    #  3. If the number is divisible by any number other than 1 or itself,
    #     the number is not prime.
    pass
