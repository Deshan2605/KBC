# Make Kaun Banega Crorepati game by displaying the questions to the user and showing the amount that he's gonna take home after winning
# You can use list and can also give random questions to the user
import random
import string
points=0 # points
lv=1 # level
print("LEVEL=",lv)
print("TOTAL POINTS=",points)

a="In the game of ludo the discs or tokens are of how many colours?"
b="Which of these are names of national parks located in Madhya Pradesh?"
c="Where was the BRICS summit held in 2014?"
d="Who wrote the introduction to the English translation of Rabindranath Tagore's Gitanjali?"
l=[str(a), str(b), str(c),str(d)]
user1=""
user2=""
user3=""
user4=""

# SOME COMMENT ADDED

for i in range(len(l)-1, 0, -1):
     
    # Pick a random index from 0 to i
    j = random.randint(0, i + 1)
   
    # Swap arr[i] with the element at random index
    l[i], l[j] = l[j], l[i]


for choice in l:
   print(choice)
   if (choice==a):
     print("(A) ONE")
     print("(B) TWO")
     print("(C) THREE")
     print("(D) FOUR")
     user1=input("ANSWER: ")

     if(user1=="D"):
      if(lv==1):points+=10000
      elif(lv==2):points+=10000
      elif(lv==3):points+=10000
      elif(lv==4):points+=10000
         
      lv+=1   
      print("\nLEVEL=",lv)
      print("TOTAL POINTS=",points)
      if(lv!=5):
       print("\nYOUR NEXT QUESTION IS:-")


     else: 
        print("SORRY, YOUR ANSWER IS INCORRECT. BETTER LUCK NEXT TIME.")
        print("YOUR TOTAL SCORE IS: ", points, "points")
        break



 
   elif (choice==b):
     print("(A) Krishna and Kanhaiya")
     print("(B) Kanha and Madhav")
     print("(C) Ghanshyam and Murari")
     print("(D) Girdhar and Gopal")
     user2=input("ANSWER: ")

     if(user2=="B"):
      if(lv==1):points+=10000
      elif(lv==2):points+=10000
      elif(lv==3):points+=10000
      elif(lv==4):points+=10000
         
      lv+=1   
      print("\nLEVEL=",lv)
      print("TOTAL POINTS=",points)
      if(lv!=5):
       print("\nYOUR NEXT QUESTION IS:-")

     else: 
        print("SORRY, YOUR ANSWER IS INCORRECT. BETTER LUCK NEXT TIME.")
        print("YOUR TOTAL SCORE IS: ", points, "points")
        break



   elif (choice==c):
     print("(A) Brazil")
     print("(B) India")
     print("(C) Russia")
     print("(D) China")
     user3=input("ANSWER: ")

     if(user3=="A"):
      if(lv==1):points+=10000
      elif(lv==2):points+=10000
      elif(lv==3):points+=10000
      elif(lv==4):points+=10000
         
      lv+=1
      print("\nLEVEL=",lv)
      print("TOTAL POINTS=",points)  
      if(lv!=5):
       print("\nYOUR NEXT QUESTION IS:-")

     else: 
        print("SORRY, YOUR ANSWER IS INCORRECT. BETTER LUCK NEXT TIME.")
        print("YOUR TOTAL SCORE IS: ", points, "points")
        break
     



   elif (choice==d):
     print("(A) P.B. Shelley")
     print("(B) Alfred Tennyson")
     print("(C) W.B. Yeats")
     print("(D) T.S. Elliot")
     user4=input("ANSWER: ")
     
     if(user4=="C"):
      if(lv==1):points+=10000
      elif(lv==2):points+=10000
      elif(lv==3):points+=10000
      elif(lv==4):points+=10000
         
      lv+=1   
      print("\nLEVEL=",lv)
      print("TOTAL POINTS=",points)
      if(lv!=5):
       print("\nYOUR NEXT QUESTION IS:-")
     else: 
        print("SORRY, YOUR ANSWER IS INCORRECT. BETTER LUCK NEXT TIME.")
        print("YOUR TOTAL SCORE IS: ", points, "points")
        break

if(user1=="D" and user2=="B"and user3=="A"and user4=="C"):
   print("Congratulations, you have won the game. Your total points are 40,000.")