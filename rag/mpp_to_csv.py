import pyautogui
import time

# Open Microsoft Project
pyautogui.hotkey('win', 'r')
pyautogui.write('winproj')
pyautogui.press('enter')

# Wait for Microsoft Project to open
time.sleep(5)

# Open the .mpp file
pyautogui.hotkey('ctrl', 'o')
# replace with the actual path to your .mpp file
pyautogui.write('C:\\path\\to\\your\\file.mpp')
pyautogui.press('enter')

# Wait for the file to open
time.sleep(5)

# Save as .csv
pyautogui.hotkey('f12')
# replace with the actual path where you want to save the .csv file
pyautogui.write('C:\\path\\to\\your\\file.csv')
pyautogui.press('tab', presses=2)
pyautogui.press('c')
pyautogui.press('enter')

# Wait for the file to save
time.sleep(5)

# Close Microsoft Project
pyautogui.hotkey('alt', 'f4')
