class CaesarCipher:
    """Class for doing encryption and decryption using Caesar Cipher"""

    def __init__(self, shift):
        """Construct Caesar Cipher using given integer shift for rotation"""
        encoder = [None] * 26
        decoder = [None] * 26
        for k in range(26):
            encoder[k] = chr((k + shift) % 26 + ord('A'))
            decoder[k] = chr((k - shift) % 26 + ord('A'))
        self._forward = ''.join(encoder)
        self._backward = ''.join(decoder)

    def encrypt(self, message):
        """Return string representing encrypted message"""
        return self._transform(message, self._forward)

    def decrypt(self, secret):
        """Return string representing decrypted message"""
        return self._transform(secret, self._backward)

    def _transform(self, original, code):
        """Utility to perform transformation based on given code string"""
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')
                msg[k] = code[j]
        return ''.join(msg)


if __name__ == '__main__':
    messages = ["THE EAGLE IS IN PLAY; MEET AT JOE'S."]
    keys = [5, -3, 3]

    ciphers = []
    for i in range(3):
        cipher = CaesarCipher(keys[i])
        ciphers.append(cipher)
        message = messages[0]
        coded = cipher.encrypt(message)
        print('secret:', coded)
        answer = cipher.decrypt(coded)
        print('message:', answer)