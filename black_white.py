#开发人员：王宁
#开发时间： 2022/9/27 16:10

import os, random, shutil
from PIL import Image
import numpy as np
from PIL import ImageFile

"""
#筛选黑白图像#
检测图像中的黑白像素点，
将黑白像素占比高的图像筛选到目标文件夹
"""

ImageFile.LOAD_TRUNCATED_IMAGES = True#同名文件转移
traversal_file = r"F:\taian\20220830" #原文件夹
output_file = r"E:\work\outwhiteblack"   # 转移目标文件夹
def show_files(path, all_files):
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

if (os.path.exists(output_file)) != True:
    os.mkdir(output_file)

contents = show_files(traversal_file, [])  # 循环打印show_files函数返回的文件名列表
fname = r"E:\work\test\sum.txt"  # 记录数目与文件进度
lenth = len(contents)

with open(fname, 'r') as f:  # 打开文件
    lines = f.readlines()  # 读取所有行
    w = lines[0]  # 取第一行
w = int(float(w))
    # print('xmlname:',xmlname)

for i in range(0,lenth-1):
    # 遍历修改
    # print(content)
    src = contents[i]
    # zhixin_1 = content.split("_")[6]
    # zhixin = zhixin_1.split(".")[0] + '.' + zhixin_1.split(".")[1]
    # num = float(zhixin)
    img_L = np.array(Image.open(contents[i]).convert("L"))
    img_RGB = np.array(Image.open(contents[i]).convert("RGB"))

    # temp = {}
    # for m in range(img_L.shape[0]):
    #     for n in range(img_L.shape[1]):
    #         if not temp.get(int(img_L[m][n])):
    #             temp[int(img_L[m][n])] = list(img_RGB[m][n])
    # print(temp)

# 这里得到灰度像素值0对应(0,0,0),62对应(19,69,139)
    color_white = 0
    for j in range(200, 255):  # 255,255,255是白色
        color_white += np.where(img_L == j)[0].shape[0]

    color_black = 0
    for q in range(0, 70):  # 0,0,0是黑色
        color_black += np.where(img_L == q)[0].shape[0]

    color_green = 0
    for q in range(70, 100):  # 0,0,0是黑色
        color_green += np.where(img_L == q)[0].shape[0]

    pixel_sum = img_L.shape[0] * img_L.shape[1]
    white_format = color_white / pixel_sum
    black_format = color_black / pixel_sum
    green_format = color_green / pixel_sum

    # print(white_format)
    # print(black_format)
    # print("白色像素个数：{} 占比：%{}".format(color_white, color_white / pixel_sum * 100))
    # print("黑色像素个数：{} 占比：%{}".format(color_black, color_black / pixel_sum * 100))
    # print("mm像素个数：{} 占比：%{}".format(color_green, color_green / pixel_sum * 100))

    w = w + 1
    with open(r"E:\work\test\sum.txt", 'w', encoding='utf-8') as f:  # 使用with open()新建对象f
        f.write(str(w))  # 写入数据，文件保存在上面指定的目录，加\n为了换行更方便阅读
        # print("已保存进度", w)
    # or ((black_format + color_green) >= 0.60 and (black_format + color_green) <= 0.55)
    # and white_format <= 0.15
    if (black_format >= 0.30 and white_format >= 0.04) or (black_format >= 0.70):
        try:
            dst_1 = output_file + "/" + os.path.basename(contents[i])
            shutil.move(src, dst_1)
            print(src)
        except:
            print("未进行保存")

