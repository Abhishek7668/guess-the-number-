#guess number
print("guess number 1 to 10")
import random
b=random.randint(1,10)
c=0


while True:
  a=int(input("enter your number:\n"))
  if b==a:
      c+=1
      
      print("total attemt:",c)
      print("you win \n")
      break
  elif a>b:
    print("guess small number\n")
    c+=1
    print("your attempt",c)
  elif a<b:
     print("guess big number\n")
     c+=1
     print("your attempt",c)
     

