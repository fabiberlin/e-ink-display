from PanelBase import PanelBase
import epd7in5


class EinkPanel(PanelBase):

    def __init__(self):
        PanelBase.__init__(self)
        # epd = epd7in5.EPD()
        # epd.init()

    def drawAtCanvas(self):
        # epd.display_frame(epd.get_frame_buffer(image))
        pass
