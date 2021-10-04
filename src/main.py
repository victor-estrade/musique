# -*- coding: utf-8 -*-
import logging

from .partition import Partition
from .loader import load_situation


def main():
    logger = logging.getLogger(__name__)
    logger.info("Hello world !")

    sit_1 = load_situation(1)
    print(sit_1)
    part_1 = Partition.from_situation(sit_1)
    print(part_1)





if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    main()
