print("Enter 'x' foe exit." )
print("Enter two numbers to find HCL and LCM: ")
num1 = input()

if num1 =='x':
    exit()
else:
    num2 = input()
    number1 = int(num1)
    number2 = int(num2)
    
    temp1 = number1
    temp2 = number2

    while temp2 != 0:
        t = temp2
        temp2 = temp1%temp2
        temp1 = t
        
    hcl = temp1
    lcm = (number1 * number2)/hcl
    print("HCL = ", hcl)
    print("LCM = ", lcm)
    print("--------------------")

# Using the Euclidean Algorithm
# In this algorithm, we divide the greater by smaller and take the remainder. 
# Now, divide the smaller by this remainder. Repeat until the remainder is 0.
def compute_hcf(x, y):
    while(y):
        x, y = y, x%y
    return x

hcf = compute_hcf(300, 400)
print("The HCF is ",hcf)

# For example, if we want to find the H.C.F. of 54 and 24, 
# we divide 54 by 24. The remainder is 6. Now, we divide 24 by 6 and the remainder is 0. 
# Hence, 6 is the required H.C.F.