import base64

long_url="https://example.com/assets/guangxi/nannin/medical_school/my_cs2_1948/exercises/project1/qqqwwweeerrrttt1234561222978"
base64encoded = base64.b64encode(long_url.encode())
print (base64encoded)
base64encoded_url = base64encoded.decode()
print (base64encoded_url)
