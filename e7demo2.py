#开发人员：王宁
#开发时间： 2022/10/26 10:35
from PIL import Image
import pyautogui
import time
import cv2

time.sleep(2)  # 留一点切换页面时间


def open_yemian():
    time.sleep(1)  # 这个可以用来防止操作过快
    result = pyautogui.locateOnScreen(r"E:\e7demo\pan.png")  # 寻找刚才保存点赞手势图片
    center = pyautogui.center(result)
    if len(result) != 0:
        print("这里有个盘！")
    xOffset = 30
    yOffset = -50
    num_seconds = 0.5
    pyautogui.moveRel(xOffset, yOffset, duration=num_seconds)
    print('打开页面成功！')

def zuixiaohua():
    time.sleep(1)  # 这个可以用来防止操作过快
    # left, top, width, height = pyautogui.locateOnScreen(r"E:\e7demo\zuixioahua.png")  # 寻找刚才保存点赞手势图片
    # center = pyautogui.center((left, top, width, height))  # 寻找图片的中心
    pyautogui.click(x = (1774,19))
    print("最小化成功！")




if __name__ == '__main__':
    zuixiaohua()
    count = 3  # 点击循环次数
    # while count:
    #     try:
    #         open_yemian()
    #         count -= 1
    #     except TypeError:  # 错误类型没有也文图不大，哈哈哈
    #         break
    while True:
        try:
            open_yemian()
        except:
            time.sleep(5)
    print("结束！")