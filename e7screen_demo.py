#开发人员：王宁
#开发时间： 2022/10/19 11:49
import pyautogui
import time
"""
pycharm最小化：1774,19


"""
pyautogui.mouseInfo()#获取点赞图片的位置(1127,756,1146,775)

# picture1 = screen_images.crop((1770,0,1821,35))  #最小化框
# picture2 = screen_images.crop((168,104,1045,153)) #输入框
# picture1 = screen_images.crop((905,104,1391,163))
# picture1 = screen_images.crop((639,1031,707,1076))

# screen_images = pyautogui.screenshot()  # 截取整个屏幕
# picture1 = screen_images.crop((905,104,1391,163)) # 根据截取的屏幕仅截取“带赞的手势图片”，用pyautogui.mouseInfo()获取图片的位置(1127,756,1146,775)，这里截取区域用到了Pillow
# picture1.save(r"E:\e7demo\huanchong.png")  # 将图片保存供pyautogui.locateOnScreen（）使用

# screen_images2 = pyautogui.screenshot()
# screen_images2 = Image.open(r"F:\0pythonproject\daily\my_script\mouseInfoScreenshot.png")
# picture2 = screen_images2.crop((166,101,1044,151))
# picture2.save(r"E:\e7demo\shurukuang.png")

# time.sleep(2)
# screen_images = pyautogui.screenshot()  # 截取整个屏幕
# picture1 = screen_images.crop((32,651,102,678)) # 根据截取的屏幕仅截取“带赞的手势图片”，用pyautogui.mouseInfo()获取图片的位置(1127,756,1146,775)，这里截取区域用到了Pillow
# picture1.save(r"E:\e7demo\pan.png")  # 将图片保存供pyautogui.locateOnScreen（）使用