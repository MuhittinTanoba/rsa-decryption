import sympy
import time

# EBOB hesaplama
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

# Modüler ters hesaplama
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Modüler ters yoktur')
    else:
        return x % m

# Anahtar çiftlerini üretme
def generate_keys(p, q, e):
    start_encryption_time = time.time()
    n = p * q
    phi = (p - 1) * (q - 1)
    d = modinv(e, phi)
    end_keygen_time = time.time()
    time_keygen = end_keygen_time - start_encryption_time
    return n, phi, d, time_keygen

# Şifreleme işlemi
def encrypt(m, e, n):
    return pow(m, e, n)

# Deşifreleme işlemi
def decrypt(c, d, n):
    return pow(c, d, n)

if __name__ == "__main__":
    p = int(input("p değerini giriniz: "))  # p değerini alma
    q = int(input("q değerini giriniz: "))  # q değerini alma
    k = int(input("Şifrelenecek sayıyı giriniz (k): "))  # Şifrelenecek sayıyı alma
    e = int(input("Açık anahtar (e) değerini giriniz: "))  # Kullanıcıdan e değerini alma

    n, phi, d, time_keygen = generate_keys(p, q, e)

    print("\nn:", n)
    print("phi(n):", phi)
    print("Gizli anahtar (d):", d)
    print("Gizli Anahtar Hesaplama Süresi (D Time):", time_keygen)

    start_encryption_time = time.time()
    encrypted = encrypt(k, e, n)
    end_encryption_time = time.time()

    print("\nŞifreleme süresi:", end_encryption_time - start_encryption_time)
    print("Şifreli Metin:", encrypted)

    start_decryption_time = time.time()
    decrypted = decrypt(encrypted, d, n)
    end_decryption_time = time.time()

    print("\nDeşifreleme süresi:", end_decryption_time - start_decryption_time)
    print("Deşifrelenmiş Metin:", decrypted)
