#开发人员：王宁
#开发时间： 2022/10/19 9:37

import cv2
import os

"""
#抽帧脚本#
将视频中的首帧抽取
并保存在指定文件夹
"""

traversal_file = r"G:\ab_video"#要抽帧的文件
outPutDirName = r"E:\work\picture_fuayngben_chouzhen"#保存的图像文件

def show_files(path, all_files):
    file_list = os.listdir(path)
    for file in file_list:
        cur_path = os.path.join(path, file)
        # 判断是否是文件夹
        if os.path.isdir(cur_path):
            show_files(cur_path, all_files)
        else:
            # 拼接文件路径
            all_files.append(path + "/" + file)
    return all_files

file_list = show_files(traversal_file,[])
def video_to_frames(video_path, outPutDirName):
    times = 0

    # 提取视频的频率，每1帧提取一个
    frame_frequency = 750

    # 如果文件目录不存在则创建目录
    if not os.path.exists(outPutDirName):
        os.makedirs(outPutDirName)

    # 读取视频帧
    camera = cv2.VideoCapture(video_path)
    flag = 0
    while True:
        times = times + 1
        res, image = camera.read()
        if not res:
            print('not res , not image')
            break
        # 按照设置间隔存储视频帧
        if times % frame_frequency == 0:
            cv2.imwrite(outPutDirName + '\\' + os.path.basename(video_path).split(".")[0] + "_" +str(flag) + '.jpg', image)
            flag += 1
            print(video_path,flag-1)

    print('图片提取结束')
    # 释放摄像头设备
    camera.release()

if __name__ == '__main__':
    for i in range(len(file_list)):
        video_to_frames(file_list[i],outPutDirName)


