import easygui
def version():
    easygui.msgbox("1.0.0 alpha1")
def zen():
    import this
a=easygui.enterbox("Do what?(zen,version):")
if a=="zen":
    zen()
elif a=="version":
    version()
else:
    easygui.msgbox("Sorry,don't have "+a+".")