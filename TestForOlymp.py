import pyautogui
import time


time.sleep(10)
i = 0
while True:
    pic_balance = pyautogui.screenshot(region=(998, 116, 1122-998, 171-116))
    pic_screen = pyautogui.screenshot()
    r_robo, g_robo, b_robo = pic_screen.getpixel((1120, 250))
    if (r_robo !=  28):
        break
    pic_balance.save(r"C:\Users\Adithiyaa\Downloads\trash\just_now-" + str(i) + ".png")
    i += 1
    time.sleep(60)
