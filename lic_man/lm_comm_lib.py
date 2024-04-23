# -*- coding: utf-8 -*-
"""许可证管理公共库

Author: Lei Wang
Date: April 17, 2024
"""


__author__ = "王磊"
__copyright__ = "Copyright 2024 四川科莫生医疗科技有限公司"
__credits__ = ["王磊"]
__maintainer__ = "王磊"
__email__ = "lei.wang@kemoshen.com"
__version__ = "0.0.1"
__status__ = "Development"


import json
import platform
import subprocess
from datetime import datetime


import bcrypt
# import netifaces
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend


def get_cpu_info_str():
    """获取CPU信息

    Returns:
        String: CPU信息
    """
    return platform.processor()


# def get_first_mac_address():
#     """获取第一个网卡的MAC地址

#     Returns:
#         String: 第一个网卡的MAC地址
#     """
#     for interface in netifaces.interfaces():
#         addrs = netifaces.ifaddresses(interface)
#         if netifaces.AF_LINK in addrs:
#             # 返回第一个找到的MAC地址
#             return addrs[netifaces.AF_LINK][0]['addr']
#     # 如果没有网卡返回公司缺省的MAC地址
#     return '8c:8c:08:18:80:66'


def get_cpu_serial_number():
    """获取CPU序列号

    Returns:
        String: CPU序列号
    """
    try:
        cpu_info = subprocess.check_output("wmic cpu get processorid", shell=True)
        return cpu_info.decode().split('\n')[1].strip()
    except Exception as e:
        # 遇异常，返回公司缺省的CPU序列号
        print(e)
        return 'BFEBFBFF08188066'


def get_csp_uuid():
    """获取系统序列号CSP UUID, 主板识别码
    微软的 CSP UUID (Cryptographic Service Provider Universally Unique Identifier) 是一个针对 Windows 平台的独特标识符，它是通过主板上的 TPM(Trusted Platform Module)芯片生成的，因此与硬件相关且无法轻易修改。

    Returns:
        String: 系统序列号
    """
    try:
        csp_uuid = subprocess.check_output("wmic csproduct get uuid", shell=True)
        return csp_uuid.decode().split('\n')[1].strip()
    except Exception as e:
        # 遇异常，返回公司缺省的系统序列号
        print(e)
        return '969C6349-390E-11EB-80E9-8C8C08188066'


def get_bios_serial_number():
    """获取BIOS序列号

    Returns:
        String: BIOS序列号
    """
    try:
        bios_info = subprocess.check_output("wmic bios get serialnumber", shell=True)
        return bios_info.decode().split('\n')[1].strip()
    except Exception as e:
        # 遇异常，返回公司缺省的BIOS串号
        print(e)
        return 'KMSSS0ZQ'


def load_private_key(private_key_fp):
    """加载PEM格式的私钥文件

    Args:
        private_key_fp (String): 私钥文件路径

    Returns:
        private_key: 私钥对象
    """
    with open(private_key_fp, "rb") as f:
        private_key = serialization.load_pem_private_key(
            f.read(),
            password=None,
            backend=default_backend()
        )
    return private_key


def load_public_key(public_key_fp):
    """加载PEM格式的公钥文件

    Args:
        public_key_fp (String): 公钥文件路径

    Returns:
        public_key: 公钥对象
    """
    with open(public_key_fp, "rb") as f:
        public_key = serialization.load_pem_public_key(
            f.read(),
            backend=default_backend()
        )
    return public_key


def load_password_hash_sign(password_hash_sign_fp):
    """加载密码hash的签名文件

    Args:
        password_hash_sign_fp (String): 密码hash的签名文件路径

    Returns:
        bytes: 公司产品主密码的hash散列信息
        bytes: 公司产品主密码的签名信息
    """
    # 读取密码签名文件
    with open(password_hash_sign_fp, 'rb') as f:
        # 读取主密码hash信息长度
        password_hash_len = int.from_bytes(f.read(4), byteorder='big')
        # 读取主密码hash信息
        password_hash = f.read(password_hash_len)
        # 读取主密码签名
        password_hash_sign = f.read()

    return password_hash, password_hash_sign


def verify_password_sign(public_key_fp, password_hash_sign_fp):
    """验证密码签名
    Args:
        public_key_fp (String): 公钥文件路径
        password_hash_sign_fp (String): 密码hash的签名文件路径

    Prerequisites(前提):
        - 密码hash的签名文件是二进制文件
        - 密码hash是bcrypt散列
        - 密码hash的签名文件有三部分: 1).4个字节的密码hash长度, 2).密码hash, 3).密码签名
        - 公钥是PEM格式的文件且存在
        - 密码hash文件存在

    Returns:
        Boolean: 公司产品主密码是否有效
        bytes: 公司产品主密码的hash散列信息
    """

    # 读取密码签名文件
    password_hash, password_hash_sign = load_password_hash_sign(password_hash_sign_fp)

    # 读取公钥
    public_key = load_public_key(public_key_fp)

    # 验证密码签名
    try:
        public_key.verify(
            password_hash_sign,
            password_hash,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
    except InvalidSignature:
        return False, None

    return True, password_hash


def verify_password(stored_hash, provided_password):
    """验证输入的密码字串是否正确
    Args:
        stored_hash (bytes): 主密码的hash散列
        provided_password (String): 输入的主密码

    Returns:
        _type_: _description_
    """
    # 比较存储的散列和提供的密码的散列
    return bcrypt.checkpw(provided_password.encode('utf-8'), stored_hash)


def generate_password_hash(password):
    """将密码转换为字节，然后散列(HASH)

    Args:
        password (String): password inputted by user

    Returns:
        Hash Bytes: 密码的HASH
    """
    # 将密码转换为字节，然后散列
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password_bytes, salt)


def sign_data(private_key, data):
    """对字节数据进行签名

    Args:
        private_key (private_key): 加载后的private key对象(load_pem_private_key的返回值)
        data (bytes): 需要签名的数据

    Returns:
        bytes: 签名后的数据
    """
    return private_key.sign(
        data,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )


def verify_license(license_fp, encoding, public_key_fp):
    """验证许可证文件是否有效
        1. 验证许可证文件的签名
        2. 验证许可证信息是否有效(例如到期日期)
        3. 验证是否是当初注册使用的主机

    Args:
        license_fp (_type_): _description_
        encoding (_type_): _description_
        public_key_fp (_type_): _description_

    Returns:
        _type_: _description_
    """
    # 加载许可证文件
    with open(license_fp, "r", encoding=encoding) as f:
        license_data = json.load(f)

    license_info = license_data["license_info"]
    signature = bytes.fromhex(license_data["signature"])

    # 验证硬件信息是否是本机
    # 验证CPU信息
    if license_info["cpu_info"] != get_cpu_info_str():
        # print("CPU信息不匹配。")
        return False, "硬件信息不匹配(C)", None, None
    # 验证MAC地址
    if license_info["csp_uuid"] != get_csp_uuid():
        # print("MAC地址不匹配。")
        return False, "硬件信息不匹配(M)", None, None
    # 验证BIOS序列号
    if license_info["bios_sn"] != get_bios_serial_number():
        # print("BIOS序列号不匹配。")
        return False, "硬件信息不匹配(B)", None, None

    # 读取public key
    with open(public_key_fp, "rb") as f:
        public_key = serialization.load_pem_public_key(
            f.read(),
            backend=default_backend()
        )
    # 验证签名
    try:
        public_key.verify(
            signature,
            json.dumps(license_info).encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        # print("许可证签名验证成功。")
    except InvalidSignature:
        # print("许可证签名验证失败。")
        return False, "许可证签名验证失败", None, None

    # 验证许可证信息，例如到期日期
    expiry_date = datetime.fromisoformat(license_info["expiry_date"])
    if datetime.now() > expiry_date:
        # print("许可证已过期。")
        return False, "许可证已过期", None, None
    else:
        # print("许可证有效。")
        return True, "许可证有效", license_info["usr_name"], license_info["expiry_date"]


def verify_admin_password(public_key_fp, admin_pwd_hash_sign_fp, master_pwd_hash_sign_fp, admin_pwd):
    """验证管理员密码

    Args:
        admin_pwd_hash_fp (String): 管理员密码hash文件路径
        master_pwd_hash_sign_fp (String): 公司产品主密码的签名文件路径
        admin_pwd (String): 管理员密码

    Returns:
        Boolean: 管理员密码是否有效
    """
    # 读取管理员密码hash
    master_hash_in_admin, admin_hash = load_password_hash_sign(admin_pwd_hash_sign_fp)
    # 验证主密码签名
    result, master_hash_in_master = verify_password_sign(public_key_fp, master_pwd_hash_sign_fp)
    if not result:
        return False, "主密码签名验证失败"
    # 验证主密码是否一致
    if master_hash_in_admin != master_hash_in_master:
        return False, "管理员密码验证失败(D)"
    # 验证管理员密码
    if not verify_password(admin_hash, admin_pwd):
        return False, "管理员密码验证失败(P)"
    return True, "管理员密码验证成功"