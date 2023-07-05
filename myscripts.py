import sys

if len(sys.argv) != 3:
    print("Usage: python script.py arg1 arg2")
    sys.exit(1)

arg1 = sys.argv[1]
arg2 = sys.argv[2]


print(arg1)
print(arg2)
def add_and_multiply(a, b):
    add = a + b
    mul = a * b
    return add, mul

# Example usage
sum_result, product_result = add_and_multiply(int(arg1), int(arg2))
print("Sum:", sum_result) 
print("Product:", product_result)  

