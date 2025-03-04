bill_total = 210

discount1 = 10
discount2 = 20

if bill_total > 100 and bill_total < 200:
    print('Bill is greater than 100')
    bill_total = bill_total - discount1
elif bill_total > 200:
    print('Bill is greate than 200!')
    bill_total = bill_total - discount2
else:
    print('bill is less than 100')



print('Total bill after discount:' , bill_total)

#Light is currently off
current = False

if current:
    current = False
    print('Turning light off')

if not current:
    current = True
    print('Turning light on')

print('Light is currently:', current)

loyalty_customer = True
total_bill = 124

if loyalty_customer and total_bill > 100:
    #give 20% discount
    total_bill = total_bill - (float(total_bill)/ 100) * 20
elif total_bill > 100:
    #give 10% discount
    total_bill = total_bill - (float(total_bill)/ 100) * 10
else:
    #sorry no discount, 5% service charge applied.
    print('Sorry, no discount ...')

print('Total Bill: ', float(total_bill))