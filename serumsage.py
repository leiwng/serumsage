# -*- coding: utf-8 -*-
"""The Main Module of SerumSage(Serum Indices Interpretation)

Author: Lei Wang
Date: April 24, 2024
"""

__author__ = "王磊"
__copyright__ = "Copyright 2023 四川科莫生医疗科技有限公司"
__credits__ = ["王磊"]
__maintainer__ = "王磊"
__email__ = "lei.wang@kemoshen.com"
__version__ = "0.0.1"
__status__ = "Development"


import sys

from new_world import new_world
from logger import log


if __name__ == "__main__":
    success, result_or_app = new_world()

    if not success:
        # print(result_or_app)
        log.error(result_or_app)
        sys.exit(-1)

    sys.exit(result_or_app.exec_())
