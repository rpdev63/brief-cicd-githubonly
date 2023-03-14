from app.models.sha_algo import SHA


class TestSHA:

    def setup_method(self, method):
        self.sha = SHA()

    def test_encrypt_success(self):
        message = 'hello world'
        expected_result = '309ecc489c12d6eb4cc40f50c902f2b4d0ed77ee511a7c7a9bcd3ca86d4cd86f989dd35bc5ff499670da34255b45b0cfd830e81f605dcf7dc5542e93ae9cd76f'
        result = self.sha.encrypt(message)
        assert result == expected_result

    def test_encrypt_with_non_string_input(self):
        message = 1234
        result = self.sha.encrypt(message)
        assert result is False

    def test_decrypt_always_return_false(self):
        message = 'test'
        result = self.sha.decrypt(message)
        assert result is False
