import cv2


i = 32

while i < 38:
    img = cv2.imread(f'kite{i}.jpg')
    img_scale = cv2.resize(img, (640, 640))

    cv2.imwrite(f'kite{i}.jpg', img_scale)



    i = i+1

print('Done')