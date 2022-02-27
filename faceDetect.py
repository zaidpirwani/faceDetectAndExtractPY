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
        # Draw rectangle around the faces
        padding=0.2 #percentage padding
        if len(faces)==0:
            csvwriter.writerow([imageFileName,'NO FACE FOUND'])
            print(row[0], ": NO FACES FOUND")
        else:
            rowToWrite = []
            rowToWrite.append(imageFileName)
            a=0
            for (x, y, w, h) in faces:
                #y1 = 0 if int(y-(h*padding))  <0 else int(y-(h*padding))
                #y2 = h if int(y+h+(h*padding))>h else int(y+h+(h*padding))
                #x1 = 0 if int(x-(w*padding))  <0 else int(x-(w*padding))
                #x2 = w if int(x+w+(w*padding))>w else int(x+w+(w*padding))
                y1 = y
                y2 = y+h
                x1 = x
                x2 = x+w
                print (y1, ", ", y2, ", ", x1, ", ", x2)
                roi = img[y1:y2,x1:x2]
                if a>0:
                    break #outFileName = os.getcwd() + '/output/' + str(a) + row[0]
                else:
                    outFileName = os.getcwd() + '/output/' + row[0]
                cv2.imwrite(outFileName, roi)
                rowToWrite.append(outFileName)
                print("SAVED IMAGE: " + outFileName)
                a=a+1
            csvwriter.writerow(rowToWrite)
