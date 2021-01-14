import cv2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--video", type=str, default="01293907", help="video to extract from")

args = parser.parse_args()

# Opens the Video file
cap= cv2.VideoCapture('{}.mkv'.format(args.video))
i=0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    cv2.imwrite('/home/gragundier/Videos/ffxiv_timelapses/{}/{}_'.format(args.video, args.video)+str(i)+'.jpg',frame)
    i+=1
 
cap.release()
cv2.destroyAllWindows()