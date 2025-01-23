msal =float(input('Enter Your Salary:'))
if msal<50000:
    tax = 5
elif 50000<=msal<100000:
    tax=15
else:
    tax=30
print('Tax is:',tax,"%")
taxAmt =msal*tax/100
print('Your Tax Amount is:',taxAmt)
