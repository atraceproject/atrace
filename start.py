import sys, os, glob, platform

fo = open("defaultscss/app.scss")
foc = fo.read()
fo.close()

def copyappscss():
    f = open("scss/app.scss", 'w')
    f.write(foc)
    f.close()

os.system("mkdir "+sys.argv[1])
org = os.getcwd()

os.chdir(sys.argv[1])

def mkdir(directory):
    os.system("mkdir "+directory)

def cp(o,t):
    if platform.system() == "Windows":
        os.system("copy "+"\""+o+"\""+" "+t)

mkdir("scss")

copyappscss()

for fn in glob.glob("C:\\Users\\Danielle\\atrace\\defaults"):
    cp(os.path.join("C:\\Users\\Danielle\\atrace\\defaults\\", fn), os.getcwd())

os.system("npm install")

os.chdir(org)
