import subprocess
test = subprocess.Popen(["tesseract","text.png","out"], stdout=subprocess.PIPE)
test.communicate()[0]
f = open("out.txt")
print('Normal Image')
print(f.read().strip())
print('processed image')
test = subprocess.Popen(["tesseract","adoThres.png","out"], stdout=subprocess.PIPE)
test.communicate()[0]
f = open("out.txt")
print(f.read().strip())


