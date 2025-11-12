import turtle as trtl
#from ai import Eleven, OpenRouter

# PLEASE USE camelCase

wn = trtl.Screen()
wn.title("trtl Boilerplate")
wn.bgcolor("white")
wn.setup(width=800, height=600)

#eleven = Eleven()
#openrouter = OpenRouter()

# Create a trtl
presidentTurtle = trtl.Turtle()
presidentTurtle.hideturtle()
branchTurtle = trtl.Turtle()
branchTurtle.hideturtle()
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
    "Trump":"somthing Trump",
    "Biden":"somthing Biden",
    "Obama":"somthing Obama",
    "FDR":"somthing FDR",
    "Kennedy":"somthing Kennedy",
}

def askQuestions():
    global name, favoritePresident, militaryBranch, presidentTurtle, branchTurtle

    name = wn.textinput("Question 1", "What is your name?").capitalize()

    favoritePresident = wn.textinput(f"Question 2", f"Thanks {name}, who is your favorite president? (Trump, Biden, Obama, FDR, Kennedy)").capitalize()

    while favoritePresident not in presidents:
        favoritePresident = wn.textinput(f"Question 2", f"Please insert a valid president (Trump, Biden, Obama, FDR, Kennedy)").capitalize()
    
    wn.addshape(f"presidents/{favoritePresident}.gif")
    presidentTurtle.shape(f"presidents/{favoritePresident}.gif")
    
    militaryBranch = wn.textinput("Question 3", "What branch of the military did you serve in? (Navy, Army, Marines, Coast Guard, Air Force, Space Force)").capitalize()
    while militaryBranch not in branches:
        militaryBranch = wn.textinput(f"Question 3", f"Please insert a valid branch (Navy, Army, Marines, Coast Guard, Air Force, Space Force)").capitalize()
    
    #branchTurtle.addshape("")
    branchTurtle.shape(f"emblems/{militaryBranch}.gif")

def genSpeech(name, favoritePresident, militaryBranch):
    makePrompt = f"Make a speech thanking {name}, a U.S. Military veteran who was in the {militaryBranch} branch in the style of {favoritePresident}. Limit your response to 1 paragraph"
    #line = openrouter.generatevoiceLine(makePrompt)
    #speech = eleven.generateSpeech(line, presidentVoices.get(favoritePresident))

askQuestions()

# Wait for user to close wn
wn.mainloop()
