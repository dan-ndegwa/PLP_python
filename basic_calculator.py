# Define the function(Formula)

def sum(num_1,num_2):
    return (num_1+num_2)

def subtraction(num_1,num_2):
    return(num_1-num_2)

def multiply(num_1,num_2):
    return(num_1*num_2)

def div(num_1,num_2):
    return(num_1/num_2)

# User Input Engine

num_1 = float(input("Enter the first value: "))
num_2 = float(input("Enter the second value: "))

output_sum = sum(num_1,num_2)
output_diff = subtraction(num_1,num_2)
output_mult = multiply(num_1,num_2)
output_div = div(num_1, num_2)

# Print the output

print(f'The sum is: {output_sum}')
print(f'The difference is: {output_diff}')
print(f'The product is: {output_mult}')
print(f'The quotient is: {output_div}')