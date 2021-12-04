def getBounds():
    import keyboard
    import pyautogui as pg
    import os

    print('Move cursor to top left of capture area and press escape.')
    keyboard.wait('esc')
    topLeftX, topLeftY = pg.position()
    print('Top left bound captured as',topLeftX,topLeftY,'\n\nMove cursor to bottom right of capture area and press escape.')


    keyboard.wait('esc')
    bottomRightX, bottomRightY = pg.position()
    print('Bottom right bound captured as',bottomRightX,bottomRightY,'\n')

    coordinateArray = [topLeftX, topLeftY, bottomRightX, bottomRightY]


    outfileConfirmation = input('\nWould you like to save these coordinates to an outfile? Please enter 1 for yes and 0 for no.\n')
    if outfileConfirmation == '1':
        outfileName = input('\nA text file will be saved in the current directory, please enter the desired name.\n')
        cwd = os.getcwd()
        filePath = cwd + "\\" + outfileName + ".txt"
        outFile = open(filePath, 'w')
        outFile.write(str(coordinateArray))


    elif outfileConfirmation == '0':
        print("Coordinated will not be saved.")

    else:
        print('Response not understood, file will not be saved.')

    return coordinateArray
