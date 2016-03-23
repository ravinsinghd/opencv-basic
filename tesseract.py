import subprocess
print('processed image')
test = subprocess.Popen(["tesseract","adoThres.png","out"], stdout=subprocess.PIPE)
test.communicate()[0]
f = open("out.txt")
print(f.read().strip())
print('processed & resized image')
test = subprocess.Popen(["tesseract","extrabigresized.png","out"], stdout=subprocess.PIPE)
test.communicate()[0]
f = open("out.txt")
print(f.read().strip())


