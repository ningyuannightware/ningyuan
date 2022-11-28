#开发人员：王宁
#开发时间： 2022/8/15 10:58
import os, cv2
from PIL import Image
import glob
import shutil

#单图空格转移保存，并计数

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

def save_num(w,num):
    w = w + 1
    num = num + 1
    with open('E:/work/picture count/num.txt', 'w', encoding='utf-8') as f:  # 使用with open()新建对象f
        f.write(str(w) + '\n')  # 写入数据，文件保存在上面指定的目录，加\n为了换行更方便阅读
        print("已保存进度", w)
        f.write(str(num) + '\n')  # 写入数据，文件保存在上面指定的目录，加\n为了换行更方便阅读
        print("已记载计数", num)

traversal_file = r"E:\work\abcapture\delete"  #可视化界面的文件夹,首要文件夹
traversal_file2 =r'F:\0pythonproject\yolov5\runs\detect\100fog\l nofog 100'   #可视化对比文件夹
output_file = r"E:\work\abcapture\smoke"     # 目标文件夹，保存路径
contrast_dir =r'E:\work\abpicture' + "/" + date +"/videos"        #原始文件夹，转出路径

contents = show_files(traversal_file, [])  # 原始路径的文件名列表
contents2 = show_files(contrast_dir,[])    #对比路径的文件名列表
contents3 = show_files(traversal_file2,[])
fist_list = os.listdir(traversal_file)
last_list = os.listdir(contrast_dir)


lenth = len(contents)
fname = r"E:\work\picture count\num.txt"   #记录数目与文件进度
if (os.path.exists(output_file)) != True:
    os.mkdir(output_file)

with open(fname, 'r') as f:  #打开文件
    lines = f.readlines() #读取所有行
    w = lines[0] #取第一行
with open(fname, 'r') as f:  #打开文件
    lines = f.readlines() #读取所有行
    num = lines[-1] #取最后一行

i = 0
w = int(float(w))
num = int(float(num))
# w = 0

for i in range(w,lenth):
    # 遍历修改
    # print(contents[i])
    # print(fist_list[i])
    img = cv2.imread(contents[i])
    cv2.namedWindow('img', 0)
    cv2.resizeWindow('img', 800, 800)  # 自己设定窗口图片的大小
    cv2.imshow("img", img)
    img2 = cv2.imread(contents3[i])
    cv2.namedWindow('img2', 0)
    cv2.resizeWindow('img2', 800, 800)  # 自己设定窗口图片的大小
    cv2.imshow("img2", img2)
    # 等待键值
    key = cv2.waitKey(0)
    w = w + 1
    with open('E:/work/picture count/num.txt', 'w', encoding='utf-8') as f:  # 使用with open()新建对象f
        f.write(str(w) + '\n')  # 写入数据，文件保存在上面指定的目录，加\n为了换行更方便阅读
        print("已保存进度", w)
    if key == 32:    #普通的移动（复制）计数
        num = num + 1
        src = contents[i]
        dst = output_file
        try:
            shutil.move(src, dst) #复制首要文件夹
            print("复制成功")
        except FileNotFoundError as e:
            print('警告')
            pass

    if key == 48:      #根据对比路径移动到指定文件夹
        num = num + 1
        print("计数",num)
        for content2 in last_list:
            # f1 = contents[i].split('.')[0]
            # f2 = content2.split('.')[0]
            if fist_list[i] == content2:
                shutil.copy(contents2[i], output_file)
                print("原始文件复制成功" + '\n')
    if key == 27:    #ESC退出，关闭窗口
        break
    else:
        continue
with open('E:/work/picture count/num.txt', 'a', encoding='utf-8') as f:  # 使用with open()新建对象f
    f.write(str(num) + '\n')  # 写入数据，文件保存在上面指定的目录，加\n为了换行更方便阅读
    print("计数记录", num)
cv2.destroyAllWindows()



