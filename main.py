import pyautogui

screenWidth, screenHeight = pyautogui.size()

windows = pyautogui.getAllWindows()

print("Choose a window to center:")
for i, window in enumerate(windows):
    print(f"[{i + 1}] - {window.title}")

choice = int(input("Enter the number of the window to center: "))

window = windows[choice - 1]

windowWidth, windowHeight = window.size
windowX, windowY = window.topleft

newX = int((screenWidth / 2) - (windowWidth / 2))
newY = int((screenHeight / 2) - (windowHeight / 2))

window.moveTo(newX, newY)
