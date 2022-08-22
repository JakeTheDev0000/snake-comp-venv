 
#snakecompetition.messycode@gmail.com
#JakeWillWin321
#xnzlyhckerojwmnk
def sendEmail(score, beat_high_score, difficulty, speed_snake, snake_pos, food_pos, food_spawn, direction, change_to, username):
    from mailer import Mailer

    if beat_high_score == True:
        subject = "New High Score! " + 'Score: ' + str(score) + ' - ' + str(username)
    else:
        subject = "Game Over! " + '-----  Score: ' + str(score) + ' - ' + str(username)
    # subject = 'Score - ' + str(score) + ' - ' + str(username)
    body = 'Score: ' + str(score) + ' Difficulty: ' + str(difficulty) + ' Speed: ' + str(speed_snake) + ' pos1: ' + str(snake_pos[0]) + ' pos2: ' + str(snake_pos[1]) + ' food_pos1: ' + str(food_pos[0]) + ' food_pos2: ' + str(food_pos[1]) + ' food_spawn: ' + str(food_spawn) + ' direction: ' + str(direction) + ' change_to: ' + str(change_to) + ' username: ' + str(username)

    mail = Mailer(email='snakecompetition.messycode@gmail.com', password='xnzlyhckerojwmnk')
    mail.send(receiver='snakecompetition.messycode@gmail.com', subject=subject, message=body)



def ranByUser():
    import time
    print("this is not a script, it is a module")
    print("this module is ran by the user")
    print("this module is not ran by another module")
    print("this module is not imported by another module")
    time.sleep(0.3)
    print("this module is not imported by a script")
    time.sleep(0.3)

    print("this module is not imported by a script")
    time.sleep(0.3)

    print("this module is not imported by a script")
    time.sleep(2)
    print("im sorry.... um... ")
    time.sleep(0.3)
    print("I am not supposed to be running as a program. ")
    time.sleep(0.3)
    print("closeing... run the main program instead")
    print
    pass

if __name__ == "__main__":
    ranByUser()