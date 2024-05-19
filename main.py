#import random and time module
import random
import time
#print ^ 90 times
for i in range(90):
    print("^",end="")
    time.sleep(0)

print()
print("\t\t!! Welcome to Kaun Banega Crorepati(Lite)!!")

for i in range(90):
    print("^",end="")
    time.sleep(0)
print()
a=input("Enter Your Name =  ")
for i in range(90):
    print("-",end="")
    time.sleep(0)
print()
print("\n\t\tOkay ",a," Let's Start The Game, Hope you enjoy it😊")
print(".............................................................................................................................................")
print("Instructions:  Enter Your answer in alphabet format like a,b,c  &  read the question carefully")
time.sleep(1)
questions=["Which is the No. 1 cleanest city in the India","What is the  largest city in India by population?","Who is the  current president of India?","Apple's Laptop is Also Known as,First Apple Computer is Known as","What is the formula of water?","Who is known as the “Iron Man” of India?","Who is the king of the pencil box?","Salman is the brother of Mohan ,Mikki is the sister of Salman ,Prav is the brother of Mikki, Guru is the father of Mikki ,Mikki is the daughter of Mohan. Then, the uncle of Prav is?","Who is the father of english literature and poetry?","Which animal is known as the king of the jungle?","Who is the largest mammal on earth?","Who called the brain of the computer system?","Multiply: (x – 4)(x + 5)","Which is India’s southernmost city?","What is the national sweet of India?","5⬜2⬜1 = 6  Add the right symbols","What is the oldest living city in India?","How many hours are there in a day?","Simplify:(4 – 5) – (13 – 18 + 2)"]
answer=["Indore","Mumbai","Dropti Murmu","Mackbook","H₂O","Sardar Vallabhbhai Patel","The Eraser","Salman","Geoffrey Chaucer","Lion","The blue whale","Central Processing Unit(CPU)","x^2 + x - 20","Kanyakumari","jalebi","+ -","Varanasi","24","2"]
wronganswers=[["Mumbai","Bhopal","Hyderabad"],["New Delhi","Surat","Kolkata"],["Narendra Modi","Dr.Rajendra Prasad","Arvind Kejriwal"],["Thinbook","ChromeBook","Notebook"],["O₂","CO₂","O₃"],["Rabindranath Tagore","Mahatma Ghandi","Bhagat Singh"],["The scale","The sharpener","The Pen"],["Guru","Mohan","Prav"],["William Blake","Nissim Ezekiel","George Orwell"],["Giraffe","Elephant","Crocodile"],["The Camel","The African elephants","The Bats"],["Monitor","Random-access memory(RAM)","Monitor"],["x^2 - 4x - 20","x^2 - x - 20","x^2 + 5x - 30"],["Kerla","Visakhapatnam","Tamil Nadu"],["RasMalai","GualabJamun","Kaju katli"],["- ×","+ ÷","- -"],["Pune","Jaipur","Satna"],["12","48","365"],["1","5","-1"]]
attempquestion=[]
count=1
amount=0
while True:
    while True:
        selectquestion=random.choice(questions)
        if selectquestion in attempquestion:
            pass
        elif selectquestion not in attempquestion:
            attempquestion.append(selectquestion)
            questionindex=questions.index(selectquestion)
            correctanswer=answer[questionindex]
            break
    optionslist=[]
    inoptionlist=[]
    optioncount=1
    while optioncount<4:
        optionselection=random.choice(wronganswers[questionindex])
        if optionselection in inoptionlist:
            pass
        elif optionselection not in inoptionlist:
            optionslist.append(optionselection)
            inoptionlist.append(optionselection)
            optioncount+=1
    optionslist.append(correctanswer)
    alreadydisplay=[]
    optiontodisplay=[]
    a1=True
    while a1:
        a=random.choice(optionslist)
        if a in alreadydisplay:
            pass
        else:
            alreadydisplay.append(a)
            optiontodisplay.append(a)
            a1=not True
    a1=True
    while a1:
        b=random.choice(optionslist)
        if b in alreadydisplay:
            pass
        else:
            alreadydisplay.append(b)
            optiontodisplay.append(b)
            a1=not True
    a1=True
    while a1:
        c=random.choice(optionslist)
        if c in alreadydisplay:
            pass
        else:
            alreadydisplay.append(c)
            optiontodisplay.append(c)
            a1=not True
    a1=True
    while a1:
        d=random.choice(optionslist)
        if d in alreadydisplay:
            pass
        else:
            alreadydisplay.append(d)
            optiontodisplay.append(d)
            a1=not True
    right_answer=""
    if correctanswer==a:
        right_answer="a"
    elif correctanswer==b:
        right_answer="b"
    elif correctanswer==c:
        right_answer="c"
    elif correctanswer==d:
        right_answer="d"
    
    print("--------------------------------------------------------------------------------------------------------------------")

    print("\t\t\tAmount Win - ",amount)
    print("-----------------------------------------------------------------------------------------------------------")
    time.sleep(1)
    print("\n\t\tQuestion ",count," On your screen")
    print("\t      ")
    time.sleep(1)
    print("  |  Question - ",selectquestion)
    print("\t\t    ")
    
    time.sleep(1)
    print("\t|  A. ",a)
    print("\t   ")
    time.sleep(1)
    print("\t|  B. ",b)
    print("\t  ")
    time.sleep(1)
    print("\t|  C. ",c)
    print("\t   ")
    time.sleep(1)
    print("\t|  D. ",d)
    print("\t   ")
    
    useranswer=input("\t\tEnter Correct Option\t   or \t press Q to quit.\n\t\t\t...").lower()
    print("\t   ")
    if useranswer==right_answer:
        if count==1:
            amount=1000
        elif count==2:
            amount=2000
        elif count==3:
            amount=3000
        elif count==4:
            amount=4000
        elif count==5:
            amount=5000
        elif count==6:
            amount=10000
        elif count==7:
            amount=15000
        elif count==8:
            amount=20000
        elif count==9:
            amount=25000
        elif count==10:
            amount=40000
        elif count==11:
            amount=80,000
        elif count==12:
            amount=160000
        elif count==13:
            amount=320000
        elif count==14:
            amount=640000
        elif count==15:
            amount=1250000
        elif count==16:
            amount=2500000
        elif count==17:
            amount=5000000
        elif count==18:
            amount=10000000
        elif count==19:
            amount=70000000
          
            print("\n\n\n\n")
            print("---------------------------------------------------------------------------------")
            print("\t\t\t !! Congratulations!! ")
            print("          ")
            print("\n\n\t\t You Won Rs. ",amount)
            print()
            break
        print("\n\n\n\n ------------------------------------------------------------------------------------------------------------------------------------------")
 
        print("\t\t\t !!Congratulations Dear 🥳!! ")
        print("\t        ")
    
        print("\t\t\t   *Right Answer* ")      
        count+=1
    elif useranswer=="q":
            print("\n\n\t\t You Won Tolat Rs. ",amount)
            break
    else:
        print("-------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("\t\t\tWrong Answer")
        print("-------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("\n\n\t\t \tYou Won Total Rs. ",amount)
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        break
         