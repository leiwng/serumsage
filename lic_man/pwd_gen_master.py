# -*- coding: utf-8 -*-
"""生成特定产品的master密码

Usage:
    - 命令行带上保存master密码hash文件的目录路径
    - 终端上输入公司产品主密码
    - 保存master密码hash签名到指定目录

Author: Lei Wang
Date: April 16, 2024
"""


__author__ = "王磊"
__copyright__ = "Copyright 2024 四川科莫生医疗科技有限公司"
__credits__ = ["王磊"]
__maintainer__ = "王磊"
__email__ = "lei.wang@kemoshen.com"
__version__ = "0.0.1"
__status__ = "Development"


import os
import sys

from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.backends import default_backend

from lm_comm_lib import generate_password_hash, sign_data


if __name__ == "__main__":
    # 检查命令行参数有2个
    if len(sys.argv) != 2:
        print("请在命令行中指定保存master password hash文件的目录路径")
        sys.exit(1)
    # 读取保存master password hash文件的目录路径
    # master password是针对不同的产品生成的，所以需要保存到对应产品的目录
    master_pwd_hash_bytes_save_dir = sys.argv[1]
    # 检查目录是否存在
    if not os.path.exists(master_pwd_hash_bytes_save_dir):
        print("指定的目录不存在")
        sys.exit(1)
    # 检查输入的路径是否是目录
    if not os.path.isdir(master_pwd_hash_bytes_save_dir):
        print("指定的路径不是目录")
        sys.exit(1)

    # 读取终端输入的公司产品主密码
    master_pwd = input("请输入主密码:")
    # 检查输入的主密码是否由英文ASCII数字、字母和标点组成
    if not master_pwd.isascii():
        print("主密码只能由英文ASCII数字、字母和标点组成")
        sys.exit(1)
    # 检查输入的主密码长度是否在8到32之间
    if not 8 <= len(master_pwd) <= 32:
        print("主密码长度必须在8到32之间")
        sys.exit(1)

    # 生成master密码hash
    master_pwd_hash_bytes = generate_password_hash(master_pwd)

    # 对master密码hash进行签名
    # 从当前目录下读入公司争对SerumSage的私钥
    if not os.path.exists("kms_serumsage_private_key.pem"):
        print("公司SerumSage产品私钥文件在当前目录下不存在")
        sys.exit(1)
    # 读取公司SerumSage产品私钥
    with open("kms_serumsage_private_key.pem", "rb") as f:
        private_key = load_pem_private_key(
            f.read(),
            password=None,
            backend=default_backend()
        )
    # 签名master密码hash
    signature = sign_data(private_key, master_pwd_hash_bytes)

    # 保存master密码hash签名到指定目录
    # 写入master密码hash的长度、master密码hash、master密码hash签名
    master_pwd_hash_bytes_signature_fp = os.path.join(master_pwd_hash_bytes_save_dir, "master_pwd.hash.sign")
    with open(master_pwd_hash_bytes_signature_fp, 'wb') as f:
        f.write(len(master_pwd_hash_bytes).to_bytes(4, byteorder='big'))
        f.write(master_pwd_hash_bytes)
        f.write(signature)

    # 保存master密码的明文到指定目录
    # 这个只能保存在公司服务上。
    master_pwd_fp = os.path.join(master_pwd_hash_bytes_save_dir, "master_pwd.txt")
    with open(master_pwd_fp, 'w', encoding='utf-8') as f:
        f.write(master_pwd)

