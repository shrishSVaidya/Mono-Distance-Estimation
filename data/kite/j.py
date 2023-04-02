import os
import cv2

i=18

for file in os.listdir(os.getcwd()):
    if file.endswith('.jpeg') and file.startswith('single'):
        filename = os.path.join(os.getcwd(), file)
        print(filename)
        print(os.path.join(os.getcwd(), 'bird'+str(i)+'.jpg'))
        img = cv2.imread(filename)
        cv2.imwrite(os.path.join(os.getcwd(), 'bird'+str(i)+'.jpg'), img)
        os.remove(filename)
        # os.rename(filename, os.path.join(os.getcwd(), 'kite'+str(i)+'.jpg'))
        i = i+1