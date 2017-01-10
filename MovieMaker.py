import numpy;
import cv2

fourcc = cv2.VideoWriter_fourcc(*"H264")
fps = 30
width = 1024
height = 1024
frameCount = 900

writer = cv2.VideoWriter("movie.mp4", fourcc, fps, (width, height))

for i in range(1, frameCount):
    print("src\\screen-{0:05d}.png".format(i))
    img = cv2.imread("src\\screen-{0:05d}.png".format(i))
    writer.write(img)
   