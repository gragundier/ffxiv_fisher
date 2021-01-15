import cv2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--dir", type=str, default="/home/gragundier/Videos/ffxiv_fisher", help="directory to find video in")
parser.add_argument("--video", type=str, default="sample1", help="video to extract from")
parser.add_argument("--limit", type=int, default=5000, help="photo limit")

args = parser.parse_args()

# Opens the Video file
cap= cv2.VideoCapture('{}/{}.mkv'.format(args.dir, args.video))
i=0
while(cap.isOpened() and i<args.limit):
    ret, frame = cap.read()
    if ret == False:
        break
    cv2.imwrite('{}/{}/{}_'.format(args.dir, args.video, args.video)+str(i)+'.png',frame)
    i+=1
 
cap.release()
cv2.destroyAllWindows()