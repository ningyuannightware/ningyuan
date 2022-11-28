#开发人员：王宁
#开发时间： 2022/11/19 14:16
import os
import shutil
"""
筛选jpg和txt文件中，
标签txt文件大小为0的图像，移动到指定文件夹
"""

path = r"E:\work\test\hot_pictures"
topath = r"E:\work\test2\hot_no"
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

def get_filesize(filepath):
    fsize = os.path.getsize(filepath)
    return fsize

def main(allfilelist):
    for file in allfilelist:
        fsize = get_filesize(file)
        if fsize < 1:
            picturefile = os.path.dirname(file) + "/" + os.path.basename(file).split(".")[0] + ".jpg"
            print("picturepath",picturefile)
            print("lablepath",file)
            shutil.move(picturefile,topath)
            shutil.move(file, topath)
        else:
            continue

if __name__ == '__main__':
    allfilelist = show_files(path, [])
    main(allfilelist)