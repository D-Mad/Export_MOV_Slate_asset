import cv2
import skvideo.io


capture=cv2.VideoCapture('/home/dev_ml/slate-python-opencv/lf_pr_guitarPaisleyGift_mod_review-turn_v006.mov') #open the default webcam
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
fps = int(capture.get(cv2.CAP_PROP_FPS))
x,y,w,h = 0,0,200,250 

font = cv2.FONT_HERSHEY_DUPLEX
outputfile = "test.mov"   #our output filename
writer = skvideo.io.FFmpegWriter(outputfile,inputdict={'-r': str(fps)}, outputdict={
  '-vcodec': 'libx264',  #use the h.264 codec
  '-crf': '0',           #set the constant rate factor to 0, which is lossless
  '-preset':'veryslow',
  '-r': str(fps),
  '-pix_fmt': "yuv420p",
  '-strict' :'-2',
  '-vf':'scale=1920:1120',
  
                                  #other options see https://trac.ffmpeg.org/wiki/Encode/H.264
}) 
while True:
    ret,frame=capture.read()
    cv2.putText(frame, 
                'BadClay', 
                (int(width-200),height-80), 
                font, 0.5, 
                (255, 255, 255), 
                1,
                cv2.LINE_AA
               )
    
    if ret==False:
        print("Bad frame")
        break
    imS = cv2.resize(frame, (960, 540))
    cv2.imshow('display',imS)
    writer.writeFrame(frame[:,:,::-1])  #write the frame as RGB not BGR
    ret=cv2.waitKey(10)
    if ret==27: #esc
        break

writer.close() #close the writer
capture.release()
cv2.destroyAllWindows()