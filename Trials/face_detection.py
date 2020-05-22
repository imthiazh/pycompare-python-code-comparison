import cv2
class face:
    def __init__(self):
        self.cascade=cv2.CascadeClassifier('faces.xml')
        self.x=None
        self.y=None
        self.w=None
        self.h=None

    def detectFace(self,img):
        cropped=None
        grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=self.cascade.detectMultiScale(grey,1.3,5)
        cropped=[]
        coor=[]
        for (self.x,self.y,self.w,self.h) in faces:
            cropped.append(img[self.y:self.y+self.h,self.x:self.x+self.w])
            coor.append([self.x,self.y,self.w,self.h])
        return cropped,coor
    #start faceDetection.py
    def detect(filename):
        eye_cascade = cv2.CascadeClassifier(
            'C:\\Users\\Abhishek\\Anaconda3\\pkgs\\libopencv-3.4.1-h875b8b8_3\\Library\\etc\\haarcascades\\haarcascade_eye.xml')
        face_cascade = cv2.CascadeClassifier(
            'C:\\Users\\Abhishek\\Anaconda3\\pkgs\\libopencv-3.4.1-h875b8b8_3\\Library\\etc\\haarcascades\\haarcascade_frontalface_default.xml')
        img = cv2.imread(filename)
        #inside detect
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 3)
            for ex, ey, ew, eh in eyes:
                cv2.rectangle(img[y:y + h, x:x + w], (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
        cv2.imshow("sample", img)
        cv2.waitKey(0)
        #end