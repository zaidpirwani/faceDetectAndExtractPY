import os
import csv
import cv2
import sys

if __name__ == "__main__":
    if len(sys.argv)!=2:
        sys.exit("argument error, usafe, python faceDetect.py CSVFILE.csv")
    file = open(sys.argv[1]) #csv file name after faceDetect.py
    csvreader = csv.reader(file)
    outfile = open('output/out_'+sys.argv[1], 'a')
    csvwriter = csv.writer(outfile)

    # Load the cascade
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    for row in csvreader:
        imageFileName = os.getcwd()+'/images/'+row[0]
        print('FILENAME WITH PATH:' + imageFileName)
        # Read the input image
        img = cv2.imread(imageFileName)
        if img is None:
            csvwriter.writerow([imageFileName,'CANNOT READ IMAGE'])
            print(row[0], ": CANNOT READ IMAGE")
            continue
        # Convert into grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Detect faces
        faces = face_cascade.detectMultiScale(gray, 1.2, 5)

        padding=0.2 #percentage padding, TODO
        if len(faces)==0:
            csvwriter.writerow([imageFileName,'NO FACE FOUND'])
            print(row[0], ": NO FACES FOUND")
        else:
            rowToWrite = []
            rowToWrite.append(imageFileName)
            largestFace = 0
            area = 0
            i=0
            for (x, y, w, h) in faces:
                if (w*h)>area:
                    area=w*h
                    largestFace = i
                i = i+1
                #y1 = 0 if int(y-(h*padding))  <0 else int(y-(h*padding))
                #y2 = h if int(y+h+(h*padding))>h else int(y+h+(h*padding))
                #x1 = 0 if int(x-(w*padding))  <0 else int(x-(w*padding))
                #x2 = w if int(x+w+(w*padding))>w else int(x+w+(w*padding))
            (x,y,w,h) = faces[largestFace]
            y1 = y
            y2 = y+h
            x1 = x
            x2 = x+w
            print (y1, ", ", y2, ", ", x1, ", ", x2)
            roi = img[y1:y2,x1:x2]
            outFileName = os.getcwd() + '/output/' + row[0]
            cv2.imwrite(outFileName, roi)
            rowToWrite.append(outFileName)
            print("SAVED IMAGE: " + outFileName)
            csvwriter.writerow(rowToWrite)
