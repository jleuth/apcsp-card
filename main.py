import turtle as trtl

wn = trtl.Screen()
wn.title("trtl Boilerplate")
wn.bgcolor("white")
wn.setup(width=800, height=600)

# Create a trtl
t = trtl.Turtle()
t.shape("turtle") 
t.color("blue")
t.speed(3)


# Wait for user to close wn
wn.mainloop()
