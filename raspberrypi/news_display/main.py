import logging

from DebugPanel import DebugPanel

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)


def main():
    logger.info("Starting main.py")

    panel = DebugPanel()

    panel.gather_information()
    panel.arrange()
    panel.drawAtCanvas()


if __name__ == '__main__':
    main()
