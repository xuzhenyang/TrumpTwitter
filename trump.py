# encoding: utf-8

from PIL import Image,ImageDraw,ImageFont
from sys import argv

try:
    language = argv[1]
    text = argv[2]
    ttfont = ''
except Exception,e:
    print "参数不正确"
    print "eg. python trump.py -e/-c \"hello world\""
    exit()

if language == '-e':
    # English use this font
    ttfont = ImageFont.truetype('C:\Windows\Fonts\Helvetica Neue.ttf', 16)
elif language == '-c':
    # 中文用这个字体
    ttfont = ImageFont.truetype('C:\Windows\Fonts\msyhl.ttc', 16)
else:
    print "参数不正确"
    print "eg. python trump.py -e/-c \"hello world\""
    exit()

image = Image.open("trump.jpg")
draw = ImageDraw.Draw(image)

draw.text((72,30),unicode(text), fill=(41,47,51),font=ttfont)

image.save('test.jpg', 'jpeg')