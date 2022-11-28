#开发人员：王宁
#开发时间： 2022/8/16 14:00

import os, cv2
from PIL import Image
import glob
import shutil
"""
#图像画框#
将文件名中的矩形框坐标
画在图像中

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


traversal_file = r"G:\9.1\data\data" #原图片位置
output_file = r"E:\work\out2"  #要保存的位置
if (os.path.exists(output_file)) != True:
    os.mkdir(output_file)

contents = show_files(traversal_file, [])  # 循环打印show_files函数返回的文件名列表
for content in contents:
        # print(content)
        img = cv2.imread(content)

        x = content.split("_")[2]
        y = content.split("_")[3]
        x_2 = content.split("_")[4]
        y_2 = content.split("_")[5]
        y_3 = y_2.split(".")[0]
        zhixin_1 = content.split("_")[6]
        zhixin = zhixin_1.split(".")[0] + '.' + zhixin_1.split(".")[1]

        # 画出这个矩形
        cv2.rectangle(img, (int(float(x)),int(float(y))), (int(float(x_2)), int(float(y_3))), (0, 0, 255), 2)
        font = cv2.FONT_HERSHEY_SIMPLEX  # 定义字体
        imgzi = cv2.putText(img, zhixin , (int(float(x_2)), int(float(y_3))), font, 0.75, (0, 0, 255), 3)

        dst = output_file + '/' + os.path.basename(content)
        shutil.copy(content, dst)        #复制文件
        cv2.imwrite(dst, img)
        i = i+1
        print("no",i)
        print('src:', content)  # 原文件路径下的文件
        print('dst:', dst)  # 移动到新的路径下的文件

