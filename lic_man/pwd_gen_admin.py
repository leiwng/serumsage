# -*- coding: utf-8 -*-
"""设置管理员密码

Usage:
    - 在授权安装本产品的用户主机上运行
    - 验证用户的许可证是否有效
    - 验证公司产品主密码后,设置管理员密码

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

from lm_comm_lib import verify_password_sign, verify_password, generate_password_hash, verify_license


if __name__ == "__main__":

    # 读取公司公钥
    # 判断公司公钥是否存在
    public_key_fp = "kms_serumsage_public_key.pem"
    if not os.path.exists(public_key_fp):
        print("公钥不存在")
        sys.exit(1)

    # 验证用户的许可证是否有效
    license_fp = "license.lic"
    if not os.path.exists(license_fp):
        print("许可证文件不存在")
        sys.exit(1)

    encoding = "utf-8"
    result, msg, usr_name, expiry_date = verify_license(license_fp, encoding, public_key_fp)
    if not result:
        print(msg)
        sys.exit(1)

    # 验证公司产品主密码签名
    # 判断主密码签名hash文件是否存在
    master_pwd_hash_sign_fp = "master_pwd.hash.sign"
    if not os.path.exists(master_pwd_hash_sign_fp):
        print("主密码签名文件不存在")
        sys.exit(1)
    # 验证公司产品主密码签名
    result, master_pwd_hash = verify_password_sign(public_key_fp, master_pwd_hash_sign_fp)
    if not result:
        print("主密码签名验证失败.")
        sys.exit(1)

    # 输入主密码
    master_pwd = input("请输入主密码:")
    # 检查输入的主密码是否由英文ASCII数字、字母和标点组成
    if not master_pwd.isascii():
        print("主密码只能由英文ASCII数字、字母和标点组成")
        sys.exit(1)
    # 检查输入的主密码长度是否在8到32之间
    if not 8 <= len(master_pwd) <= 32:
        print("主密码长度必须在8到32之间")
        sys.exit(1)

    # 验证输入的密码是否为主密码
    if not verify_password(master_pwd_hash, master_pwd):
        print("输入密码同公司产品主密码不符,退出.")
        sys.exit(1)

    # 输入管理员密码
    admin_pwd = input("请输入管理员密码:")
    # 检查输入的主密码是否由英文ASCII数字、字母和标点组成
    if not admin_pwd.isascii():
        print("管理员密码只能由英文ASCII数字、字母和标点组成")
        sys.exit(1)
    # 检查输入的主密码长度是否在8到32之间
    if not 8 <= len(admin_pwd) <= 32:
        print("管理员密码长度必须在8到32之间")
        sys.exit(1)

    # 将密码转换为散列字节
    admin_pwd_hash = generate_password_hash(admin_pwd)

    # 将master密码hash的长度,master密码hash,管理员密码hash写入文件
    admin_pwd_hash_fp = "admin_pwd.hash.sign"
    with open(admin_pwd_hash_fp, 'wb') as f:
        # 写入master密码hash的长度
        f.write(len(master_pwd_hash).to_bytes(4, byteorder='big'))
        # 写入master密码hash
        f.write(master_pwd_hash)
        # 写入管理员密码hash
        f.write(admin_pwd_hash)