def getUsername():
    file = open("src\config.txt", "r")
    lines = file.readlines()
    file.close()
    username = lines[1].split(":")[1].strip()
    return username

def getEmail():
    file = open("src\config.txt", "r")
    lines = file.readlines()
    file.close()
    email = lines[2].split(":")[1].strip()
    return email

def getEmailPass():
    file = open("src\config.txt", "r")
    lines = file.readlines()
    file.close()
    PassWord = lines[3].split(":")[1].strip()
    return PassWord

def get_frame_size_x():
    file = open("src\config.txt", "r")
    lines = file.readlines()
    file.close()
    frame_size_x = lines[4].split(":")[1].strip()
    return frame_size_x

def get_frame_size_y():
    file = open("src\config.txt", "r")
    lines = file.readlines()
    file.close()
    frame_size_y = lines[5].split(":")[1].strip()
    return frame_size_y

def getFullscreen():
    file = open("src\config.txt", "r")
    lines = file.readlines()
    file.close()
    fullscreen = lines[6].split(":")[1].strip()
    return fullscreen

def getDifficulty():
    file = open("src\config.txt", "r")
    lines = file.readlines()
    file.close()
    difficulty = lines[7].split(":")[1].strip()
    return difficulty

def getSpeedSnake():
    file = open("src\config.txt", "r")
    lines = file.readlines()
    file.close()
    speedSnake = lines[8].split(":")[1].strip()
    return speedSnake

def getSnakeName():
    file = open("src\config.txt", "r")
    lines = file.readlines()
    file.close()
    snakeName = lines[9].split(":")[1].strip()
    return snakeName

def saveConfig(username, email, emailPass, frame_size_x, frame_size_y, fullscreen, difficulty, speedSnake, snakeName):
    file = open("src\config.txt", "w")
    file.write("")
    file.close()

    file = open("src\config.txt", "a")
    file.write("no spaces after the colon (:)\n")
    file.write("username:" + username + "\n")
    file.write("email:" + email + "\n")
    file.write("emailPass:" + emailPass + "\n")
    file.write("frame_size_x:" + frame_size_x + "\n")
    file.write("frame_size_y:" + frame_size_y + "\n")
    file.write("fullscreen:" + fullscreen + "\n")
    file.write("difficulty:" + difficulty + "\n")
    file.write("speedSnake:" + speedSnake + "\n")
    file.write("snakeName:" + snakeName + "\n")
    file.close()