# mortgage.py
#
# Exercise 1.7

# Mortgage calculator

principal = 500_000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    month += 1
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment

# If remaining principal is less than the monthly payment, adjust the payment to principal left.
    
    if payment > principal:
        payment = principal * (1+rate/12)

    print(f"Month #{month}, Total payment made: {round(total_paid,2)}, Balance remaining: {round(principal, 2)}")


print('Total paid', round(total_paid, 2))
print('Months', month)



