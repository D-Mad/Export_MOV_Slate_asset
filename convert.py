
import sys
import nuke

root = nuke.root()
root['format'].setValue('HD_1080')
r = nuke.nodes.Read(file = sys.argv[1])
r['first'].setValue(1)
r['last'].setValue(72)

ts = nuke.loadToolset("./Slate_Lego.nk")
ts.setInput(0, r)
w = nuke.nodes.Write(file = sys.argv[2])

w['file_type'].setValue("mov")
w['colorspace'].setValue("sRGB")
w['mov64_codec'].setValue("h264")
w['create_directories'].setValue(True)
w.setInput(0, ts)
