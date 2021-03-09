import cv2
import os


subjects = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24',
            '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50']
actions = ['walk', 'hand', 'run', 'jump']
modes = ['train', 'test']


for subject in subjects:
  path = '/home/culiver/Edwin/pytorch_segmentation/images/' + subject + '/'
  if not os.path.isdir(path):
    os.mkdir(path)
  

  for action in actions:
    path = '/home/culiver/Edwin/pytorch_segmentation/images/' + subject + '/' + action + '/'
    if not os.path.isdir(path):
      os.mkdir(path)
    
    
    for mode in modes:
      path = '/home/culiver/Edwin/pytorch_segmentation/images/' + subject + '/' + action + '/' + mode + '/'
      if not os.path.isdir(path):
        os.mkdir(path)
      
      
      
      path = '/data2/lab50_dataset/' + subject + '/' + action + '/'
      os.chdir(path)
      vidcap = cv2.VideoCapture('video_lab_5G_220_' + subject + '_' + action + '_' + mode + '.avi')
      success,image = vidcap.read()
      count = 0


      os.chdir('/home/culiver/Edwin/pytorch_segmentation/images/' + subject + '/' + action + '/' + mode + '/')
      while success:

        cv2.imwrite("%d.jpg" % count, image)     # save frame as JPEG file
        success,image = vidcap.read()
        count+=1

