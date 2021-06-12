from PIL import Image
import urllib.request
import subprocess, os, datetime, random

x = datetime.datetime.now()
folder_name = x.strftime("%Y-%m-%d")
file_name = x.strftime("%H-%M-%S")
if not os.path.exists("./images/" + folder_name):
    os.makedirs("./images/" + folder_name) 

relative_image_path = './images/' + folder_name + '/' + file_name + '.jpg'

categories = ['city', 'car', 'architecture', 'travel']

URL = 'https://source.unsplash.com/random/1920x1080/?' + random.choice(categories)

with urllib.request.urlopen(URL) as url:
    with open(relative_image_path, 'wb') as f:
        f.write(url.read())

command = 'gsettings set org.gnome.desktop.background picture-uri "file://' + os.environ['HOME'] + '/.python-wallpaper-unsplash/' + relative_image_path + '"'
subprocess.run(command.split(' '))
