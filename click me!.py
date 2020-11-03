import easygui
import zen
import version
import random_number
a=easygui.enterbox("Do what?(zen,version,randomNumber):")
if a=="zen":
    zen.zen()
elif a=="version":
    version.version()
elif a=="randomNumber":
    random_number.random_number()
else:
    easygui.msgbox("Sorry,don't have "+a+".")