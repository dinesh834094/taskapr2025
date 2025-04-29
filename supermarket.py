items={'a':10,
       'b':20,
       'c':30}
price=0
price_list=[]
ilist=[]
qlist=[]
plist=[]
total_price=0
fina_final_price=[]

option= int(input('enter number'))

if option==1:
 print(items)
 for i in range(len(items)):
  inp1=int(input('enter number 1 for buy and 2 for exit'))
  if inp1==2:
   break
  if inp1==1:
   item=input('enter items')
   quantity= int(input('enter quantity' ))
   if item in items.keys():
    price=quantity*(items[item])
    price_list.append((item,quantity,items,price))
    total_price+=price
    ilist.append(item)
    qlist.append(quantity)
    plist.append(price)
    gst=(total_price*5)/100
    finalamount=gst+total_price
   else:
    print('item not in list')
else:
 print('entered wrong number')
 inp=input('enter bill yes or no')
 if inp=='yes':
  pass
if finalamount!=0:
  for i in range(len(price_list)):
   print(i,ilist[i],qlist[i],plist[i])
 
   




   

   
   

 


           
       

     
     
     



    









               
             

 
                

               
        
    
        


      

       
    




    


