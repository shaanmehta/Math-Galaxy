# Name: Shaan Mehta
# Description: This is the Math Galaxy! This GUI-based math game has been
#              designed to help younger students practice the fundamentals of
#              math in an enjoyable way. By using interactive flashcards with
#              random numbers and operators, students can strengthen their math
#              skills while having fun. The game begins with a homepage that
#              welcomes the user and prompts them to view their options. Then,
#              the user is presented with various options for customization.
#              These options include choosing the level of difficulty, selecting
#              specific operators to focus on, the option to include negative
#              numbers, and determining the number of questions to be asked.
#              Once the user has filled in all of the options, they are directed 
#              to the game. Within the game, there are a number of features to 
#              enhance user interface. These include intuitive buttons such as 
#              "Back," "Start," "Enter," "Reset," and "Quit," ensuring smooth 
#              navigation throughout the game. As the user progresses, the count 
#              of correct, wrong, and total attempts are displayed. To keep students 
#              motivated and encourage better results, a progress bar and stopwatch 
#              are shown as well. The Math Galaxy provides a comprehensive platform 
#              for users to practice their skills and become a math whiz!


# <-------------------------------Import Library------------------------------->

import random
import time
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Checkbutton
from tkinter.ttk import Progressbar
from tkinter import *

# <----------------------------Custom Functions-------------------------------->


# Move from the first tab to the second tab when the button is clicked.
def move_to_second_tab():
    tab_control.select(1)
    
# Move from the second tab to the third tab when the button is clicked.
def move_to_third_tab():
    
    # Display an error message if no operators are selected.
    if ((addition_state.get()==False) and (subtraction_state.get()==False) and
        (multiplication_state.get()==False) and (division_state.get()==False)):
        messagebox.showerror("", "Please select an operator(s)")
            
    # Display a message to tell the user to confirm their selections.
    else:
        optionConfirmation = messagebox.askyesno("",
                                            "Are you sure with your options?")
        
        # Stay on the second tab if the user is not sure with their options.
        if (optionConfirmation == False):
            tab_control.select(1)
            
        # Continue to the next tab.
        else:
            tab_control.select(2)
            
            # Reset everything. 
            reset()
            
# Reset all values as to how they were before the game was started.
def reset():
    global correct_count, wrong_count, total_questions, stopwatch_running
    correct_count = 0
    wrong_count = 0
    total_questions = 0
    click_to_enter.configure(state="disabled")
    click_to_start.configure(state="normal")
    randomOperator.configure(text="?")
    randomNum1.configure(text="?")
    randomNum2.configure(text="?")
    correct_questions.configure(text="Correct:   0")
    wrong_questions.configure(text="Wrong:   0")
    total_attempts.configure(text="Total Attempts:   0")
    progressBar["value"] = 0
    stopwatch_running = False
    stopwatch.configure(text="00:00:000")
    update_stopwatch()
    
# Generate the math problem based on what the options were. 
def generate_math_problem():
    global operator
    operator = []
    
    # Append the operators to an empty list if they were selected during the
    # options screen.
    if (addition_state.get() == True):
        operator.append("+")
    if (subtraction_state.get() == True):
        operator.append("−")
    if (multiplication_state.get() == True):
        operator.append("×")
    if (division_state.get() == True):
        operator.append("÷")
        
    # Generate a random operator when the start button is clicked.
    randomOp = random.choice(operator)
    
    # Replace the question mark with a random operator.
    randomOperator.configure(text=randomOp)
    
    # Generate appropriate numbers for division.
    if (randomOp == "÷"):
        num1 = random.randint(1, 3 * int(choose_level.get()))
        num2 = random.randint(1, 3 * int(choose_level.get()))
        
        # Change numbers to negative if the option was selected.
        if (choose_negative.get() == 1):
            randomNegative1 = random.choice([-1, 1])
            num1 *= randomNegative1
            randomNegative2 = random.choice([-1, 1])
            num2 *= randomNegative2
            
        # Create the real num1 by doing reverse multiplication. 
        dividend = num1 * num2
        
        # Change the initial question mark for randomNum1 and randomNum2
        randomNum1.configure(text=dividend)
        randomNum2.configure(text=num1)
        
    # Generate appropriate numbers for all other operators.
    else:
        num1 = random.randint(1, 3 * int(choose_level.get()))
        num2 = random.randint(1, 3 * int(choose_level.get()))
        
        # Change numbers to negative if the option was selected.
        if (choose_negative.get() == 1):
            randomNegative1 = random.choice([-1, 1])
            num1 *= randomNegative1
            randomNegative2 = random.choice([-1, 1])
            num2 *= randomNegative2
        
        # Change the initial question mark for randomNum1 and randomNum2
        randomNum1.configure(text=num1)
        randomNum2.configure(text=num2)
        
# Function to update the time on the stopwatch.
def update_stopwatch():
    global start_time, final_time_display
    
    if (stopwatch_running == True): # The game has started.
        
        # Calculate the time it takes from the start of the game to the end.
        final_time = time.time() - start_time
        
        # Convert this time into milliseconds.
        milliseconds = int(1000 * final_time)
        
        # Convert milliseconds into seconds.
        seconds = (milliseconds % 60000) // 1000
        
        # Convert minutes into seconds.
        minutes = milliseconds // 60000
        
        # Make it so that this time is displayed in "MM:SS:MMM"
        final_time_display = str(minutes) + ":" + str(seconds) + ":" + str(milliseconds)
        
        # Update the stopwatch label with the final time variable.
        stopwatch.configure(text=final_time_display)
        
        # Stop the stopwatch if the user has completed all of the questions.
        if (total_questions == int(num_of_questions.get())):
            return # Return the stopwatch so that it stops.

        # Update the stopwatch every 10 milliseconds
        mainScreen.after(10, update_stopwatch) 

def stopwatch_started():
    global start_time, stopwatch_running
    start_time = time.time() # Start time has been defined.
    stopwatch_running = True # Stopwatch will start.
    update_stopwatch() # Update the stopwatch.
        
# Update the count of correct answers.
def num_correct():
    global correct_count
    correct_count += 1
    correct_questions.configure(text="Correct:   " + str(correct_count))
    
# Update the count of wrong answers.
def num_wrong():
    global wrong_count
    wrong_count += 1
    wrong_questions.configure(text="Wrong:   " + str(wrong_count))
        
# Update the count of total attempts.
def num_attempts():
    global total_questions
    total_questions += 1
    total_attempts.configure(text="Total Attempts:   " + str(total_questions))
        
# Check to see if the user's answer is correct or wrong.
def check_answer():
    global total_questions
    
    # Check to see if user input is valid.
    try:
        answer = int(userAnswer.get())
    except ValueError:
        # Display an error message.
        messagebox.showerror("", "Please enter an appropriate answer.")
        # Clear the answer entry widget
        userAnswer.delete(0, "end")
        return
    
    # Get the math problem.
    num1 = int(randomNum1["text"])
    num2 = int(randomNum2["text"])
    operator = randomOperator["text"]      
    
    # Check to see if the answer is correct.
    if (operator == "+"):
        correct_ans = num1 + num2
    elif (operator == "−"):
        correct_ans = num1 - num2
    elif (operator == "×"):
        correct_ans = num1 * num2
    else:
        correct_ans = num1 // num2
        
    # Update the count of correct questions.
    if (answer == correct_ans):
        num_correct()
        
    # Update the count of wrong questions.
    else:
        num_wrong()
    
    # Clear the answer entry.
    userAnswer.delete(0, "end")
    
    # Update the count of total attempts.
    num_attempts()
    
    # Increase the increment on the progress bar.
    increase_progress_bar()
    
    # Keep generating a math problem until the user has answered all questions.
    if (total_questions == int(num_of_questions.get())):
        mainScreen.after(100, game_ended_message)
    else:
        generate_math_problem()
    
# Give the user one final message after they have completed the game. 
def game_ended_message():
    global total_questions
    total_questions += 1
    num_attempts()
    
    # Display a yes/no message box to ask the user if they want to play again.
    # Before doing this, tell them how they did during the game.
    end_of_game = messagebox.askyesno("", "Great Job! You completed " +
                            str(num_of_questions.get()) + " questions. Your \
final time was " + str(final_time_display) + "! \n Would you like to play again?")
    
    # If the user selects yes, go back to the instructions tab.
    if (end_of_game == True):
        move_to_second_tab()
    else:
        mainScreen.destroy()
        
    
def enter_key_clicked(enter_key):
    
    # Check if a question has been generated.
    operator = randomOperator["text"]
    
    # Only allow the enter key to work if there is a math problem generated.
    if (operator != "?"):
        check_answer()
    else:
        pass
        
# Increase the progress on the progress bar by consistent increments.
def increase_progress_bar():
    increment = 100 / int(num_of_questions.get())
    progressBar["value"] += increment
        
# When the start button is clicked, a math problem will be generated. After
# the first click, the start button will be disabled and the enter button will
# be enabled.
def start_button():
    click_to_start.configure(state="disabled") # Disable the Start button.
    click_to_enter.configure(state="normal") # Enable the Enter button.
    generate_math_problem()
    
    # Move the cursor to the entry box.
    userAnswer.focus()
    
    # Start the stopwatch.
    stopwatch_started()
    
# Go back to the Options tab when the back button is clicked. Display a
# warning message to confirm losing all progress.
def back_button():
    backConfirmation = messagebox.askyesno("",
                                            "Are you sure you want to go back? \
    \n You will lose all of your progress!")
    
    # Stay on the third tab if the user selects "No".
    if (backConfirmation == False):
        tab_control.select(2)
        
    # Otherwise, go back to the second tab.
    else:
        tab_control.select(1)

def exit_button():
    exitConfirmation = messagebox.askokcancel("", "Are you sure you want to \
exit? \n This will close the game.")
    
    # Stay on the third tab if the user selects "Cancel".
    if (exitConfirmation == False):
        tab_control.select(2)
        
    # Otherwise, exit the game.
    else:
        mainScreen.destroy()
    
# <-----------------------------Initialization--------------------------------->

# Create the window.
mainScreen = Tk()
mainScreen.title("Shaan's Math Galaxy")
mainScreen.geometry("1024x768")
tab_control = ttk.Notebook(mainScreen)

# Variables used in functions
stopwatch_running = False 
operator = []
correct_count = 0
wrong_count = 0
total_questions = 0

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
click_to_options = Button(home, image = resizedoptions,
                          command=move_to_second_tab)
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

# Set check states for all operators. Make all operators except division have a
# check button prior to any user adjustment.
addition_state = BooleanVar()
addition_state.set(True)
subtraction_state = BooleanVar()
subtraction_state.set(True) 
multiplication_state = BooleanVar()
multiplication_state.set(True)
division_state = BooleanVar()
division_state.set(False)

# Create a check button for each operator. 
addition_checkbox = Checkbutton (operators_frame, text = "Addition",
bg="black", fg="white", selectcolor="black", variable=addition_state)
subtraction_checkbox = Checkbutton (operators_frame, text = "Subtraction",
bg="black", fg="white", selectcolor="black", variable=subtraction_state)
multiplication_checkbox = Checkbutton (operators_frame, text = "Multiplication",
bg="black", fg="white", selectcolor="black", variable=multiplication_state)
division_checkbox = Checkbutton (operators_frame, text = "Division",
bg="black", fg="white", selectcolor="black", variable=division_state)

# Organize the choices inside the frame.
addition_checkbox.pack(anchor = W)
subtraction_checkbox.pack(anchor = W)
multiplication_checkbox.pack(anchor = W)
division_checkbox.pack(anchor = W)

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
                                 value=0, variable=choose_negative)

# Set the default option to "No".
choose_negative.set(0)

# Place the choices inside the frame.
negative_option_yes.pack(anchor = W)
negative_option_no.pack(anchor = W)

# Create a Spinbox to allow the user to choose the number of questions to have.
# Set the range of questions and place it on the screen.
choose_num_of_questions = IntVar()

num_of_questions = Spinbox(options, from_ = 10, to = 25, state="readonly",
                           font=("OpenSans", 15),
                           background="white", fg="black")
num_of_questions.place(relx=0.58, rely=0.65, anchor="center",
                       width=50, height=50)

# Set the default number of questions to the minimum (10).
choose_num_of_questions.set(10)

# Add a label for it.
questions = Label(options, text="Number of Questions:",
                  font=("OpenSans-Bold", 15), bg="black", fg="white")
questions.place(relx=0.42, rely = 0.65, anchor="center")

# Add a "Ready To Play" button for the user as a way for the user to confirm
# their selections. Make this an image for visual preference.
ReadyToPlay = PhotoImage(file="ReadyToPlay.png")
resizedReadyToPlay = ReadyToPlay.subsample(4, 4)
click_to_play = Button(options, image = resizedReadyToPlay,
                       command=move_to_third_tab)
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
progressBarStyle.configure("navyblue.Horizontal.TProgressbar",
                           background = "navyblue")
progressBar = Progressbar(game, length = 300,
                          style="navyblue.Horizontal.TProgressbar")
progressBar.place(relx = 0.5, rely = 0.2, anchor = "center")
progressBar["value"] = 0

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

# Add a Textbox for the user to enter their answer.
userAnswer = Entry(game, width=3, font=("Arial Bold", 55))
userAnswer.place(relx = 0.76, rely = 0.47, anchor="center")

# Add a button to give the user the option to start the game. Make this
# an image for visual preference.
startButton = PhotoImage(file="StartButton.png")
resizedStartButton = startButton.subsample(5, 5)
click_to_start = Button(game, image=resizedStartButton, command=start_button)
click_to_start.place(relx = 0.5, rely = 0.3, anchor = "center")

# Add a button to give the user the option to enter their answer after filling
# in the Textbox. Make this an image for visual preference.
enterButton = PhotoImage(file="EnterButton.png")
resizedEnterButton = enterButton.subsample(7, 6)
click_to_enter = Button(game, image=resizedEnterButton,
                        command=check_answer)
click_to_enter.place(relx = 0.88, rely = 0.47, anchor = "center")

# Allow the return key to be used for the user to enter their answer.
enter_key = mainScreen.bind("<Return>", enter_key_clicked)

# Add a button to give the user the option to reset their progress. Make this
# an image for visual preference.
resetButton = PhotoImage(file="ResetButton.png")
resizedResetButton = resetButton.subsample(5, 5)
click_to_reset = Button(game, image=resizedResetButton, command=reset)
click_to_reset.place(relx = 0.9, rely = 0.2, anchor = "center")

# Add a button to give the user the option to go back to the Options tab.
# Make this an image for visual preference.
backButton = PhotoImage(file="BackButton.png")
resizedBackButton = backButton.subsample(5, 5)
click_to_go_back = Button(game, image=resizedBackButton, command=back_button)
click_to_go_back.place(relx = 0.1, rely = 0.1, anchor = "center")

# Add a button to give the user the option to exit the game. Make this
# an image for visual preference.
exitButton = PhotoImage(file="ExitButton.png")
resizedExitButton = exitButton.subsample(8, 6)
click_to_exit = Button(game, image=resizedExitButton, command=exit_button)
click_to_exit.place(relx = 0.9, rely = 0.1, anchor = "center")

# Create labels to represent the count of correct, wrong, and total attempts.
# Initialize them to 0.
correct_questions = Label(game, text="Correct:   0",
                          font=("Arial Bold", 25), bg="black", fg="lightgreen")
wrong_questions = Label(game, text="Wrong:   0",
                            font=("Arial Bold", 25), bg="black", fg="red")
total_attempts = Label(game, text="Total Attempts:   0",
                       font=("Arial Bold", 25), bg="black", fg="white")

# Place these labels on the screen.
correct_questions.place(relx=0.07, rely=0.7, anchor="w")
wrong_questions.place(relx=0.07, rely=0.78, anchor="w")
total_attempts.place(relx=0.07, rely=0.86, anchor="w")

# Add a temporary label to represent a stopwatch from the starting of the game
# to the end.
stopwatch = Label(game, text="00:00:000", font=("digital-7", 60),
                  bg="black", fg="white")
stopwatch.place(relx = 0.5, rely = 0.7, anchor="center")

# Place the tab location.
tab_control.pack(expand=1, fill="both")

# Call the endless loop.
mainScreen.mainloop()


