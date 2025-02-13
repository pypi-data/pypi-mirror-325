import sys
import argparse
import os
import time

from pytvpaint import george
from pytvpaint.project import Project

start = time.time()
print("start", start)

def process_remaining_args(args):
    parser = argparse.ArgumentParser(
        description='TVPaint Project Template Arguments'
    )
    parser.add_argument('--ref-path', dest='ref_path')
    parser.add_argument('--audio-path', dest='audio_path')
    parser.add_argument('--width', dest='width')
    parser.add_argument('--height', dest='height')

    values, _ = parser.parse_known_args(args)

    return (
        values.ref_path, values.audio_path, values.width, values.height
    )

print("HALF")
ref_path = process_remaining_args(sys.argv)[0]# .replace(".mov", "_HALF.mov")
print(ref_path)
print("exists", os.path.exists(ref_path))
AUDIO_PATH = process_remaining_args(sys.argv)[1]
print(AUDIO_PATH)
print("exists", os.path.exists(AUDIO_PATH))


CAMERA_WIDTH = process_remaining_args(sys.argv)[2]
print(CAMERA_WIDTH)
if CAMERA_WIDTH == 'None':
    project_width = 4240
else :
    project_width = float(CAMERA_WIDTH)

CAMERA_HEIGHT = process_remaining_args(sys.argv)[3]
print(CAMERA_HEIGHT)
if CAMERA_HEIGHT == 'None':
    project_height = 2385
else : 
    project_height = float(CAMERA_HEIGHT)

# change project resolution

print("get current project")
project = Project.current_project()
print(project)
clip = project.current_clip
camera = clip.camera

# project_width = camera_width+300
# project_height = camera_height+170

print("resizing to ",project_width,'x',project_height)
# project = project.resize(4240,2385,overwrite=True)
project = project.resize(project_width,project_height,overwrite=True)

project = Project.current_project()
# project = Project.new(r"C:\projets\2h14\_2h14\sq060\sh0160\layout\layout_tvpp\thomasthiebaut\sq060_sh0160_layout.tvpp")
print(project)
clip = project.current_clip
camera = clip.camera


print("set fps")
project.set_fps(25)
print(project)

print("set camera")
camera.get_point_data_at(0)
# george.tv_camera_set_point(0,2120,1192,0,scale=1)
george.tv_camera_set_point(0, project_width/2, project_height/2, 0, scale=1)

# -- import img sequence --

print("Loading", time.time() - start)
print("importing ref")
img_seq = clip.load_media(media_path=ref_path, with_name="[REF]", preload=True)
print("Loading done", time.time() - start)

# -- Import Audio --
print('importing audio')
if os.path.exists(AUDIO_PATH):
    audio = clip.add_sound(AUDIO_PATH)
    clip = project.current_clip
    print(clip)
    print('audio imported')
else : print('audio not found')



print("resize 2")
# project = project.resize(4240,2385,overwrite=True)
project = project.resize(project_width,project_height,overwrite=True)
project = Project.current_project()
# -- change img seq layer position
img_seq.position = 1
print("Saving", time.time() - start)
print(project)
print("saving")
# print(project.path) 
project.save_video_dependencies()
project.save_audio_dependencies()
project.save()
# george.tv_save_project()
print("importing closing")
project.close()
