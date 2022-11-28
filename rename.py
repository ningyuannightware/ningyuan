#开发人员：王宁
#开发时间： 2022/9/20 15:07
import os, cv2
"""
#文件重命名#
将文件夹中文件，
重命名为数字序列
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
traversal_file = r"E:\work\test" #原文件夹，要重命名的文件夹
output_file = r"E:\work\test"   # 转移目标文件夹,out22920为自定义文件夹命名


if (os.path.exists(output_file)) != True:
    os.mkdir(output_file)

contents = show_files(traversal_file, [])  # 循环打印show_files函数返回的文件名列表
lenth = len(contents)

for i in range(lenth-1):
    # 遍历修改
    # print(content)
    path = output_file +"/" + str(i) +'.png'
    try:
        print('src:', contents[i])
        print('dst:', path)
        # os.remove(content)
        os.rename(contents[i],path)
    except:
        print("未进行保存")