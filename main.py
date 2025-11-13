import turtle as trtl
from ai import Eleven, OpenRouter

wn = trtl.Screen()
wn.title("trtl Boilerplate")
wn.bgcolor("#1a2332")
wn.setup(width=800, height=600)

eleven = Eleven()
openrouter = OpenRouter()

presidentTurtle = trtl.Turtle()
branchTurtle = trtl.Turtle()
podiumTurtle = trtl.Turtle()
audienceTurtle = trtl.Turtle()
textTurtle = trtl.Turtle()
decorTurtle = trtl.Turtle()
textTurtle.hideturtle()

branches = [
    "Navy",
    "Army",
    "Marines",
    "Air Force",
    "Space Force",
    "Coast Guard"
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

def drawStars():
    """Corner stars for minimal flair"""
    decorTurtle.hideturtle()
    decorTurtle.speed(0)
    decorTurtle.color("#ffffff")
    
    star_positions = [(-350, 250), (350, 250), (-350, -250), (350, -250)]
    
    for pos in star_positions:
        decorTurtle.penup()
        decorTurtle.goto(pos)
        decorTurtle.pendown()
        decorTurtle.begin_fill()
        for _ in range(5):
            decorTurtle.forward(15)
            decorTurtle.right(144)
        decorTurtle.end_fill()

def askQuestions():
    global name, favoritePresident, militaryBranch, presidentTurtle, branchTurtle

    name = wn.textinput("Question 1", "What is your name?").capitalize()

    while not name:
        name = wn.textinput("Question 1", "Please enter your name (cannot be empty)").capitalize()

    favoritePresident = wn.textinput(f"Question 2", f"Thanks {name}, who is your favorite president? (Trump, Biden, Obama, FDR, Kennedy)").capitalize()
    print(favoritePresident)
    if favoritePresident.lower() == "fdr":
        favoritePresident = favoritePresident.upper()

    print(favoritePresident)

    while favoritePresident not in presidents:
        favoritePresident = wn.textinput(f"Question 2", f"Please insert a valid president (Trump, Biden, Obama, FDR, Kennedy)").capitalize()
    
    wn.addshape(f"presidents/{favoritePresident}.gif")
    presidentTurtle.shape(f"presidents/{favoritePresident}.gif")

    militaryBranch = wn.textinput("Question 3", "What branch of the military did you serve in? (Navy, Army, Marines, Coast Guard, Air Force, Space Force)").title()
    
    while militaryBranch not in branches:
        militaryBranch = wn.textinput(f"Question 3", f"Please insert a valid branch (Navy, Army, Marines, Coast Guard, Air Force, Space Force)").title()
    
    branch_filename = militaryBranch.lower().replace(" ", "_")
    wn.addshape(f"emblems/{branch_filename}.gif")
    branchTurtle.shape(f"emblems/{branch_filename}.gif")

def drawExtra():
    wn.addshape("podium.gif")
    podiumTurtle.shape("podium.gif")

    wn.addshape("audience.gif")
    audienceTurtle.shape("audience.gif")

def genSpeech(name, favoritePresident, militaryBranch):
    makePrompt = f"Make a super short speech thanking {name}, a U.S. Military veteran who was in the {militaryBranch} branch in the style of {favoritePresident}. Limit your response to 4 sentences and do not include any preamble, just the speech itself."
    line = openrouter.generateVoiceLine(makePrompt)
    eleven.generateSpeech(line, presidentVoices.get(favoritePresident))
    
    textTurtle.speed(0)
    textTurtle.penup()
    textTurtle.goto(-350, -150)
    textTurtle.pendown()
    textTurtle.color("#2a3f5f")
    textTurtle.fillcolor("#f8f9fa")
    textTurtle.begin_fill()
    textTurtle.pensize(2)
    for _ in range(2):
        textTurtle.forward(700)
        textTurtle.right(90)
        textTurtle.forward(130)
        textTurtle.right(90)
    textTurtle.end_fill()
    
    textTurtle.penup()
    textTurtle.goto(0, -180)
    textTurtle.color("#1a1f3a")
    
    max_chars_per_line = 125
    font_size = 12
    line_height = 18
    y_position = -180
    
    words = line.split()
    current_line = ""
    
    for word in words:
        if len(current_line) + len(word) + 1 <= max_chars_per_line:
            current_line += word + " "
        else:
            textTurtle.goto(0, y_position)
            textTurtle.write(current_line.strip(), align="center", font=("Arial", font_size, "normal"))
            y_position -= line_height
            current_line = word + " "
    
    if current_line:
        textTurtle.goto(0, y_position)
        textTurtle.write(current_line.strip(), align="center", font=("Arial", font_size, "normal"))

drawStars()
askQuestions()
drawExtra()

presidentTurtle.penup()
presidentTurtle.teleport(-180, 80)

podiumTurtle.penup()
podiumTurtle.teleport(-180, 20) 

branchTurtle.penup()
branchTurtle.teleport(150, 150) 

audienceTurtle.penup()
audienceTurtle.teleport(150, -50) 

genSpeech(name, favoritePresident, militaryBranch)

wn.mainloop()