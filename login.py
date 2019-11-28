from guizero import *
import os

app = App(layout="grid", bg="white")

def login():
    if password == pinInput.value_text:
        pinError.fg = "green"
        pinError.value_text = "logging in..."
    elif pinInput.value_text == "":
        pinError.fg = "red"
    elif pinInput.value_text != password:
        pinError.fg = "red"
        pinError.value_text = "password is incorrect!!!"

pinText     = Text(app, grid=[0,0], text="PIN: ")
pinInput    = TextBox(app, grid=[1,0])
pinError    = Text(app, grid=[0,1], text="You must enter \n a PIN to login")
pinError.fg = "white"
pinError.bg = "white"
PinEnter    = PushButton(app, text="LOGIN", command=login())



app.display()
