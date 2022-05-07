import cv2
import numpy as np

cam = cv2.VideoCapture('Lane Detection Test Video 01.mp4')

while True:
    ret,frame=cam.read()

    if ret is False:
        break
    # #ex1
    # print(frame.shape)
    # cv2.imshow('Original',frame)

    #ex2
    resize=cv2.resize(frame,(int(frame.shape[1]/4),int(frame.shape[0]/4)))
    cv2.imshow('Small',resize)

    #ex3
    colored = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    colo=cv2.resize(colored,(int(frame.shape[1]/4),int(frame.shape[0]/4)))
    cv2.imshow('Gray', colo)

    #ex4
    frame_in_which_to_draw = np.zeros((frame.shape[0], frame.shape[1]), np.uint8)

    upper_left=(int(frame.shape[1]*0.53),int(frame.shape[0]*0.78))
    upper_right=(int(frame.shape[1]*0.46),int(frame.shape[0]*0.78))
    lower_left=(int(frame.shape[1]*0.46),int(frame.shape[0]))
    lower_right=(int(frame.shape[1]),int(frame.shape[0]))

    points_of_a_polygon=np.array([upper_left,upper_right,lower_left,lower_right],dtype=np.int32)
    trap=cv2.fillConvexPoly(frame_in_which_to_draw,points_of_a_polygon,1)

    trapez=cv2.resize(trap,(int(frame.shape[1]/4),int(frame.shape[0]/4)))
    cv2.imshow('Trapezoid',trapez*255)

    image=colored*trap
    road=cv2.resize(image,(int(frame.shape[1]/4),int(frame.shape[0]/4)))
    cv2.imshow('Road',road)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
