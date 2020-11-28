# CTRL SHIFT R 
import pyautogui
import time

def Home():
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  ")
    print("*" + "                              TAP TAP CLICKER                                        *")
    print("*" + "                                                                                     *")
    print("*" + "                                                                                     *")
    print("*" + "            1. PLAY THE GAME (WHEN YOUR IN THE GAME)                                 *")
    print("*" + "            2. BEGIN WITH THE FIRST STEP                                             *")
    print("*" + "            3. CHECK POSITION OF MOUSE                                               *")
    print("*" + "                                                                                     *")
    print("*" + "                                                                                     *")
    print("*" + "                                                                                     *")
    print("*" + "                             Made by: mmb it developer                               *")
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  ")    

count = 0

Home()
answer = input("Choose number: ")

if answer == "1":
    time.sleep(3)
    while count <= 1:
        for num in range(600):
            pyautogui.click(953, 443)
            num = num + 1
            print(num)
        pyautogui.click(768, 978)
        time.sleep(1)
        pyautogui.click(1121, 775)
        pyautogui.click(1157, 636)
elif answer == "2":
    # Click on Google Chrome (166, 1067)
    pyautogui.click(166, 1067)
    time.sleep(2)
    pyautogui.click(314, 52)

    # Search to Facebook games
    pyautogui.typewrite("https://www.facebook.com/games/instantgames")
    pyautogui.typewrite(["enter"])
    time.sleep(2)

    # Click on Facebook game genre (537, 850)
    pyautogui.click(531, 369)
    time.sleep(4)

    # Click on Tap Tap start button
    pyautogui.click(951, 817)
    time.sleep(3)

    while count <= 1:
        pyautogui.click(953, 443)
else:
    print(pyautogui.position())
