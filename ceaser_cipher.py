class CeaserCipher:

    def __init__(self, shift):
        """
        Constructor for the cipher object - constructs the forward/backward translation arrays
        :param shift: The amount of shift required in the cipher
        """

        self._forward = 26 * [None]
        self._backward = 26 * [None]

        for k in range(26):

            self._forward[k] = chr(ord('A') + (k + shift)%26)
            self._backward[k] = chr(ord('A') + (k - shift)%26)

    def transform(self, message, code):
        """
        Transforms the message according to the code
        :param message: The message that needs transforming - String
        :param code: The code used to transform the message - forward (encryption) & backward(decryption) - Char list
        :return: Transformed message
        """
        msg = list(message)

        for k in range(len(msg)):

            if msg[k].isupper():

                j = ord(msg[k]) - ord('A')
                msg[k] = code[j]

        return "".join(msg)

    def encrypt(self, message):

        return self.transform(message, self._forward)

    def decrypt(self, message):

        return self.transform(message, self._backward)

if __name__ == '__main__':

    Cipher = CeaserCipher(3)

    plaintext = "BYE BYE MISS AMERICAN PiE"
    ciphertext = Cipher.encrypt(plaintext)
    d_text = Cipher.decrypt(ciphertext)

    print(plaintext)
    print(ciphertext)
    print(d_text)

