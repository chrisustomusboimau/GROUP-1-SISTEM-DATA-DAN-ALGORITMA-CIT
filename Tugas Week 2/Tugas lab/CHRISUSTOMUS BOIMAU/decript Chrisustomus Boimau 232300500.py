class CaesarCipher:

    def __init__(self,shift):
        encoder = [None] * 26
        decoder = [None] * 26
        for k in range(26):
            encoder[k] = chr((k + shift)%26 + ord('A'))
            decoder[k] = chr((k- shift)%26 + ord('A'))
        self._forward = ''.join(encoder)
        self._backward = ''.join(decoder)

    def encrypt(self,message):
        return self._transform(message,self._forward)

    def decrypt(self, secret):
        return self._transform(secret, self._backward)

    def _transform(self, original, code):
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')
                msg[k] = code[j]
        return ''.join(msg)


if __name__ == '__main__':
    key = [5,-1,10]
    message = ["ATTACKATFIVEPM","BROKENARROW","VILGEN06110502"]
    for i in range(len(key)):
        cipher = CaesarCipher(key[i])
        coded = cipher.encrypt(message[i])
        print("secret: ", coded)
        answer = cipher.decrypt(coded)
        print('message:',answer)

    
# if __name__ == '__main__':
#     message = "Antidisestablishmentarianism"
#     cipher = CaesarCipher(11)
#     coded = cipher.encrypt(message)
#     print("secret: ", coded)
#     answer = cipher.decrypt(coded)
#     print('message:',answer)