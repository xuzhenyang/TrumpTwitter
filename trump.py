# encoding: utf-8

from PIL import Image,ImageDraw,ImageFont  

# English use this font
# ttfont = ImageFont.truetype('C:\Windows\Fonts\Helvetica Neue.ttf', 16)
# 中文用这个字体
ttfont = ImageFont.truetype('C:\Windows\Fonts\msyhl.ttc', 16)

image = Image.open("trump.jpg")
draw = ImageDraw.Draw(image)

draw.text((72,30),u'test', fill=(41,47,51),font=ttfont)

image.save('test.jpg', 'jpeg')