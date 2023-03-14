from app.models.aes_algo import AdvancedEncryptionStandard


class TestAES:

    def setup_method(self, method):
        self.aes = AdvancedEncryptionStandard()

    def test_encrypt_success(self):
        message = 'hello'
        key = '1234567890ABCDEF'
        expected_result = 'b381772147'
        result = self.aes.encrypt(message, key=key)
        assert result == expected_result

    def test_encrypt_with_non_string_input(self):
        message = 1234123412341234
        key = '1234567890ABCDEF'
        result = self.aes.encrypt(message, key=key)
        assert result is False

    def test_encrypt_with_wrong_key_length(self):
        message = 'hello'
        key = '1234567890ABCDEF12'
        result = self.aes.encrypt(message, key=key)
        assert result is False

    def test_encrypt_with_non_string_key(self):
        message = 'hello'
        key = 123456789
        result = self.aes.encrypt(message, key=key)
        assert result is False

    def test_decrypt_success(self):
        message = 'b381772147'
        key = '1234567890ABCDEF'
        expected_result = 'hello'
        result = self.aes.decrypt(message, key=key)
        assert result == expected_result

    def test_decrypt_with_non_string_input(self):
        message = 2323233714
        key = '1234567890ABCDEF'
        result = self.aes.decrypt(message, key=key)
        assert result is False

    def test_decrypt_with_wrong_key_length(self):
        message = 'hello'
        key = '1234567890ABCDEF12'
        result = self.aes.decrypt(message, key=key)
        assert result is False

    def test_decrypt_with_non_string_key(self):
        message = 'hello'
        key = 123456789
        result = self.aes.decrypt(message, key=key)
        assert result is False
