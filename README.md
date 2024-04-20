# faceDetectAndExtractPY
a simply python script todetect and extract FACE from images - to generate ID Card images automatically

all images should be in images folder

output images are saved in OUTPUT folder

image data to be provided via a CSV file, with only image names in row, single column, no header

image name should NOT contain any space

this is a SIMPLE Script, no error checking, csv file checking, image file exists, face going out of image dimensions or anything done.

SHARING for personal record and archive

UPDATE: 14 October
New argument to run
usage:
python3 faceDetect.py CSVFILE.csv FOLDER_NAME_WHERE_IMAGES width_padding heightpadding
width padding and height padding is uniform and in percentage, but use INTs


UPDATE: 20 April 2024
running again, on UBunt 22.04
AWS, EC2, Large
commands ran / log and process
sudo apt update
udo apt upgrade
sudo apt install python3-opencv
git clone https://github.com/zaidpirwani/faceDetectAndExtractPY
sudo apt install unzip
uploaded zip files of image folders via WinSCP
uploaded csv file of image folders with single row of image names only - no header
mkdir output
mkdir output/g8-image
csv file: g8.csv
folder-name: g8-image

python3 faceDetect.py g8.csv g8-image 20 20



ZAID PIRWANI
