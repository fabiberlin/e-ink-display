import epd7in5
import Image
import ImageDraw
import ImageFont
import matplotlib.pyplot as plt
import matplotlib.image as mpimg



EPD_WIDTH = 640
EPD_HEIGHT = 384

def main():
    epd = epd7in5.EPD()
    epd.init()
    print "init done"

    image = Image.new('1', (EPD_WIDTH, EPD_HEIGHT), 1)    # 1: clear the frame
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', 24)
    draw.rectangle((0, 6, 640, 30), fill = 0)
    draw.text((200, 10), 'e-Paper demo', font = font, fill = 255)
    draw.rectangle((200, 80, 600, 280), fill = 0)
    draw.arc((240, 120, 580, 220), 0, 360, fill = 255)
    draw.rectangle((0, 80, 160, 280), fill = 255)
    draw.arc((40, 80, 180, 220), 0, 360, fill = 0)
    imgplot = plt.imshow(image)
    #plt.ion()
    plt.show()
    raw_input()
    #epd.display_frame(epd.get_frame_buffer(image))
    
    print "exit"

if __name__ == '__main__':
    main()
