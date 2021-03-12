# 生成二维码

把你的英文名字和学生号生成一个二维码。 


## 应用场景

1. 生成网址的二维码, 扫描进入网站.
   
<img src="apple-url.png" alt="apple" width="200"/>


2. 生成二维码信息 : 文字编码

<img src="my-msg.png" alt="my-msg" width="200"/>


# Python库安装

用`pip`来安装这两个库:

* pip install pyqrcode
* pip install pypng

```
pip install pyqrcode

Collecting pyqrcode
  Downloading PyQRCode-1.2.1.zip (41 kB)
     |████████████████████████████████| 41 kB 968 kB/s 
Building wheels for collected packages: pyqrcode
  Building wheel for pyqrcode (setup.py) ... done
  Created wheel for pyqrcode: filename=PyQRCode-1.2.1-py3-none-any.whl size=36245 sha256=547dbb936d4ee2ad43361b595f40eebcb39ed6b8a0e7a484dbfbc65d9c96ce4d
  Stored in directory: /Users/kai/Library/Caches/pip/wheels/da/75/c0/38c7f82750de2725429b6b8571dca254249d73f6c882c5d9b1
Successfully built pyqrcode
Installing collected packages: pyqrcode
Successfully installed pyqrcode-1.2.1
```
```
pip install pypng

Collecting pypng
  Downloading pypng-0.0.20.tar.gz (649 kB)
     |████████████████████████████████| 649 kB 3.5 MB/s 
Building wheels for collected packages: pypng
  Building wheel for pypng (setup.py) ... done
  Created wheel for pypng: filename=pypng-0.0.20-py3-none-any.whl size=67162 sha256=aed3d73c0812c59d11d6eeb4ceb5ae0104fd41196ad503a0fa5bd0928b13d73f
  Stored in directory: /Users/kai/Library/Caches/pip/wheels/28/dd/ea/756ac2cb38f4e73f04a756fb3b4650e5f5dcd019a641098959
Successfully built pypng
Installing collected packages: pypng
Successfully installed pypng-0.0.20
```

# 范例 

```
python3 create-qr-code.py http://apple.com
--- 命令行参数: ['create-qr-code.py', 'http://apple.com']
--- 二维码已生成: msg.png
```

```
python3 create-qr-code.py "See you tomorrow at 2 pm"
--- 命令行参数: ['create-qr-code.py', 'See you tomorrow at 2 pm']
--- 二维码已生成: msg.png
```