#开发人员：王宁
#开发时间： 2022/11/15 13:40

import os
import xml.etree.ElementTree as ET

"""
xml文件修改脚本
"""
path = r"E:\work\test"

def show_files(path, all_files):
    file_list = os.listdir(path)
    for file in file_list:
        cur_path = os.path.join(path, file)
        if os.path.isdir(cur_path):
            show_files(cur_path, all_files)
        else:
            all_files.append(path + "/" + file)
    return all_files

def __indent(elem, level=0):
    i = "\n" + level*"\t"
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "\t"
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            __indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


def setxml(allfile_list):
    root = ET.Element("annotation")#创建根节点

    folder_et = ET.Element("folder")#创建子节点
    folder_et.text = "filedirname"#子节点的内容
    filename_et = ET.Element("filename")
    filename_et.text = "picture_name"
    path_et = ET.Element("path")
    path_et.text = "filepath"
    source_et = ET.Element("source")
    source_et_child = ET.SubElement(source_et,"database")#创建子节点的子节点
    source_et_child.text = "Unknown"
    size_et = ET.Element("size")
    size_et_width = ET.SubElement(size_et,"width")
    size_et_width.text = "width"
    size_et_height = ET.SubElement(size_et,"height")
    size_et_height.text = "height"
    size_et_depth = ET.SubElement(size_et,"depth")
    size_et_depth.text = "depth"
    segmented_et = ET.Element("segmented")
    segmented_et.text = "0"

    tree = ET.parse(allfile_list[0])#读取xml文件
    root2 = tree.getroot()#得到文件的根节点

    root.extend((folder_et,filename_et,path_et,source_et,size_et,segmented_et,root2))#关键，拼装各个节点到root根节点
    __indent(root)#格式美化，调整换行
    trees = ET.ElementTree(root)#生成以root节点为根节点的trees
    trees.write(path + "test.xml")#保存为xml文件

def main(allfile_list):

    for file in allfile_list:
        print(file)


if __name__ == '__main__':
    allfile_list = show_files(path, [])
    main(allfile_list)