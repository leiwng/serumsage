"""程序日志公共模块

Returns:
    _type_: _description_
"""

import os
import sys

from loguru import logger
# from pathlib import Path

logger.remove()  # 删去import logger之后自动产生的handler，不删除的话会出现重复输出的现象
handler_id = logger.add(sys.stderr, level="DEBUG")  # 添加一个可以修改控制的handler

# BasePath = Path(__file__).resolve().parent.parent
BasePath = os.path.dirname(os.path.abspath(__file__))
LogPath = os.path.join(BasePath, "logs")


class Logger:
    @staticmethod
    def log() -> logger:
        if not os.path.exists(LogPath):
            os.mkdir(LogPath)

        # 日志文件
        log_file = os.path.join(LogPath, "serumsage.log")

        # loguru日志
        # more: https://github.com/Delgan/loguru#ready-to-use-out-of-the-box-without-boilerplate
        # +----------------------+------------------------+------------------------+
        # | Level name           | Severity value         | Logger method          |
        # +======================+========================+========================+
        # | ``TRACE``            | 5                      | |logger.trace|         |
        # +----------------------+------------------------+------------------------+
        # | ``DEBUG``            | 10                     | |logger.debug|         |
        # +----------------------+------------------------+------------------------+
        # | ``INFO``             | 20                     | |logger.info|          |
        # +----------------------+------------------------+------------------------+
        # | ``SUCCESS``          | 25                     | |logger.success|       |
        # +----------------------+------------------------+------------------------+
        # | ``WARNING``          | 30                     | |logger.warning|       |
        # +----------------------+------------------------+------------------------+
        # | ``ERROR``            | 40                     | |logger.error|         |
        # +----------------------+------------------------+------------------------+
        # | ``CRITICAL``         | 50                     | |logger.critical|      |
        # +----------------------+------------------------+------------------------+
        logger.add(
            log_file,
            encoding="utf-8",
            level="INFO",
            rotation="01:00",  # 每天 0 点创建一个新日志文件
            retention="30 days",  # 定时自动清理文件
            enqueue=True,  # 异步安全
            backtrace=True,  # 错误跟踪
            diagnose=True,
        )

        return logger


log = Logger().log()
