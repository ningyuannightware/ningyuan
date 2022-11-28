#开发人员：王宁
#开发时间： 2022/8/19 9:13

import os, random, shutil
"""
#同名文件转移#
将不同文件夹中，相同文件名的文件转移到目标文件夹
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
traversal_file = r"E:\work\out819" #原文件夹
output_file = r"E:\work\out819057"   # 转移目标文件夹

if (os.path.exists(output_file)) != True:
    os.mkdir(output_file)

contents = show_files(traversal_file, [])  # 循环打印show_files函数返回的文件名列表

time = "2022-9-14"

xml_dir = r"F:\0pythonproject\daily" + "/" + time + "/"+"imgs"  #对比的路径,画框的路径
initimage_dir = r"E:\work\abcapture" +"/" + time #转出的路径，原图
image_dir = 'E:/work/out/'   #转入路径
initimages = os.listdir(initimage_dir)   #转出，原图
initxml = os.listdir(xml_dir) #对比，画框的
count = 0
flag = 0
for imagename in initimages:
    # print('xmlname:',xmlname)
    for xmlname in initxml:
        test_xml = xmlname.split('.')[0]
        test_image = imagename.split('.')[0]
        if test_xml == test_image:
            # shutil.move(initimage_dir + imagename, image_dir + imagename)  #移动图片
            # shutil.copy(initimage_dir + imagename, image_dir + imagename)    #复制图片
            count += 1
            flag = 1
    if flag == 0:
        os.remove(imagename)


    print('count:', count)