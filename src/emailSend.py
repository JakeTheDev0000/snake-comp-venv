import configMgr
def sendEmail(score, beat_high_score, difficulty, speed_snake, snake_pos, food_pos, food_spawn, direction, change_to):
    from mailer import Mailer

    if beat_high_score == True:
        subject = "New High Score! " + 'Score: ' + str(score) + ' - ' + str(configMgr.getUsername())
    else:
        subject = "Game Over! " + '-----  Score: ' + str(score) + ' - ' + str(configMgr.getUsername())
    # subject = 'Score - ' + str(score) + ' - ' + str(username)
    body = """
    Score: """ + str(score) + """
    Difficulty: """ + str(difficulty) + """
    Speed: """ + str(speed_snake) + """
    Snake Position: """ + str(snake_pos) + """
    Food Position: """ + str(food_pos) + """
    Food Spawn: """ + str(food_spawn) + """
    Direction: """ + str(direction) + """
    Change To: """ + str(change_to) + """

    Username: """ + str(configMgr.getUsername()) + """
    Snake Name: """ + str(configMgr.getSnakeName()) + """

    """

    mail = Mailer(email=configMgr.getEmail(), password=configMgr.getEmailPass())
    mail.send(receiver=configMgr.getEmail(), subject=subject, message=body)



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