import turtle as trtl
from ai import Eleven, OpenRouter

# PLEASE USE camelCase

wn = trtl.Screen()
wn.title("trtl Boilerplate")
wn.bgcolor("white")
wn.setup(width=800, height=600)

eleven = Eleven()
openrouter = OpenRouter()

# Create a trtl
presidentTurtle = trtl.Turtle()
branchTurtle = trtl.Turtle()
podiumTurtle = trtl.Turtle()
audienceTurtle = trtl.Turtle()
textTurtle = trtl.Turtle()
t = trtl.Turtle()
t.hideturtle()
t.shape("turtle") 
t.color("blue")
t.speed(3)

branches = [
    "Navy",
    "Army",
    "Marines",
    "Air Force"
    "Space Force",
    "Coast Gaurd"
]

presidents = [
    "Trump", 
    "Biden",
    "Obama",
    "FDR",
    "Kennedy"
]

presidentVoices = {
    "Trump": "J8RK8FPFvXNMlsVUpFQS",
    "Biden": "IrJA5iRyWTr1LUIlT098",
    "Obama": "ycFAmB4o5zN51P40L7PQ",
    "FDR": "ypxAgoE4j8JBMEI5V4rh",
    "Kennedy": "GE7KqtQX40jQnrwgDMKn",
}

def askQuestions():
    global name, favoritePresident, militaryBranch, presidentTurtle, branchTurtle

    name = wn.textinput("Question 1", "What is your name?").capitalize()

    while not name:
        name = wn.textinput("Question 1", "Please enter your name (cannot be empty)").capitalize()

    favoritePresident = wn.textinput(f"Question 2", f"Thanks {name}, who is your favorite president? (Trump, Biden, Obama, FDR, Kennedy)").capitalize()

    while favoritePresident not in presidents:
        favoritePresident = wn.textinput(f"Question 2", f"Please insert a valid president (Trump, Biden, Obama, FDR, Kennedy)").capitalize()
    
    wn.addshape(f"presidents/{favoritePresident}.gif")
    presidentTurtle.shape(f"presidents/{favoritePresident}.gif")

    
    militaryBranch = wn.textinput("Question 3", "What branch of the military did you serve in? (Navy, Army, Marines, Coast Guard, Air Force, Space Force)").capitalize()
    while militaryBranch not in branches:
        militaryBranch = wn.textinput(f"Question 3", f"Please insert a valid branch (Navy, Army, Marines, Coast Guard, Air Force, Space Force)").capitalize()
    
    wn.addshape(f"emblems/{militaryBranch}.gif")
    branchTurtle.shape(f"emblems/{militaryBranch}.gif")

def drawExtra():
    wn.addshape("podium.gif")
    podiumTurtle.shape("podium.gif")

    wn.addshape("audience.gif")
    audienceTurtle.shape("audience.gif")


def genSpeech(name, favoritePresident, militaryBranch):
    makePrompt = f"Make a speech thanking {name}, a U.S. Military veteran who was in the {militaryBranch} branch in the style of {favoritePresident}. Limit your response to 4 sentences."
    line = openrouter.generateVoiceLine(makePrompt)
    
    # Position the text turtle and write the generated line
    textTurtle.penup()
    textTurtle.goto(-350, -200)  # Adjust coordinates as needed for positioning
    textTurtle.color("black")    # Set text color
    textTurtle.write(line, align="left", font=("Arial", 12, "normal"))
    
    speech = eleven.generateSpeech(line, presidentVoices.get(favoritePresident))

askQuestions()
drawExtra()
presidentTurtle.penup()
presidentTurtle.teleport(-250, 150)

audienceTurtle.penup()
audienceTurtle.teleport(200, -100)

podiumTurtle.penup()
podiumTurtle.teleport(-250, 100)

genSpeech(name, favoritePresident, militaryBranch)

# Wait for user to close wn
wn.mainloop()
