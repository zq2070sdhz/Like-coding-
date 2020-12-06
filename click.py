import easygui
import zen
import version
import random_number
import about
a=easygui.enterbox("Do what?(zen,version,randomNumber,about):")
if a=="zen":
    zen.zen()
elif a=="version":
    version.version()
elif a=="randomNumber":
    random_number.random_number()
elif a=="about":
    about.about()
else:
    easygui.msgbox("Sorry,don't have "+a+".")