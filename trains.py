trains=["Express 101", "Superfast 202", "Passenger 303"]
bookings=[]
while True:
 
 print('\n railway reservation system')
 print('1 show the availale seats  ')
 print('2 to book tickets ')
 print('3 to cancel the tickets')
 print('4 to exit')

 choice= int(input('enter number'))
 if choice==1:
  print(trains)
 elif choice==2:
  ticket=input('enter train num to book tickets')
  if ticket in trains:
   bookings.append(ticket)
   print('your ticket has been booked')
  else:
   print('enter valid train number to book ')
 elif choice==3:
  ticket =input('enter train number to cancel')
  if ticket in trains:
   bookings.remove(ticket)
   print('your ticket has been cancelled')
  else:
   print('enter valid train number to cancel ')
 
 elif choice==4:
  print('you are exited')



  


