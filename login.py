#logging into the OS

import PySimpleGUI as sg
import os

layout = [
    [sg.Text("PIN ID:"), sg.InputText()],
    [sg.Text("PASSWORD:"), sg.InputText()],
    [sg.Button("USERS LOGIN"), sg.Button("GUEST LOGIN")]
]

sg.Window("Login to brickOS").Layout(layout)
