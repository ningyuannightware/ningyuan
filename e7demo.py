#开发人员：王宁
#开发时间： 2022/10/18 16:45
from PIL import Image
import pyautogui
import time
import cv2

time.sleep(2)  # 留一点切换页面时间
# screen_images = pyautogui.screenshot()  # 截取整个屏幕
# picture1 = screen_images.crop((905,104,1391,163)) # 根据截取的屏幕仅截取“带赞的手势图片”，用pyautogui.mouseInfo()获取图片的位置(1127,756,1146,775)，这里截取区域用到了Pillow
# picture1.save(r"E:\e7demo\huanchong.png")  # 将图片保存供pyautogui.locateOnScreen（）使用

# screen_images2 = pyautogui.screenshot()
# screen_images2 = Image.open(r"F:\0pythonproject\daily\my_script\mouseInfoScreenshot.png")
# picture2 = screen_images2.crop((166,101,1044,151))
# picture2.save(r"E:\e7demo\shurukuang.png")

# time.sleep(1)

def open_yemian():
    time.sleep(1)  # 这个可以用来防止操作过快
    left, top, width, height = pyautogui.locateOnScreen(r"E:\e7demo\dianzan.png")  # 寻找刚才保存点赞手势图片
    center = pyautogui.center((left, top, width, height))  # 寻找图片的中心
    pyautogui.click(center)
    print('打开页面成功！')

def zuixiaohua():
    # screen_images2 = pyautogui.screenshot()
    # picture2 = screen_images2.crop((1771,0,1819,32))
    # picture2.save(r"E:\work\GK2A\zuixioahua.png")
    time.sleep(1)  # 这个可以用来防止操作过快
    left, top, width, height = pyautogui.locateOnScreen(r"E:\e7demo\zuixioahua.png")  # 寻找刚才保存点赞手势图片
    center = pyautogui.center((left, top, width, height))  # 寻找图片的中心
    pyautogui.click(center)
    print("最小化成功！")
def shurukuang():
    left, top, width, height = pyautogui.locateOnScreen(r"E:\e7demo\shurukuang.png")  # 寻找刚才保存点赞手势图片
    center = pyautogui.center((left, top, width, height))  # 寻找图片的中心
    pyautogui.click(center)
    print("点击成功")
def shuru():
    pyautogui.write("pyhton使用手册", interval=0.3)
    pyautogui.press(' ')
    pyautogui.press('enter')
    print("输入")
def huanchong():
    left, top, width, height = pyautogui.locateOnScreen(r"E:\e7demo\huanchong.png")  # 寻找刚才保存点赞手势图片
    center = pyautogui.center((left, top, width, height))  # 寻找图片的中心
    pyautogui.click(center)
    print("点击成功")
def dianji():
    left, top, width, height = pyautogui.locateOnScreen(r"E:\e7demo\baiduyixia.png")  # 寻找刚才保存点赞手势图片
    center = pyautogui.center((left, top, width, height))  # 寻找图片的中心
    pyautogui.click(center)
    print("点击百度！")

count = 2  # 为了防止一直运行下去，点一定数量的赞就结束，自己定义
while count:
    try:
        open_yemian()
        time.sleep(2)
        shurukuang()
        time.sleep(2)
        shuru()
        # time.sleep(2)
        # huanchong()
        # time.sleep(2)
        # dianji()
        # zuixiaohua()
        count -= 1
    except TypeError:  # 错误类型没有也文图不大，哈哈哈
        # pyautogui.scroll(-500)  # 本页没有图片后，滚动鼠标；
        # print('没有找到目标，屏幕下滚~')
        break
print("结束！")