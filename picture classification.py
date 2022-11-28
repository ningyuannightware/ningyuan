#开发人员：王宁
#开发时间： 2022/8/15 9:13

import os, cv2
from PIL import Image
import glob
import shutil
"""
#图像分类筛选脚本#
可视化文件夹
并根据数字按键，
将图像移动到对应的文件夹中
"""
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
traversal_file = r"F:\taian\20220830"

# 修改完成后输出的文件夹00
output_file = r"E:\work\taian"
contents = show_files(traversal_file, [])  # 循环打印show_files函数返回的文件名列表4
# filelist=['car','light',"fanguang","sun",'roof',"yanhuo","rain","factory","cloud","others"]
 #          0      1        2        3      4        5       6      7       8       9
filelist=['delete','smoke',"other","car","cloud"]


contents = show_files(traversal_file, [])  # 循环打印show_files函数返回的文件名列表

for content in contents:
    # 遍历修改
    img_1 = cv2.imread(content)
    cv2.namedWindow('img1', 0)
    cv2.resizeWindow('img1', 800, 800)  # 自己设定窗口图片的大小
    cv2.imshow("img1", img_1)
        # 等待键值
    num=cv2.waitKey(0)
    num=num-48
    src_1 = content
    # src_2 = content[1]
    try:
        dst_1 = output_file + "/" +filelist[num]+'/' + os.path.basename(content)
        # dst_2 = output_file + "/" + filelist[num] + '/' + os.path.basename(content_1)
        print('src:', src_1)                 # 原文件路径下的文件
        print('dst:', dst_1)                 # 移动到新的路径下的文件
        shutil.move(src_1, dst_1)
    except:
        print("未进行保存")
    cv2.destroyAllWindows()