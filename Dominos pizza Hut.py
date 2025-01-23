orders=[]
print('Menu Card')
print('1.Pizza')
print('2.Breadsticks')
print('3.Pasta')
print('4.Burger')
print('5.Cake')
print('6.Chips')
ch='y'
while ch=='y':
    n=int(input('Enter any item:'))
    orders.append(n)
    ch=input('Do You want any item(y/n):')

if n in orders:
    i=orders.index(n)
    m=int(input('Do you want to modify any item(y/n):'))
    orders[i]=m
    print('Is Available in Your Menu Card')
else:
    print('Sorry item is not available')
if ch==1:
    orders.append('Pizza')
elif ch==2:
    orders.append('Breadsticks')
elif ch==3:
    orders.append('Pasta')
elif ch==4:
    orders.append('Burger')
elif ch==5:
    orders.append('Cake')
elif ch==6:
    orders.append('Chips')
print(orders)
