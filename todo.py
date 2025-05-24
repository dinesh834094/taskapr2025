Task=[]
while True:

 print('\n todo list ')
 print('1 enter to add task')
 print('2 enter to remove task')
 print('3 exit task')

 choice=int(input('enter number'))
 if choice==1:
  task=input('enter task to add')
  Task.append(task)
  print(f'task has been added:{task}')

 elif choice==2:
  task=input('eneter task to remove')
  if task in Task:
   Task.remove(task)
   print('task removed')
  else:
   print('task not found')
 elif choice==3:
   q=int(input('enter number to exit'))
   if q==3:
    print(f'you are exited:{q}')

   

  
  
 
   
 

        
     