from Crypto.Cipher import AES
import base64


# str不是16的倍数那就补足为16的倍数
def add_to_16(value='1234567890123456'):
    while len(value) % 16 != 0:
        value += '\0'
    return str.encode(value)  # 返回bytes


# 加密方法
def myEncrypt(data):
    # 初始化加密器，先进行aes加密
    key = 'f351ddc7e3698ab8'.encode('utf-8')
    mode = AES.MODE_CBC
    iv = b'02f3b743271aef51'

    aes = AES.new(key,AES.MODE_CBC,iv)
    encrypt_aes = aes.encrypt(add_to_16(data))

    # 用base64编码
    encrypted_data = base64.encodebytes(encrypt_aes)
    # print(encrypted_data)
    return str(encrypted_data, encoding='utf-8')


# password = myEncrypt("test123456")
# print(password)
