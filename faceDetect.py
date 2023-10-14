import os
import csv
import cv2
import sys

if __name__ == "__main__":
    if len(sys.argv)!=5:
        sys.exit("argument error, usage:python faceDetect.py CSVFILE.csv FOLDERNAME width_padding heightpadding")
    file = open(sys.argv[1]) #csv file name after faceDetect.py
    csvreader = csv.reader(file)
    outfile = open('output/out_'+sys.argv[1], 'a')
    csvwriter = csv.writer(outfile)
    wp = int(sys.argv[3])
    hp = int(sys.argv[4])
    folder = sys.argv[2]

    # Load the cascade
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    for row in csvreader:
        imageFileName = os.getcwd()+'/images/'+folder+'/'+row[0]
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

            (x,y,w,h) = faces[largestFace]
            # Calculate padding based on the face width and height
            padding_x = int(wp/100.0 * w)
            padding_y = int(hp/100.0 * h)

            # Adjust the coordinates for padding
            y1 = max(0, y - padding_y)
            y2 = min(img.shape[0], y + h + padding_y)
            x1 = max(0, x - padding_x)
            x2 = min(img.shape[1], x + w + padding_x)

            print (y1, ", ", y2, ", ", x1, ", ", x2)
            roi = img[y1:y2,x1:x2]
            outFileName = os.getcwd() + '/output/' + folder + '/' + row[0]
            cv2.imwrite(outFileName, roi)
            rowToWrite.append(outFileName)
            print("SAVED IMAGE: " + folder + '/' + outFileName)
            csvwriter.writerow(rowToWrite)
