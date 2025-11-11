import turtle as trtl
# PLEASE USE camelCase
wn = trtl.Screen()
wn.title("trtl Boilerplate")
wn.bgcolor("white")
wn.setup(width=800, height=600)

# Create a trtl
t = trtl.Turtle()
t.hideturtle()
t.shape("turtle") 
t.color("blue")
t.speed(3)

def askQuestions():
    global name, favoritePresident, militaryBranch
    
    name = wn.textinput("Question 1", "What is your name?")
    favoritePresident = wn.textinput(f"Question 2", f"Thanks {name}, who is your favorite president?")
    militaryBranch = wn.textinput("Question 3", "What branch of the military did you serve in?")


# Wait for user to close wn
wn.mainloop()
