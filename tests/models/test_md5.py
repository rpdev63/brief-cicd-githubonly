from app.models.md5_algo import MD5


class TestMD5:

    def setup_method(self, method):
        self.md5 = MD5()

    def test_encrypt_success(self):
        message = 'hello'
        expected_result = '5d41402abc4b2a76b9719d911017c592'
        result = self.md5.encrypt(message)
        assert result == expected_result

    def test_encrypt_with_non_string_input(self):
        message = 1234
        result = self.md5.encrypt(message)
        assert result is False

    def test_decrypt_always_return_false(self):
        message = 'test'
        result = self.md5.decrypt(message)
        assert result is False
