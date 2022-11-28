#开发人员：王宁
#开发时间： 2022/9/28 9:20
#开发人员：王宁
#开发时间： 2022/8/15 10:58
import os, cv2
from PIL import Image
import glob
import shutil
import numpy as np

"""
#筛选阿坝州日期文件夹的图像#
设置可视化文件夹：raw_file
设置进度文件：numtxtpath
设置相应的对比文件夹：contrast_file
设置要转出的原始文件夹：output_file
设置要保存的目标文件夹：save_file

按空格下一张
按0转移文件
"""

fname = r"E:\work\abcapture\date.txt"  # 记录数目与文件进度
raw_file = r"E:\work\abcapture\delete"  # 可视化界面的文件夹,首要文件夹
save_file = r"E:\work\abcapture\test"  # 目标文件夹，保存路径

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

def date_set(raw_name):
    date = raw_name.split('_')[0] + "-" + raw_name.split('_')[1] + "-" +raw_name.split('_')[2]
    return date

def main(w,lenth,raw_contents,raw_list):

    for i in range(w,lenth):
        # 遍历修改
        raw_name = raw_list[i]
        date = date_set(raw_name)
        contrast_file = r'E:\work\abpicture' + "/" + date + "/imgs"  # 可视化对比文件夹
        output_file = r'E:\work\abpicture' + "/" + date + "/videos"  # 原始文件夹，转出路径
        if (os.path.exists(save_file)) != True:
            os.mkdir(save_file)

        output_list = os.listdir(output_file)  # 转出路径文件名列表

        img1 = cv2.imread(raw_contents[i])
        contrast_name = contrast_file + "/" + raw_list[i]
        img2 = cv2.imread(contrast_name)
        try:
            img1 = cv2.resize(img1, (800, 580))
            # 设置图2的宽高，与图1相同
            img2 = cv2.resize(img2, (800, 580))

        except:
            print("报错了")
            continue
        vs = np.hstack((img1, img2))

        cv2.namedWindow('img', cv2.WINDOW_AUTOSIZE)
        cv2.setWindowProperty('img', cv2.WND_PROP_TOPMOST, 1)
        cv2.imshow("img", vs)

        # 等待键值
        key = cv2.waitKey(0)
        w = w + 1
        with open(r'E:\work\abcapture\date.txt', 'w', encoding='utf-8') as f:  # 使用with open()新建对象f
            f.write(str(w) + '\n')  # 写入数据，文件保存在上面指定的目录，加\n为了换行更方便阅读
            print("已保存进度", w)

        if key == 48:      #根据对比路径移动到指定文件夹
            for output in output_list:
                f1 = raw_list[i].split('.')[0]
                f2 = output.split('.')[0]
                if f1 == f2:
                    out_path = output_file + "/" + output
                    shutil.copy(out_path, save_file)
                    print("原始文件复制成功")
        if key == 27:    #ESC退出，关闭窗口
            break
        else:
            continue

    cv2.destroyAllWindows()


if __name__ == '__main__':

    raw_list = os.listdir(raw_file)  # 原始路径文件名列表
    raw_name = raw_list[0]
    date = date_set(raw_name)
    print(date)

    raw_contents = show_files(raw_file, [])  # 原始路径的文件绝对地址列表

    lenth = len(raw_contents)

    with open(fname, 'r') as f:  # 打开文件
        lines = f.readlines()  # 读取所有行
        w = lines[0]  # 取第一行

    w = int(float(w))
    main(w,lenth,raw_contents,raw_list)


