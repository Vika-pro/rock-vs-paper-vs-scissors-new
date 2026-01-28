from tkinter import *
import random
import os
from PIL import Image, ImageTk

window = Tk()
window.geometry("800x450")
window.title("ROCK PAPER SCISSORS")

frame = Frame(window)
frame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

name = Label(frame, text="Rock Paper Scissors - Player vs Computer", font="100")
name.place(x=250, y=20)

label1 = Label(frame, text="Player", font="normal 15")
label2 = Label(frame, text="VS", font="normal 15")
label3 = Label(frame, text="Computer", font="normal 15")

label1.place(x=80, y=50, width=200)
label2.place(x=350, y=150, width=100)
label3.place(x=500, y=50, width=200)

def load_image(filename):
    path = os.path.join(os.path.dirname(__file__), filename)
    img = Image.open(path)
    img = img.resize((200, 200))
    return ImageTk.PhotoImage(img)

rock_png = load_image("rock.png")
paper_png = load_image("paper.png")
scissors_png = load_image("scissors.png")

user_image = Label(frame, image="")
user_image.place(x=80, y=100)

comp_image = Label(frame, image="")
comp_image.place(x=500, y=100)

label4 = Label(frame, text="", font="normal 20", width=15, borderwidth=2, relief="solid")
label4.place(x=275, y=280)

def check_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        label4.config(text="Tie")
    elif (user_choice == "Rock" and comp_choice == "Paper") or \
         (user_choice == "Paper" and comp_choice == "Scissors") or \
         (user_choice == "Scissors" and comp_choice == "Rock"):
        label4.config(text="Computer wins")
    else:
        label4.config(text="U win")

def Rock():
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    user_image.config(image=rock_png)
    if computer_choice == "Rock":
        comp_image.config(image=rock_png)
    elif computer_choice == "Paper":
        comp_image.config(image=paper_png)
    else:
        comp_image.config(image=scissors_png)
    check_winner("Rock", computer_choice)

def Paper():
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    user_image.config(image=paper_png)
    if computer_choice == "Rock":
        comp_image.config(image=rock_png)
    elif computer_choice == "Paper":
        comp_image.config(image=paper_png)
    else:
        comp_image.config(image=scissors_png)
    check_winner("Paper", computer_choice)

def Scissors():
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    user_image.config(image=scissors_png)
    if computer_choice == "Rock":
        comp_image.config(image=rock_png)
    elif computer_choice == "Paper":
        comp_image.config(image=paper_png)
    else:
        comp_image.config(image=scissors_png)
    check_winner("Scissors", computer_choice)

b1 = Button(frame, text="Rock", font="10", width=15, command=Rock)
b1.place(x=100, y=330)

b2 = Button(frame, text="Paper", font="10", width=15, command=Paper)
b2.place(x=325, y=330)

b3 = Button(frame, text="Scissors", font="10", width=15, command=Scissors)
b3.place(x=550, y=330)

window.mainloop()



# from tkinter import *
# import random
# import os
# from tkinter import PhotoImage


# window = Tk()

# window.geometry("800x400")
# window.title("ROCK PAPER SCISSORS")

# frame = Frame(window)
# frame.place(relx=0.01,rely=0.01, relwidth=0.98, relheight=0.98)

# name = Label(frame, text = "Rock Paper Scissors - Player vs Computer", font = "100")
# name.place(x=250, y=20)

# label1 = Label(frame, text= "Player", font="normal 15")

# label2 = Label(frame, text= "VS", font="normal 15")

# label3 = Label(frame, text= "Computer", font="normal 15")

# label1.place(x=80, y=50, width=100)
# label2.place(x=350, y=50, width=100)
# label3.place(x=600, y=50, width=100)



# base_path = os.path.dirname(__file__)
# path_to_rock = os.path.join(base_path, "rock.png")
# rock_png = PhotoImage(file=path_to_rock, width=200, height=200)



# path_to_scissors = os.path.join(base_path, "scissors.png")
# scissors_png = PhotoImage(file=path_to_scissors, width=200, height=200)


# path_to_paper = os.path.join(base_path, "paper.png")
# paper_png = PhotoImage(file=path_to_paper, width=200, height=200)


# user_image = Label(frame, image="")
# user_image.place(x=80, y=100)

# comp_image = Label(frame, image="")
# comp_image.place(x=300, y=100)

# label4 = Label(frame, text="", font="normal 20", width= 15, borderwidth=2, relief="solid")
# label4.place(x=275, y=250)

# def Rock():
#     user = "Rock"
#     computer = random.choice(["Rock", "Paper", "Scissors"])
#     user_image.config(image=rock_png)
#     if user == computer:
#         label4.config(text="Tie")
#         comp_image.config(image=rock_png)
#     elif computer == "Paper":
#         label4.config(text="Computer wins")
#         comp_image.config(image=paper_png)
#     else:
#         label4.config(text="U win")
#         comp_image.config(image=scissors_png)



# b1 = Button(frame, text="Rock", font="10", width=20, command=Rock)
# b1.place(x=100, y=300)
# def Paper():
#     user = "Paper"
#     computer = random.choice(["Rock", "Paper", "Scissors"])
#     user_image.config(image=paper_png)
#     if user == computer:
#         label4.config(text="Tie")
#         comp_image.config(image=paper_png)
#     elif computer == "Scissors":
#         label4.config(text="Computer wins")
#         comp_image.config(image=scissors_png)
#     else:
#         label4.config(text="U win")
#         comp_image.config(image=rock_png)





# b2 = Button(frame, text="Paper", font="10", width=20, command=Paper)
# b2.place(x=300, y=300)
# def Scissors():
#     user = "Scissors"
#     computer = random.choice(["Rock", "Paper", "Scissors"])
#     user_image.config(image=scissors_png)
#     if user == computer:
#         label4.config(text="Tie")
#         comp_image.config(image=scissors_png)
#     elif computer == "Rock":
#         label4.config(text="Computer wins")
#         comp_image.config(image=rock_png)
#     else:
#         label4.config(text="U win")
#         comp_image.config(image=paper_png)






# b3 = Button(frame, text="Scissors", font="10", width=20, command=Scissors)
# b3.place(x=500, y=300)

# window.mainloop()