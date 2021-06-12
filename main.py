from PIL import Image
import urllib.request
import subprocess, os, datetime, random


x = datetime.datetime.now()
folder_name = x.strftime("%Y-%m-%d")
file_name = x.strftime("%H-%M-%S")
root_path = os.environ['HOME'] + '/.python-wallpaper-unsplash'
if not os.path.exists(root_path + "/images/" + folder_name):
    os.makedirs(root_path + "/images/" + folder_name) 

image_path = os.environ['HOME'] + '/.python-wallpaper-unsplash/images/' + folder_name + '/' + file_name + '.jpg'

categories = ['city', 'car', 'architecture', 'travel']

URL = 'https://source.unsplash.com/random/1920x1080/?' + random.choice(categories)

with urllib.request.urlopen(URL) as url:
    with open(image_path, 'wb') as f:
        f.write(url.read())

g_path = os.popen('which gsettings').read()[:-1]
command = g_path + ' set org.gnome.desktop.background picture-uri "file://' +image_path + '"'
subprocess.run(command.split(' '))