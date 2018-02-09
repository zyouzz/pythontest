import PIL.Image as Image
import PIL.ImageDraw as ImageDraw
import PIL.ImageFont as ImageFont


class postMaker(object):
    def __init__(self, backImg, font):
        self.backImg = backImg
        self.font = font
        self.post = None

    def create(self, userIcon, userName, qrImg, textColor):

        try:
            backImg = Image.open(self.backImg)
            userIcon = Image.open(userIcon)
            font = ImageFont.truetype(self.font, 30)

            userIcon.thumbnail((88, 88))
            backImg.paste(userIcon, (316, 242))

            draw = ImageDraw.Draw(backImg)
            draw.ink = textColor.get('R', 0) + textColor.get('G', 0) * 256 + textColor.get('B', 0) * 256 * 256
            textWidth, textHeight = font.getsize(userName)
            draw.text([360 - textWidth / 2, 335], userName, font=font)

            qrImg = Image.open(qrImg)
            qrImg.thumbnail((142, 142))
            backImg.paste(qrImg, (191, 946))

            self.post = backImg
            backImg.save("testPost.jpg", "jpeg")
        except Exception as e:
            print repr(e)


if __name__ == '__main__':
    backImg = r"C:\Users\Esri\Desktop\20170815112219.jpg"
    font = r"C:\Users\Esri\Desktop\msyhl.ttc"
    pMaker = postMaker(backImg=backImg, font=font)
    userIcon = r'C:\Users\Esri\Desktop\qrimg.jpg'
    qrImg = r'C:\Users\Esri\Desktop\qrimg.jpg'
    pMaker.create(
        userIcon=userIcon,
        userName=U"sasfda",
        qrImg=qrImg,
        textColor={'R': 0, 'G': 0, 'B': 0})
    print 'ok'