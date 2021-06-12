import os, argparse, sys

parser = argparse.ArgumentParser(prog='Unsplash Python Wallpaper')
parser.add_argument('-m', help='change wallpaper every M minutes', default=5, type=int, choices=range(1, 59))
args = parser.parse_args()
M = vars(args)['m']
# print(vars(args)['m'])

python_exec = sys.executable

if not os.path.exists(os.environ['HOME'] + "/.python-wallpaper-unsplash"):
    os.makedirs(os.environ['HOME'] + "/.python-wallpaper-unsplash") 

os.system('cp ./wallpaper.py $HOME/.python-wallpaper-unsplash/wallpaper.py')

command = '{ crontab -l; echo "*/' + str(M) + ' * * * * cd $HOME/.python-wallpaper-unsplash/ && '+ python_exec +' wallpaper.py && cd - >> /dev/null 2>&1"; } | crontab -' 

os.system(command)