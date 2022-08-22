import PySimpleGUI as sg
import snake
import sys

def main():
    sg.theme('DarkAmber')
       # Add a touch of color
    # All the stuff inside your window.
    layout = [
        [sg.Text("Snake Comtatition", font=("Helvetica", 25))],
        [sg.Button("Start Game", font=("Helvetica", 20))],
      ]

    # Create the Window
    window = sg.Window('Window Title', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            sys.exit()
            break

        if event == 'Start Game':
            window.close()
            snake.snakePlay()
            break

    window.close()

    pass

if __name__ == "__main__":
    main()