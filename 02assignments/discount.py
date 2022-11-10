#If the subtotal is $50 or greater and today is Tuesday or Wednesday, your program must subtract 10%
#from the subtotal. Your program must then compute the total amount due by adding sales tax of 6% to
#the subtotal. Your program must print the discount amount if applicable, the sales tax amount, and
#the total amount due.

#Please enter the subtotal: 42.75
#Sales tax amount: 2.56
#Total: 45.31
#to get the total, first divide 0.06 from the subtotal, then add that to the total. 
total_bef_tax = float(input("Please enter the subtotal: $"))

discount = .10 * total_bef_tax

discount_sub = total_bef_tax - discount

tax = 0.06 * total_bef_tax 

tax_add  = total_bef_tax + tax

print(f'Discount amount: {discount:.02f}')
print(f'Sales tax amount: {tax:.02f}')
total_aft_tax = print(f"Total ${tax_add:.02f}")

from datetime import datetime
time = datetime.now()
date_of_week = datetime.weekday(time)

if date_of_week == 1 or date_of_week ==2:
   if total_bef_tax >=50:
      new_total_bef_tax = total_bef_tax *0.6
      tax = 0.06 * new_total_bef_tax 
      tax_add  = new_total_bef_tax + tax
else: subtotal = total_bef_tax * 1.06

print(f"{subtotal:.2f}")

