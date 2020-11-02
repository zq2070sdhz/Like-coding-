import easygui
import zen
import version
a=easygui.enterbox("Do what?(zen,version):")
if a=="zen":
    zen.zen()
elif a=="version":
    version.version()
else:
    easygui.msgbox("Sorry,don't have "+a+".")