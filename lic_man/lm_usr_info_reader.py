# -*- coding: utf-8 -*-
"""用户信息读取模块
收集软件许可证申请所需要的主机的硬件信息和用户信息.
 - 用于安装本产品的Windows主机的硬件信息
 - 用户信息

Usage:
    - 在用户的Windows主机上运行该模块
    - 输入用户名称

Author: Lei Wang
Date: April 10, 2024
"""


__author__ = "王磊"
__copyright__ = "Copyright 2024 四川科莫生医疗科技有限公司"
__credits__ = ["王磊"]
__maintainer__ = "王磊"
__email__ = "lei.wang@kemoshen.com"
__version__ = "0.0.1"
__status__ = "Development"


import json

from lm_comm_lib import get_cpu_info_str, get_first_mac_address, get_bios_serial_number


if __name__ == "__main__":

    usr_name = input("请输入许可证注册使用的用户名称:")

    # 拼接信息
    usr_info = {
        "cpu_info": get_cpu_info_str(),
        "mac_addr": get_first_mac_address(),
        "bios_sn": get_bios_serial_number(),
        "usr_name": usr_name
    }
    print(usr_info)
    with open("usr_info.uis", "w", encoding="utf-8") as f:
        json.dump(usr_info, f)
