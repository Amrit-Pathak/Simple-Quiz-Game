print("Welcome to the quiz!")
score=0
a= input("Would you like to participate in the quiz?*(Yes/No): ").lower()
if a=="yes":
    print("Let's get started...")
else:
    print("No worries, Bye!")
    quit()

print("This is a Jujutsu Kaisen quiz\nYou'll be prsented with 5 questions\nTry getting them right.\nGoodluck!")

question= input("Who's The Strongest character in all of JJK?: ").lower()
if question== "satoru gojo":
    print("Right Answer")
    score+=1
elif question=="gojo":
    print("Right Answer")
    score+=1
elif question== "sukuna":
    print("He is a FRAUD")
else:
    print("Wrong Answer, The right answeris Satoru Gojo")

question_2= input("Whose epithet is " +"The One Who Left It All Behind"+"? : ").lower()
if question_2== "toji":
    print("Right Answer")
    score+=1
elif question_2== "toji zenin":
    print("Right Answer")
    score+=1
else:
    print("Wrong Answer, The right answer is Toji Zenin")

question_3= input("Which Shikigami is considered as the Magnum Opus of the Ten Shadows Technique: ").lower()
if question_3== "mahoraga":
    print("Right Answer")
    score+=1
else:
    print("Wrong Answer, The right answeris Mahoraga")

print (f"Your Total Score is: {score}")
print (f"You Got: {(int(score/3)*100)}% right")
