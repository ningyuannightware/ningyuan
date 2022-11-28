#开发人员：王宁
#开发时间： 2022/11/4 10:49

import os, cv2
from PIL import Image
import glob
import shutil

"""
#筛选删除图像#
可视化文件夹，删除图像
"""

i = 0
def show_files(path, all_files):
    '''遍历文件夹，获得要转换的文件名称'''
    # 首先遍历当前目录所有文件及文件夹
    file_list = os.listdir(path)
    # 准备循环判断每个元素是否是文件夹还是文件，是文件的话，把名称传入list，是文件夹的话，递归
    for file in file_list:
        # 利用os.path.join()方法取得路径全名，并存入cur_path变量，否则每次只能遍历一层目录
        cur_path = os.path.join(path, file)
        # 判断是否是文件夹
        if os.path.isdir(cur_path):
            show_files(cur_path, all_files)
        else:
            # 拼接文件路径
            all_files.append(path + "/" + file)
    return all_files
traversal_file = r"E:\work\abcapture\cloud" #原文件夹
contents = show_files(traversal_file, [])  # 循环打印show_files函数返回的文件名列表



for i in range(len(contents)):
    # 遍历修改
    print(contents[i])
    img_1 = cv2.imread(contents[i])
    cv2.namedWindow('img1', 0)
    cv2.resizeWindow('img1', 1500, 1000)  # 自己设定窗口图片的大小
    cv2.imshow("img1", img_1)
    key = cv2.waitKey(0)
    if key == 32:  # 空格键，下一张
        i += 1
        continue
    if key == 49:
        print("shanhcu")
        i -= 2
    if key == 48:
        os.remove(contents[i])
        print("删除图片!")
    if key == 27:
        break
