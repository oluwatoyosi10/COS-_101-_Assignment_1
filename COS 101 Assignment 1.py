principal = float(input("Enter the amount: "))
time = float(input("Enter the amount: "))
rate = float(input("Enter the amount: "))
simple_interest = (principal*time*rate)/100
compound_interest = principal * (1+rate/100)**time - 1
print(f'simple interest is: {simple_interest}')
print(f'compound interest is: {compound_interest}')
print("yusuf and sons")