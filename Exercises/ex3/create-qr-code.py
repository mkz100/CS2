import pyqrcode
import png

import sys

print("--- 命令行参数:", sys.argv)
if len(sys.argv) < 2:
    # expect 2 arguments
    print(f"用法: {sys.argv[0]} my-msg")
    exit(1)

msg = sys.argv[1]

qrcode = pyqrcode.create(msg)

qrcode.png("msg.png", scale=8)

print("--- 二维码已生成: msg.png")

