import logging
import os

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)


class PanelBase:

    def __init__(self):
        logger.info("init")
        self.WIDTH = 640
        self.HEIGHT = 384

        self.image = Image.new('1', (self.WIDTH, self.HEIGHT), 1)  # 1: clear the frame
        self.draw = ImageDraw.Draw(self.image)
        script_dir = os.path.dirname(__file__)
        font_file_path = os.path.join(script_dir, 'font', 'FreeMonoBold.ttf')
        logger.debug("File Path for Typo")
        logger.debug(font_file_path)
        self.font = ImageFont.truetype(font_file_path, 24)

    def gather_information(self):
        pass

    def arrange(self):
        logger.info("arrange")
        self.draw.rectangle((0, 6, 640, 30), fill=0)
        self.draw.text((200, 10), 'e-Paper demo', font=self.font, fill=255)
        self.draw.rectangle((200, 80, 600, 280), fill=0)
        self.draw.arc((240, 120, 580, 220), 0, 360, fill=255)
        self.draw.rectangle((0, 80, 160, 280), fill=255)
        self.draw.arc((40, 80, 180, 220), 0, 360, fill=0)

    def drawAtCanvas(self):
        logger.debug("draw")
