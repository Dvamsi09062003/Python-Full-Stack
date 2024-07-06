name ="VAMSI"
password ="0906"
user_name = input("enter the user name:")
passwords = input("enter the password:")
s = '''
   1.credit
   2.debit
   3.mini statement
   4.exit
'''
Amount = 1000
if name==user_name and passwords==password:
    while(1):
        print(s)
        option = int(input("enter the option:"))
        if option==1:
            credit_amount = float(input("enter the credit amount:"))
            print("amount after credit:", Amount+credit_amount)
        elif option == 2:
            debit_amount = float(input("enter the debit amount:"))
            print("amount after debit:", Amount-debit_amount)
        elif option == 3:
            print("mini statement")
            print(Amount)
        elif option==4:
            break;
        else:
            print("enter the displayed values from 1 to 4")
            break;
            
else:
    print("incoorect credentials")