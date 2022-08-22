import PySimpleGUI as sg
import snake
import sys
import configMgr

def main():
    sg.theme('DarkAmber')
       # Add a touch of color
    # All the stuff inside your window.
    configListCol = sg.Column([
        [sg.Text('Username', size=(15, 1)), sg.InputText(configMgr.getUsername(), key='username')],
        [sg.Text('Snake Name', size=(15, 1)), sg.InputText(configMgr.getSnakeName(), key='snakeName')],
        [sg.Text('Make sure the email address and password are correct, we dont check for that', font=('Helvetica', 8))],

        [sg.Text('Email', size=(15, 1)), sg.InputText(configMgr.getEmail(), key='email', password_char='*')],
        [sg.Text('Email Password', size=(15, 1)), sg.InputText(configMgr.getEmailPass(), key='emailPass', password_char='*')],
        [sg.Text('Frame Size X and Frame Size Y is the resolution ie. 1920 by 1080', font=('Helvetica', 8))],
        
        [sg.Text('Frame Size X', size=(15, 1)), sg.InputText(configMgr.get_frame_size_x(), key='frame_size_x')],
        [sg.Text('Frame Size Y', size=(15, 1)), sg.InputText(configMgr.get_frame_size_y(), key='frame_size_y')],
        [sg.Text('Fullscreen', size=(15, 1)), sg.InputText(configMgr.getFullscreen(), key='fullscreen')],
        [sg.Text('Difficulty is the speed of the snake. DONT TOUCH \'speed snake\' you could break the game', font=('Helvetica', 8))],

        [sg.Text('Difficulty', size=(15, 1)), sg.InputText(configMgr.getDifficulty(), key='difficulty')],
        [sg.Text('Speed Snake', size=(15, 1)), sg.InputText(configMgr.getSpeedSnake(), key='speedSnake')],
    ])

    leftLayout = sg.Column([ 
        [sg.Button("Start Game",size=(15,1), font=("Helvetica", 20))],
        [sg.Button("Start Game loop",size=(15,1), font=("Helvetica", 15), tooltip="Starts the game in a loop, so you can play multiple times without restarting the program, press ESC to exit the loop")],
        [sg.Button("Start Practice",size=(15,1), font=("Helvetica", 15), tooltip="Starts the game in practice mode, you can play as long as you want and wont send emails, press ESC to exit the loop")],

    ])

    layout = [
        [sg.Text("Snake Competition", font=("Helvetica", 25))],
        [leftLayout, configListCol],
      ]

    # Create the Window
    window = sg.Window('EJR', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            sys.exit()
            break

        if event == 'Start Game':
            window.close()
            configMgr.saveConfig(values['username'], values['email'], values['emailPass'], values['frame_size_x'], values['frame_size_y'], values['fullscreen'], values['difficulty'], values['speedSnake'], values['snakeName'])
            snake.snakePlay()
            break

        if event == 'Start Game loop':
            window.close()
            configMgr.saveConfig(values['username'], values['email'], values['emailPass'], values['frame_size_x'], values['frame_size_y'], values['fullscreen'], values['difficulty'], values['speedSnake'], values['snakeName'])
            while True:
                snake.snakePlay(loop=True)
            break
            
        if event == 'Start Practice':
            window.close()
            configMgr.saveConfig(values['username'], values['email'], values['emailPass'], values['frame_size_x'], values['frame_size_y'], values['fullscreen'], values['difficulty'], values['speedSnake'], values['snakeName'])
            while True:
                snake.snakePlay(loop=True, practice=True)
            break


    window.close()

    pass

if __name__ == "__main__":
    main()