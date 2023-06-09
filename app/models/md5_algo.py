"""Implementation of the MD5 hashing function"""

import logging
import logging.handlers
import hashlib
from app.views.encryptioninterface import EncryptionInterface


class MD5(EncryptionInterface):

    def __init__(self):

        self.logger = logging.getLogger(__name__)
        fh = logging.handlers.RotatingFileHandler(
            'app/logs/' + __name__ + '.log', maxBytes=10000000, backupCount=100)
        fh.setFormatter(logging.Formatter(
            fmt='%(asctime)s - %(levelname)s - %(name)s - %(message)s'))
        self.logger.addHandler(fh)

    def encrypt(self, message, key=0):

        if not isinstance(message, str):

            self.logger.error(
                "Error during the hashing of a message with MD5. The message must be a string")
            return False

        result = hashlib.md5(message.encode())

        return result.hexdigest()

    def decrypt(self, message, key=0):

        return False
