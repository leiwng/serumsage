import contextlib
from PIL import Image

def is_jpeg_completed(file_path):
    with contextlib.suppress(IOError, AttributeError, KeyError, IndexError):
        with Image.open(file_path) as img:
            exif_data = img._getexif()
            if exif_data and exif_data.get(0x8769):
                return True
    return False

# 示例用法
file_path = "path/to/image.jpg"
if is_jpeg_completed(file_path):
    print("JPEG 文件写入已完成")
else:
    print("JPEG 文件写入未完成")