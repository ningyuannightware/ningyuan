#开发人员：王宁
#开发时间： 2022/8/19 14:44

import os, cv2
from PIL import Image
import glob
import shutil

"""
#文件名特征分类脚本#
根据文件名的特点，
将指定文件剔除到目标文件夹
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
traversal_file = r"E:\work\out819" #原文件夹
output_file = r"E:\work\out819057"   # 转移目标文件夹
contrast_dir =r''

if (os.path.exists(output_file)) != True:
    os.mkdir(output_file)

contents = show_files(traversal_file, [])  # 循环打印show_files函数返回的文件名列表


# #1.识别文件后缀，当后缀为_1,为可见光图像，后缀为_2为热成像图像
# for content in contents:
#     # 遍历修改
#     # print(content)
#     src = content
#     if content.split("_")[1] == '1.jpeg':
#         try:
#             dst_1 = output_file + "/"  + os.path.basename(content)
#             print('src:', content)
#             print('dst:', dst_1)
#             shutil.copy(src, dst_1)
#         except:
#             print("未进行保存")

#2.识别置信度，大于0.75的转移
for content in contents:
    # 遍历修改
    # print(content)
    src = content
    zhixin_1 = content.split("_")[6]
    zhixin = zhixin_1.split(".")[0] + '.' + zhixin_1.split(".")[1]
    num = float(zhixin)
    if num >= 0.75:
        try:
            dst_1 = output_file + "/"  + os.path.basename(content)
            print('src:', content)
            print('dst:', dst_1)
            shutil.copy(src, dst_1)
        except:
            print("未进行保存")

