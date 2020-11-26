from base64 import b64decode
from hashlib import sha1
from Crypto.Cipher import AES
from codecs import decode
from binascii import b2a_hex, a2b_hex
from binascii import unhexlify

def key(ka,kb):
    K = []
    a = bin(int(ka,16))[2:] + bin(int(kb,16))[2:]
    for i in range(0,len(a),8):
        if (a[i:i+7].count("1")) % 2 == 0:
            K.append(a[i:i+7])
            K.append('1') 
        else :
            K.append(a[i:i+7])
            K.append('0')
    K = hex(int(''.join(K),2))
    return K[2:]

if __name__ == '__main__':
    IV = unhexlify('00000000000000000000000000000000')
    c_text = b64decode('9MgYwmuPrjiecPMx61O6zIuy3MtIXQQ0E59T3xB6u0Gyf1gYs2i3K9Jxaa0zj4gTMazJuApwd6+jdyeI5iGHvhQyDHGVlAuYTgJrbFDrfB22Fpil2NfNnWFBTXyf7SDI')

    a = [1,1,1,1,1,6]
    b = [7,3,1,7,3,1]
    c = 0
    i = 0
    while i < 6:
        c = (c + a[i] * b[i]) % 10
        i = i + 1
    text = '12345678<81110182111116' + str(c)
    kd = sha1(text.encode()).hexdigest()[:32] + '00000001'
    [ka,kb] = sha1(decode(kd,"hex")).hexdigest()[:16],sha1(decode(kd,"hex")).hexdigest()[16:32]
    
    K = unhexlify(key(ka,kb))
    m_text = AES.new(K,AES.MODE_CBC,IV).decrypt(c_text)
    print(m_text)

