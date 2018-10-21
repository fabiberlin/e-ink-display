import logging

from PanelBase import PanelBase
import matplotlib.pyplot as plt

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)


class DebugPanel(PanelBase):

    def __init__(self):
        logger.info("init")
        PanelBase.__init__(self)

    def drawAtCanvas(self):
        logger.debug("draw")
        imgplot = plt.imshow(self.image)
        plt.show()
