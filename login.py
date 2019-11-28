from guizero import *
import os

app = App(grid=True)

pinText  = Text(grid=[0,0], text="PIN: ")
pinInput = TextBox(grid=[1,0])
