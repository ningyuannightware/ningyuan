import os,cv2
import shutil
import numpy as np
import tkinter
import tkinter.messagebox#弹窗库

flagmsg = 0
flagdel = 0

x0=0
y0=0

def OnMouse(event,x,y,flags,param): #鼠标事件
    global x0,y0,x1,y1
    if event==cv2.EVENT_LBUTTONDOWN:#左键单击,这里可以设置为其他的鼠标动作
        x0, y0 = x, y
        xy = 'classified'
        cv2.putText(imgs, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
                    12, (0,0,255), thickness = 10)
        cv2.imshow("imgs", imgs)

        return x0,y0

def Move_file(key,local_list):  #文件移动致文件夹
    path_t = r'E:\pic'
    path_f = r'E:\pic\false'
    if key == 100:  # d
        src = os.path.join(raw_path, tempname_list)
        dst = os.path.join(path_t, tempname_list)
        try:
            shutil.move(src, dst)
        except FileNotFoundError as e:
            print('警告')
            pass
    if key == 97:  # a
        src = os.path.join(raw_path, tempname_list)
        dst = os.path.join(path_f, tempname_list)
        try:
            shutil.move(src, dst)
        except FileNotFoundError as e:
            print('警告')
            pass
    # if key == 119: # w
    #     with open('E:/pic/true/num.txt', 'w', encoding='utf-8') as f:  # 使用with open()新建对象f
    #         i_back = int(float(i))-1
    #         f.write(str(i_back) + '\n')  # 写入数据，文件保存在上面指定的目录，加\n为了换行更方便阅读
    #         print("已回退进度", i_back)

def Windowmake(imgs):
    cv2.namedWindow('imgs', 0)
    cv2.resizeWindow('imgs', 2400, 1000)
    cv2.imshow("imgs", imgs)


raw_path = r"E:\pic\img\AB4"
detected_path = r'D:\pythonproject\yolov5\runs\detect\exp4'
fname = 'E:/pic/true/num.txt'
file_list = os.listdir(detected_path)
pics_lenth = len(file_list)
num_picset = divmod(pics_lenth,4)   #整个图片文件夹的组数  4个为一组
w = 1

with open(fname, 'r') as f:  #打开文件
    lines = f.readlines() #读取所有行
    w = lines[-1] #取最后一行

w = int(float(w))
for i in range(w,num_picset[0] ):
    s ="当前为第 %d 组，还剩 %d 组" %( i+1, num_picset[0]-i-1,)
    print(s)
    with open('E:/pic/true/num.txt', 'w', encoding='utf-8') as f:  # 使用with open()新建对象f
        f.write(str(i) + '\n')  # 写入数据，文件保存在上面指定的目录，加\n为了换行更方便阅读
        print("已保存进度",i+1)
    # group_num = i
    picset_list = file_list[4*i:4*(i+1)]  #从整体文件队列中，根据组别，选出4个作为列表
    detected_pic_path = []  #创建检测列表
    imgs_list = []
    for j in range(0,4):
        detected_pic_path.append(os.path.join(detected_path,picset_list[j]))
        img = cv2.imread(detected_pic_path[j])
        if list(img.shape)!=[1520,2688,3] :
            img=cv2.resize(img,(2688,1520),)
        imgs_list.append(img)
        #统一图片格式

    imgs_set = np.array(imgs_list) #数组
    imgset_list=[]
    for j in range(0,2) :
        set_temp = imgs_set[2*j, :, :, :]
        for k in range(1,2):
            temp = imgs_set[2*j+k, :, :, :]
            set_temp = np.vstack([set_temp, temp]) #垂直方向堆叠一个新数组
        imgset_list.append(set_temp)

    imgs_temp = np.array(imgset_list)
    imgs = imgs_temp[0,:,:,:]

    for i in range(1,2) :
        imgs = np.hstack([imgs,imgs_temp[i,:,:,:]]) #水平方向堆叠一个新数组
    Windowmake(imgs)
    key = 9
    while key!= 115: #s
        key =9
        local_list = []
        while key == 9:
            key = 0
            cv2.setMouseCallback('imgs', OnMouse)
            key = cv2.waitKey(0)
            pic_local_x = int(x0 / 2688)
            pic_local_y = int(y0 / 1520)
            pic_local = 2 * pic_local_x + pic_local_y
            pic_name = picset_list[pic_local]
            local_list.append(pic_name)

        local_list=list(set(local_list))
        for tempname_list in local_list:
            Move_file(key)
    local_list=[]


for i in range(pics_lenth-num_picset[1],pics_lenth) :
    content = file_list[i]
    pic_name = os.path.join(detected_path,content)
    imgs = cv2.imread(pic_name)
    Windowmake(imgs)
    key = 999
    while key != 115:
        key = 0
        key = cv2.waitKey(0)
        Move_file(key)
