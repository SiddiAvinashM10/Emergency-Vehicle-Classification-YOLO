import cv2
from darkflow.net.build import TFNet
import numpy as np
import time

options = {
    'model' : 'cfg/yolov2-tiny-voc-4c.cfg',
    'load' : 1750,
    'threshold' : 0.2,
    'gpu' : 1.0
}

tfnet = TFNet(options)

capture = cv2.VideoCapture('vehicles5.mp4')
colors = [tuple(255 * np.random.rand(4)) for i in range(4)]

while (capture.isOpened()):
    stime = time.time()
    ret, frame = capture.read()
    if ret:
        results = tfnet.return_predict(frame)
        for color, result in zip(colors, results):
            tl = (result['topleft']['x'], result['topleft']['y'])
            br = (result['bottomright']['x'], result['bottomright']['y'])
            label = result['label']
            #confidence = result['confidence']
            text = '{}'.format(label)#, confidence * 100)
            frame = cv2.rectangle(frame, tl, br, color, 5)
            frame = cv2.putText(frame, text, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
        cv2.imshow('frame', frame)
        print('FPS {:.1f}'.format(1 / (time.time() - stime)))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        capture.release()
        cv2.destroyAllWindows()
        break