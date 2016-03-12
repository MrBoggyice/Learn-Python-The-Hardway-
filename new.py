'''
building a calculator program 
the calc_program which takes no 
parameters will at first take in
all the variables which n1 and n2
by using raw_input() to collect them
and then later on within it, another 
function called calc_num(n1, n2) which 
which takes in 2 parameters and does the
rest of the calculations for us

NB: the math module was not used so 
    don't expect much.
    thanks
    
fortune iyke
'''

def calc_program():
    n1 = int(raw_input("pick a number:  "))
    operator = raw_input("pick an operator. eg. + - /: ")
    n2 = int(raw_input("pick the next number: "))
   

    def calc_num(n1, n2):
    
        #for addition 
        if operator == "+":
            total = n1 + n2
            print "your answer is ", total
            do_more = raw_input("Do you wish to do more? y/n: ")
            
            if do_more == "y":
                total = n1
            elif do_more == "n":
                print "Thanks for using the calculator"
            else:
                print "Please choose yes or no appropriately by typing y or n"
                
       #for multiplication         
        elif operator == "*":
            product = n1 * n2
            print "your answer is ",  product
            
        #for division 
        elif operator == "/":
            quotient = n1 / n2
            print "your answer is ", quotient
            
        #for subtraction 
        elif operator == "-":
            difference = n1 - n2
            print "your answer is ",  difference 
        else:
            print "That wasn't an operator, please appropriately. eg. +, *, -, /"
    
    calc_num(n1, n2)

calc_program()
