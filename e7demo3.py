#开发人员：王宁
#开发时间： 2022/10/26 11:06
from PIL import Image
import pyautogui
import time
import cv2

button_1 = r"E:\e7demo\pan.png"

def find_button(picture_path,region):
    """
    检测确认函数，并返回坐标！
    picture_path 要检测的图像标本路径
    picture_regin 划定检测区域，加快检测速度
    """
    time.sleep(1)  # 这个可以用来防止操作过快
    result = pyautogui.locateOnScreen(picture_path,region)  # region来划定检测区域，提高监测速度
    center = pyautogui.center(result)
    if result is not None:
        return True,center
    else:
        return False,center

def open_button(picture_path):
    """
    检测图像点击函数
    picture_path 要检测的图像标本路径
    picture_regin 划定检测区域，加快检测速度
    """
    time.sleep(1)  # 这个可以用来防止操作过快
    result = pyautogui.locateOnScreen(picture_path)
    center = pyautogui.center(result)
    pyautogui.click(center)
    print("图像检测点击成功！")

def slide():
    """
    鼠标移动函数
    """
    xOffset = 30
    yOffset = -50
    num_seconds = 1
    pyautogui.moveRel(xOffset, yOffset, duration=num_seconds)
    print('打开页面成功！')


def location_button(x):
    """
    点击固定坐标函数
    """
    time.sleep(1)  # 这个可以用来防止操作过快
    pyautogui.click(x)
    print("位置点击成功！")

def cycledetection(picpath,region,detectmode,picpath_other):
    """
    持续检测某图片是否出现在页面，若出现，根据detectmode判断点击目标
    picpath，要检测的图片
    region，划定范围
    detectmode,检测
    """
    while True:
        try:
            flag_1, center_1 = find_button(picpath,region)  # 检测图像是否存在
            if flag_1 is True:
                if detectmode == 1:
                    location_button(center_1)  # 点击该图像中心点
                    break
                if detectmode == 2:
                    open_button(picpath_other)  # 寻找其他指定的图像，并点击中心点
                    break
        except:
            continue

def taofa(count):
    """
    讨伐流程
    """
    # count = 10  # 重复10轮宠物循环战斗
    while count:
        try:
            print(f"开始第{11 - count}轮讨伐！")
            # open_button() #点击进入战斗
            cycledetection(button_1, (0, 338, 753, 882),2,button_1) #2代表需要指定其他位置进行点击
            time.sleep(2)
        except Exception as exc:
            print("讨伐循环出现错误！", exc)
            time.sleep(2)
        count -= 1

def goulaing_2_3(count):
    """
    速刷3狗粮的迷宫关卡
    """
    while count:
        open_button()#检测小人关卡图
        time.sleep(2)
        open_button()#点击进入战斗
        time.sleep(2)#缓冲
        count = 2
        dianweilist = []#设置三次点位的位置
        while count:
            location_button()  # 点击固定位置，进行第一点位跳转
            time.sleep(1)  # 缓冲
            cycledetection() #第一次战斗，检测战斗结束，2模式，点击结束战斗
            time.sleep(1)  # 缓冲
            count -= 1
        location_button()  # 点击固定点位，退出关卡
        time.sleep(2)
        location_button()  # 点击固定点位，结束战斗点位(可图像检测，也可固定点位)
        time.sleep(3)
        count -= 1

def gouliang9_4():
    while count:
        open_button()  # 检测小人关卡图
        time.sleep(2)
        open_button()  # 点击进入战斗
        time.sleep(2)  # 缓冲
        count = 2
        dianweilist = []  # 设置三次点位的位置
        while count:
            location_button()  # 固定点击迷宫,打开地图
            time.sleep(1)  # 缓冲
            location_button()  # 点击固定位置，进行第一点位跳转
            time.sleep(1)  # 缓冲
            cycledetection()  # 第一次战斗，检测战斗结束，2模式，点击结束战斗
            time.sleep(1)  # 缓冲
            count -= 1
        location_button()  # 点击固定点位，退出关卡
        time.sleep(2)
        location_button()  # 点击固定点位，结束战斗点位(可图像检测，也可固定点位)
        time.sleep(3)
        count -= 1
def paolasi():
    """
    跑拉斯检测！
    出现就等，并点击一下屏幕
    """
    ...


if __name__ == '__main__':

    MODE,count = input("请输入模式与轮数：")
    location_button(x  = (1774,19)) #pycharm运行最小化
    time.sleep(2)
    count = int(count)
    if MODE == "1":
        #启动页面为开始战斗页面
        taofa(count)
    if MODE == "2":
        #启动页面为小人关卡页面
        goulaing_2_3(count)
    if MODE == "3":
        ...
