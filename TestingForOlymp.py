# import pyautogui
# import time
# import keyboard


# #green color r, g, b = (12, 155, 89)
# #orange color r, g, b = (238, 125, 86)

# y_green_coord = y_orange_coord = False

# while keyboard.is_pressed('q') == False:
#     time.sleep(2)
#     # pic = pyautogui.screenshot(region=(710, 565, 250, 115))
#     pic = pyautogui.screenshot(region=(680, 560, 970-680, 670-560))
#     # pic = pyautogui.screenshot(region=(986, ))

#     for x in range(970-680-1, 0, -1):
#         for y in range(670-560-1, 0, -1):
#             r, g, b = pic.getpixel((x, y))

#             if r == 10:
#                 y_green_coord = y
#             elif r == 239:
#                 y_orange_coord = y

#             if y_green_coord and y_orange_coord:
#                 if y_green_coord == y_orange_coord:
#                     print(y_orange_coord, y_green_coord, "It met...")
#                     break

from yahoo_fin import stock_info as si


si.get_live_price("aapl")
si.get_quote_table("aapl")
