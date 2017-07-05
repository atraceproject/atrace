import sys, os, glob

os.system("sass "+os.path.join(sys.argv[1], os.path.join("scss", "app.scss"))+":"+os.path.join(sys.argv[1], os.path.join("www", "app.css")))

org = os.getcwd()
os.chdir(sys.argv[1])
os.system("npm start")
os.chdir(org)
exit()
