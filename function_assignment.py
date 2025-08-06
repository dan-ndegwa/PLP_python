def calculate_discount(price, discount_percent):
    if discount_percent>=(20):
        return (price-(price*(discount_percent/100)))
    else:
        return(price)

price = float(input("Enter the original price: "))
discount = float(input("Enter the discount: "))

output = calculate_discount(price, discount)

print(f'The final_price is:{output}')