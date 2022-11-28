#开发人员：王宁
#开发时间： 2022/11/15 15:27

import xml.etree.ElementTree as ET
import os
from PIL import Image
import shutil
from os import listdir, getcwd

"""
#xml文件转txt文件特殊版#
可以读取只有矩形框数据的xml,
并把它转化为txt文件

需要与图像同文件夹
"""

path = r"E:\work\test\sunhot11"
classes = ["sunIR","sunVisible"]  # 这里输入你的数据集类别

def convert(size, box, lablenum):  # 读取xml文件中的数据，xywh
    dw = 1 / size[0]
    dh = 1 / size[1]
    x = (box[0] + box[2]) / 2.0
    y = (box[1] + box[3]) / 2.0
    w = box[2] - box[0]
    h = box[3] - box[1]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (lablenum,x, y, w, h)

def add_source(xmlfilepath):
    xml_file = open(xmlfilepath, 'r+')  # 存入txt文件的文件夹
    str = xml_file.readlines()

    for i in range(len(str)):
        str[i]="\t"+str[i]
    str.insert(0, "<annotation>\n")
    str.append("</annotation>\n")
    xml_file.seek(0,0)
    xml_file.writelines(str)
    xml_file.close()

    return

def convert_annotation(i,xmlfilepath,w,h):
    out_file = open(path + "/" + "hot" + str(i) + ".txt", 'w')  # 存入txt文件的文件夹
    # xml_file = open(xmlfilepath, 'r+')  # 存入txt文件的文件夹
    # str=xml_file.readlines()
    add_source(xmlfilepath)


    print("xml:",str)
    tree = ET.parse(xmlfilepath)
    root = tree.getroot()

    # 读取<object></object>
    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        lablename = obj.find('name').text
        if lablename not in classes or int(difficult) == 1:
            continue
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text),
             int(xmlbox.find('ymax').text))
        lablenum = classes.index(lablename)
        bb = convert((w, h), b, lablenum)
        print(bb)
        out_file.write(" ".join([str(a) for a in bb]) + '\n')
        # out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

def show_files(path, all_files):
    file_list = os.listdir(path)
    for file in file_list:
        cur_path = os.path.join(path, file)
        if os.path.isdir(cur_path):
            show_files(cur_path, all_files)
        else:
            all_files.append(path + "/" + file)
    return all_files


def main():
    allfilelist = show_files(path,[])
    i = 0

    while True:
        if i >= len(allfilelist):
            break
        # print(allfilelist[i])
        # print(os.path.dirname(allfilelist[i]))
        if os.path.basename(allfilelist[i]).split(".")[1] == "xml":
            try:
                imgpath = os.path.dirname(allfilelist[i]) + "/" + os.path.basename(allfilelist[i]).split(".")[0] + ".jpg"
                imgtopath = path + "/" + "hot" + str(i) + ".jpg"
                shutil.copy(imgpath, imgtopath)
                img = Image.open(imgpath)
                w = img.width
                h = img.height
                convert_annotation(i,allfilelist[i],w,h)
            except Exception as exc:
                print("此文件发生错误",allfilelist[i],exc)
        i += 1
if __name__ == '__main__':
    main()