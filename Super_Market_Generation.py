from datetime import datetime
name=input("Enter your name:")
#lists of items
lists='''
Rice    Rs 20/kg
Sugar   Rs 30/kg
Salt    Rs 20/kg
oil     Rs 80/kg
paneer  Rs 180/kg
Maggi   Rs 50/kg
Boost   Rs 90/each
Colgate Rs 85/each
'''
price=0
pricelist=[]
totalprice=0
Finalfinalprice=0
ilist=[]
qlist=[]
plist=[]

#rates for items
items={'Rice':20,
       'Sugar':30,
       'Salt':20,
       'oil':80,
       'paneer':180,
       'Maggi':50,
       'Boost':90,
       'Colgate':85}
option=int(input("for list of items press 1:"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to press 1 to buy and 2 for exit:")) 
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your items:") 
        quantity=int(input("Enter quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("sorry you entered item iss not avilable")
    else:
        print("you entered wrong number")
    inp=input("can i  bill the items yes or no :")
    if inp=='yes':
        pass
        if finalamount!=0:
            print(25*"=","VASUDEV supermarket",25*"-")
            print(28*" ","Vamsi")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"-")
            print("sno",8*"",'items',8*"",'quantity',3*"",'price')
            for i in range(len(pricelist)):
              print(i,8*' ',5*' ',ilist[i],3*' ',qlist[i],8*"" ,plist[i])     
            print(75*"-")    
            print(50*" ",'TotalAmount:','Rs',totalprice)
            print("gst amount",50*" ",'Rs',gst)
            print(75*"-")  
            print(50*" ",'FinalAmount:','Rs',finalamount)
            print(75*"-") 
            print(50*" ","Thanks for visiting")
            print(75*"-") 




