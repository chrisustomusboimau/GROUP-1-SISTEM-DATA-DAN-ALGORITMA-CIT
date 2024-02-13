class CaesarCipher:
    """Class for doing encryption and decryption using a Caesar cipher."""
    
    def __init__(self,shift):
        """Construct Chaesar cipher using given integer shift for rotation"""
        encoder = [None]*26
        decoder = [None]*26
        for k in range (26):
            encoder[k] = chr((k+shift)%26 +ord('A'))
            decoder[k] = chr((k-shift)%26 +ord('A'))
        self._forward = ''.join(encoder)
        self._backward = ''.join(decoder)

    def encrypt(self, message):
        '''Return string representing encripted message'''
        return self._transform(message, self._forward)
    
    def decrypt(self, secret):
        '''Return string representing dencripted message'''
        return self._transform(secret, self._backward)
    
    def _transform(self, original, code):
        msg = list(original)
        for k in range (len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')
                msg[k] = code[j]
        return ''.join(msg)

if __name__ == '__main__':
    cipher = [None,None,None]
    teks = ['ATTACKATFIVEPM','BROKENARROW','VULGEN06110502']
    key = [5,-3,10]
    # cipher = CaesarCipher(-10)
    # message = "CORAMDEO"
    # coded = cipher.encrypt(message)
    # print ('secret: ',coded)

    for i in range (3):
        cipher =CaesarCipher(key[i])
        msg = teks[i]
        coded = cipher.encrypt(msg)
        print ('secret: ',coded)



# ATTACKATFIVEPM (5)
# FYYFHPFYKNAJUR
# BROKENARROW (-3)
# YOLHBKXOOLT
#     "VULGEN06110502" (10)
# MYBKWNOY
