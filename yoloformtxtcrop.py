from PIL import Image
import os
import numpy as np

path_dir = 'C:/Users/HHES/Downloads/korail_data_yolo_form/korail_data_yolo_form/imgs/'
 
file_list = os.listdir(path_dir)

for file_name in file_list:
    if file_name[-4:]=='.jpg':
        try:
            imagei = Image.open(path_dir+file_name)
            imagewidth = imagei.size[0]
            imageheight = imagei.size[1]
            label = open(path_dir+file_name[:-4]+'.txt', 'r')
            i=0
            while True:
                line = label.readline()
                if not line: break
                classname, xcenter, ycenter, width, height  = line.split()
                imageicropped = imagei.crop((imagewidth*float(xcenter)-(imagewidth*float(width)/2), imageheight*float(ycenter)-(imageheight*float(height)/2), imagewidth*float(xcenter)+(imagewidth*float(width)/2), imageheight*float(ycenter)+(imageheight*float(height)/2)))
                if not os.path.exists(path_dir+"croppedimage/train/"):
                    os.makedirs(path_dir+"croppedimage/train/")
                if not os.path.exists(path_dir+"croppedimage/test/"):
                    os.makedirs(path_dir+"croppedimage/test/")
                n = np.random.randint(1,10)
                if n==9:
                    imageicropped.save(path_dir+"croppedimage/test/"+file_name[:-4]+"_"+str(i)+".jpg")
                else:
                    imageicropped.save(path_dir+"croppedimage/train/"+file_name[:-4]+"_"+str(i)+".jpg")

                
                
                print(file_name[:-4]+str(i)+".jpg"+' done')
                i+=1
            label.close()
        except:
            print("Error with "+ file_name)

            
        
print('done')