def test_index_page(test_client):
    response = test_client.get('/')
    assert response.status_code == 200
    assert b"Welcome to KryptX" in response.data


def test_aes_page(test_client):
    response = test_client.get('/aes')
    assert response.status_code == 200
    assert b"AES (Advanced Encryption Standard)" in response.data


def test_blowfish_page(test_client):
    response = test_client.get('/blowfish')
    assert response.status_code == 200
    assert b"Blowfish" in response.data


def test_caesar_cipher_page(test_client):
    response = test_client.get('/caesarcipher')
    assert response.status_code == 200
    assert b"Caesar cipher" in response.data


def test_des_page(test_client):
    response = test_client.get('/des')
    assert response.status_code == 200
    assert b"DES (Data Encryption Standard)" in response.data


def test_enigma_m3_page(test_client):
    response = test_client.get('/enigmam3')
    assert response.status_code == 200
    assert b"Enigma M3" in response.data


def test_md5_page(test_client):
    response = test_client.get('/md5')
    assert response.status_code == 200
    assert b"MD5 (Message Digest 5)" in response.data


def test_rsa_page(test_client):
    response = test_client.get('/rsa')
    assert response.status_code == 200
    assert b"RSA" in response.data


def test_sha_page(test_client):
    response = test_client.get('/sha')
    assert response.status_code == 200
    assert b"SHA-512" in response.data


def test_vigenere_cipher_page(test_client):
    response = test_client.get('/vigenerecipher')
    assert response.status_code == 200
    assert b"Cipher" in response.data
