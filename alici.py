import socket

# Alıcının (sunucu gibi davranan) ayarları
HOST = '0.0.0.0'  # Tüm ağ arayüzlerinden gelen bağlantıları dinle
PORT = 9999  # Dinlenecek port numarası
BUFFER_SIZE = 1024  # Tek seferde alınacak maksimum veri boyutu

# Yeni dosyanın adı
FILENAME = 'alinan_dosya.jpeg'

# UDP soketi oluştur
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Soketi belirtilen host ve porta bağla
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))

print(f"[*] {HOST}:{PORT} adresinde dinleme baslatildi...")

# Gelen veriyi dosyaya yazmak için dosyayı 'binary write' modunda aç
with open(FILENAME, 'wb') as f:
    while True:
        # Veriyi ve gönderenin adresini al
        data, addr = s.recvfrom(BUFFER_SIZE)

        # Eğer veri gelmediyse (gönderici transferi bitirdi), döngüyü kır
        if not data:
            print("[-] Veri akisi sonlandi. Dosya alimi tamamlandi.")
            break

        # Gelen veriyi dosyaya yaz
        f.write(data)

        # Ekrana küçük bir bilgi basalım
        print(f"[+] {addr} adresinden {len(data)} byte'lik veri alindi.")

# İşlem bittikten sonra soketi kapat
s.close()
print(f"[*] Soket kapatildi. '{FILENAME}' basariyla kaydedildi.")