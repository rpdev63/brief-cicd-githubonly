from app.models.des_algo import DES


class TestDES:

    def setup_method(self, method):
        self.des = DES()

    def test_encrypt_success(self):
        message = 'hello'
        key = '1234567890ABCDEF'
        expected_result = 'df88b4de41032d35'
        result = self.des.encrypt(message, key=key)
        assert result == expected_result

    def test_encrypt_with_non_string_input(self):
        message = 1234123412341234
        key = '1234567890ABCDEF'
        result = self.des.encrypt(message, key=key)
        assert result is False

    def test_encrypt_with_wrong_key_length(self):
        message = 'hello'
        key = '1234567890ABCDEF12'
        result = self.des.encrypt(message, key=key)
        assert result is False

    def test_encrypt_with_non_string_key(self):
        message = 'hello'
        key = 123456789
        result = self.des.encrypt(message, key=key)
        assert result is False

    def test_decrypt_success(self):
        message = 'df88b4de41032d35'
        key = '1234567890ABCDEF'
        expected_result = 'hello'
        result = self.des.decrypt(message, key=key)
        assert result == expected_result

    def test_decrypt_with_non_string_input(self):
        message = 2323233714
        key = '1234567890ABCDEF'
        result = self.des.decrypt(message, key=key)
        assert result is False

    def test_decrypt_with_wrong_key_length(self):
        message = 'hello'
        key = '1234567890ABCDEF12'
        result = self.des.decrypt(message, key=key)
        assert result is False

    def test_decrypt_with_non_string_key(self):
        message = 'hello'
        key = 123456789
        result = self.des.decrypt(message, key=key)
        assert result is False
