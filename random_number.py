import random
import easygui
b=random.randint(1,100)
choices=("close","new game")
def something():
    random_number()
def random_number():
    player=int(easygui.enterbox("Enter your number(1~100)"))
    if player==b:
        c=easygui.buttonbox(msg="do what?",title="do what",choices=choices)
        if c=="close":
            pass
        else:
            something()
    elif player>b:
        easygui.msgbox("big!")
        something()
    else:
        easygui.msgbox("small!")
        something()