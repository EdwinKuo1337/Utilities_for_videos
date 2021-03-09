import cv2
import numpy as np
import glob
 

subjects = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10']
# subjects = ['01']




for subject in subjects:
    img_array = []
    name_array = []
    for index, filename in enumerate(glob.glob('/data2/NewDataset/' + subject + '/' + 'all_pictures/' + '*.jpg')):
        name_array.append(int(filename.split('/')[-1].split('.')[0]))
        name_array.sort()
    # print(name_array)
    # exit()
    for index, filename in enumerate(name_array):
        # print(filename)
        
        img = cv2.imread('/data2/NewDataset/' + subject + '/' + 'all_pictures/' + str(filename) + '.jpg')
        height, width, layers = img.shape
        size = (width,height)
        img_array.append(img)
        # print(filename.split('/')[-1].split('.')[0])
        # exit()
    
    out = cv2.VideoWriter(subject + '.avi',cv2.VideoWriter_fourcc(*'DIVX'), 20, size)
    
    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()
