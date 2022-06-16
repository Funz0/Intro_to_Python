import math

#Problem 1: Roots
#Compute and print both roots of the quadratic equation x2-5.86 x+ 8.5408.

#Hint: recall that the roots of a quadratic equation ax2+bx+c are x=

    # −b ± √ b^2 − 4ac / 2a 
    
def quadratic(a, b, c):
    disc_root = math.sqrt(abs(b*b - 4*a*c))
    pos_root = round((-b + disc_root)/(2*a), 4)
    neg_root = round((-b - disc_root)/(2*a), 4)
    
    print("The two values of x are: {} and {}".format(pos_root, neg_root))

quadratic(3,4,-1)
    
#Problem 2: Reciprocals
#Use a for loop to print the decimal representations of 1/2, 1/3, ..., 1/10, one on each line.
    
factorials = [1/2,1/3,1/4,1/5,1/6,1/7,1/8,1/9,1/10]
    
for i in factorials:
    decimal = round(float(i), 4) # round to 4 decimal places
    
    print("List item {}'s value as a decimal is {}".format(factorials.index(i) + 1, decimal))