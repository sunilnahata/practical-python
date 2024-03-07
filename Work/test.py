principal = 100
rate = 0.05
payment = 50
total_paid = 0.0
month = 0



while principal > 0:
    month += 1
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment



# If remaining principal is less than the monthly payment, adjust the payment to principal left.
    if payment > principal:
        payment = principal * (1+rate/12)

    print(month, round(total_paid,2), round(principal, 2))



print('Total paid', round(total_paid, 2))
print('Months', month)