#开发人员：王宁
#开发时间： 2022/10/10 13:27
import os, random, shutil
"""
#文件路径列表保存#
读取文件夹，
将所有文件路径添加到txt中
"""
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
traversal_file = r"E:\work\picture count" #原文件夹

contents = show_files(traversal_file, [])

for i in range(len(contents)):
    with open(r'E:/work/picture count/num.txt', 'a', encoding='utf-8') as f:  # 使用with open()新建对象f
        f.write(contents[i] + "\n")  # 写入数据，文件保存在上面指定的目录