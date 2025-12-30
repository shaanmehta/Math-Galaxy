# Name: Shaan Mehta
# Description: This is the Math Galaxy! This file contains a rough design of
#              the desired product. The buttons, labels, etc, for the required 
#              properties along with have been designed to show how the math game 
#              would appear without any functionality. 

# <-------------------------------Import Library------------------------------->
import random
from tkinter import ttk
from tkinter.ttk import Checkbutton
from tkinter.ttk import Progressbar
from tkinter import *


# Create the window.
mainScreen = Tk()
mainScreen.title("Shaan's Math Galaxy")
mainScreen.geometry("1024x768")
tab_control = ttk.Notebook(mainScreen)

# <-------------------------------Sources-------------------------------------->
# 1. Subsample(): 
# 2. Place(): 
# 3. LabelFrame():
# 4. Pack(): 
# 5. Spinbox - readonly: 


# <---------------------------------Home--------------------------------------->

# Create the first tab.
home = Frame(tab_control)
tab_control.add(home, text="Home")

# Set the background for this tab.
backgroundHome = PhotoImage(file="HomeBackground.png")
lbl_backgroundHome = Label(home, image = backgroundHome)
lbl_backgroundHome.place(x = 0, y = 0)

# Add a button to tell the user to view the options. Make this
# an image for visual preference.
Viewoptions = PhotoImage(file="ViewOptions.png")
resizedoptions = Viewoptions.subsample(4, 4)
click_to_options = Button(home, image=resizedoptions)
click_to_options.place(relx = 0.5, rely = 0.8, anchor = "center")

# <--------------------------------Options------------------------------------->

# Create the second tab.
options = Frame(tab_control)
tab_control.add(options, text='Options')

# Set the background for this tab.
backgroundOptions = PhotoImage(file="optionsBackground.png")
lbl_backgroundOptions = Label(options, image = backgroundOptions)
lbl_backgroundOptions.place(x = 0, y = 0)

# Add a label for the title.
options_name = Label(options, text="OPTIONS OF THE GALAXY",
                          font=("SPACE MISSION", 50), bg="black", fg="white")
options_name.place(relx=0.5, rely = 0.05, anchor = N)

# Add a subheading to introduce the user to the game.
userIntroduction = Label(options, text="Welcome to a fun math game \
where you can practice your skills with flashcards and become a math whiz! \
Decide your selections and begin!", font=("OpenSans-BoldItalic", 10),
                         bg="black", fg="white")
userIntroduction.place(relx = 0.5, rely = 0.2, anchor="center")

# Create a frame to hold the level options.
level_frame = LabelFrame(options, borderwidth=3, text="Choose Your Level",
                         bg="black", fg="white")
level_frame.place(relx=0.2, rely=0.37, anchor="center")

# Create radio buttons to allow the user to choose which level to play on.
choose_level = IntVar()

level1 = Radiobutton(level_frame, text="Level 1: Numbers 1-3", value = 1,
                     bg="black", fg="white", selectcolor="black",
                     variable=choose_level)
level2 = Radiobutton(level_frame, text="Level 2: Numbers 1-6", value = 2,
                     bg="black", fg="white", selectcolor="black",
                     variable=choose_level)
level3 = Radiobutton(level_frame, text="Level 3: Numbers 1-9", value = 3,
                     bg="black", fg="white", selectcolor="black",
                     variable=choose_level)
level4 = Radiobutton(level_frame, text="Level 4: Numbers 1-12", value = 4,
                     bg="black", fg="white", selectcolor="black",
                     variable=choose_level)

# Set the default option to level 1.
choose_level.set(1)

# Organize the choices inside the frame.
level1.pack(anchor = W)
level2.pack(anchor = W)
level3.pack(anchor = W)
level4.pack(anchor = W)

# Ask the user which operators they would like to have during the game.
# Create a frame to hold the options.
operators_frame = LabelFrame(options, text="Select Operators",
                             bg="black", fg="white")
operators_frame.place(relx=0.5, rely=0.37, anchor="center")

# Set check states for all operators.
addition_state = BooleanVar()
addition_state.set(False)
subtraction_state = BooleanVar()
subtraction_state.set(False) 
multiplication_state = BooleanVar()
multiplication_state.set(False)
division_state = BooleanVar()
division_state.set(False)

# Create a check button for each operator.
addition_state = Checkbutton (operators_frame, text = "Addition",
bg="black", fg="white", selectcolor="black", variable=addition_state)
subtraction_state = Checkbutton (operators_frame, text = "Subtraction",
bg="black", fg="white", selectcolor="black", variable=subtraction_state)
multiplication_state = Checkbutton (operators_frame, text = "Multiplication",
bg="black", fg="white", selectcolor="black", variable=multiplication_state)
division_state = Checkbutton (operators_frame, text = "Division",
bg="black", fg="white", selectcolor="black", variable=division_state)

# Organize the choices inside the frame.
addition_state.pack(anchor = W)
subtraction_state.pack(anchor = W)
multiplication_state.pack(anchor = W)
division_state.pack(anchor = W)

# Create a frame to hold the options of whether or not the user wants to
# include negative numbers.
negative_option_frame = LabelFrame(options, borderwidth=3, text="Include \
Negative Numbers?", bg="black", fg="white")
negative_option_frame.place(relx=0.8, rely=0.37, anchor="center")

# Create radio buttons to allow the user to choose which level to play on.
choose_negative = IntVar()
negative_option_yes = Radiobutton(negative_option_frame, text="Yes",
                     bg="black", fg="white", selectcolor="black",
                                  value=1, variable=choose_negative)
negative_option_no = Radiobutton(negative_option_frame, text="No",
                     bg="black", fg="white", selectcolor="black",
                                 value=2, variable=choose_negative)

# Place the choices inside the frame.
negative_option_yes.pack(anchor = W)
negative_option_no.pack(anchor = W)

# Create a Spinbox to allow the user to choose the number of questions to have.
# Set the range of questions and place it on the screen.
num_of_questions = Spinbox(options, from_ = 10, to = 25, state="readonly",
                           font=("OpenSans", 15),
                           background="white", fg="black")
num_of_questions.place(relx=0.58, rely=0.65, anchor="center",
                       width=50, height=50)

# Add a label for it.
questions = Label(options, text="Number of Questions:",
                  font=("OpenSans-Bold", 15), bg="black", fg="white")
questions.place(relx=0.42, rely = 0.65, anchor="center")
choose_num_of_questions = IntVar()

# Add a "Ready To Play" button for the user as a way for the user to confirm
# their selections. Make this an image for visual preference.
ReadyToPlay = PhotoImage(file="ReadyToPlay.png")
resizedReadyToPlay = ReadyToPlay.subsample(4, 4)
click_to_play = Button(options, image=resizedReadyToPlay)
click_to_play.place(relx = 0.5, rely = 0.82, anchor = "center")

# <------------------------------------Game------------------------------------>

# Create the third tab.
game = Frame(tab_control)
tab_control.add(game, text="Game")

# Set the background for this tab.
backgroundGame = PhotoImage(file="GameBackground.png")
lbl_backgroundGame = Label(game, image = backgroundGame)
lbl_backgroundGame.place(x = 0, y = 0)

# Add a label for the title of the game.
game_name = Label(game, text="The Space Race", font=("SPACE MISSION", 65),
                  bg="black", fg="white")
game_name.place(relx = 0.5, rely = 0.08, anchor="center")

# Create a progress bar and place it right below the title. Style it to
# the desired preference.
progressBarStyle = ttk.Style()
progressBarStyle.theme_use("classic")
progressBarStyle.configure("lawngreen.Horizontal.TProgressbar",
                           background = "lawngreen")
progressBar = Progressbar(game, length = 300,
                          style="lawngreen.Horizontal.TProgressbar")
progressBar.place(relx = 0.5, rely = 0.2, anchor = "center")
progressBar["value"] = 20

# Add question marks as a temporary replacement for the numbers and operators.
randomNum1 = Label(game, text="?", font=("Levitation-7BnPB", 65),
                   bg="black", fg="white")
randomNum1.place(relx = 0.1, rely = 0.4)
randomOperator = Label(game, text="?", font=("QuartzoBold-W9lv", 65),
                   bg="black", fg="white")
randomOperator.place(relx = 0.28, rely = 0.4)
randomNum2 = Label(game, text="?", font=("Levitation-7BnPB", 65),
                   bg="black", fg="white")
randomNum2.place(relx = 0.46, rely = 0.4)
equalSign = Label(game, text="=", font=("QuartzoBold-W9lv", 75),
                   bg="black", fg="white")
equalSign.place(relx = 0.60, rely = 0.39)

# Add an Textbox for the user to enter their answer.
userAnswer = Entry(game, width=3, font=("Arial Bold", 55))
userAnswer.place(relx = 0.76, rely = 0.47, anchor="center")

# Add a button to give the user the option to start the game. Make this
# an image for visual preference.
startButton = PhotoImage(file="StartButton.png")
resizedStartButton = startButton.subsample(5, 5)
click_to_start = Button(game, image=resizedStartButton)
click_to_start.place(relx = 0.5, rely = 0.3, anchor = "center")

# Add a button to give the user the option to enter their answer after filling
# in the Textbox. Make this an image for visual preference.
enterButton = PhotoImage(file="EnterButton.png")
resizedEnterButton = enterButton.subsample(7, 6)
click_to_enter = Button(game, image=resizedEnterButton)
click_to_enter.place(relx = 0.88, rely = 0.47, anchor = "center")

# Add a button to give the user the option to reset their progress. Make this
# an image for visual preference.
resetButton = PhotoImage(file="ResetButton.png")
resizedResetButton = resetButton.subsample(5, 5)
click_to_reset = Button(game, image=resizedResetButton)
click_to_reset.place(relx = 0.9, rely = 0.2, anchor = "center")

# Add a button to give the user the option to go back to the Options tab.
# Make this an image for visual preference.
backButton = PhotoImage(file="BackButton.png")
resizedBackButton = backButton.subsample(5, 5)
click_to_go_back = Button(game, image=resizedBackButton)
click_to_go_back.place(relx = 0.1, rely = 0.1, anchor = "center")

# Add a button to give the user the option to exit the game. Make this
# an image for visual preference.
exitButton = PhotoImage(file="ExitButton.png")
resizedExitButton = exitButton.subsample(8, 6)
click_to_exit = Button(game, image=resizedExitButton)
click_to_exit.place(relx = 0.9, rely = 0.1, anchor = "center")

# Create labels to represent the count of correct, wrong, and total attempts.
correct_questions = Label(game, text="Correct:   ?",
                          font=("Arial Bold", 25), bg="black", fg="lightgreen")
incorrect_questions = Label(game, text="Incorrect:   ?",
                            font=("Arial Bold", 25), bg="black", fg="red")
total_attempts = Label(game, text="Total Attempts:   ?",
                       font=("Arial Bold", 25), bg="black", fg="white")

# Place these labels on the screen.
correct_questions.place(relx=0.07, rely=0.7, anchor="w")
incorrect_questions.place(relx=0.07, rely=0.78, anchor="w")
total_attempts.place(relx=0.07, rely=0.86, anchor="w")

# Add a temporary label to represent a stopwatch from the starting of the game
# to the end.
stopwatch = Label(game, text="0:00:00", font=("digital-7", 60),
                  bg="black", fg="white")
stopwatch.place(relx = 0.5, rely = 0.7, anchor="center")


# Place the tab location.
tab_control.pack(expand=1, fill="both")

# Call the endless loop.
mainScreen.mainloop()

