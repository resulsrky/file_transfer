import socket
import time

# Alıcının (hedef) ayarları
# EĞER YEREL AĞDA TEST EDİYORSANIZ: Alıcının IP adresini yazın (ör: '192.168.1.5')
# EĞER İNTERNETTEN GÖNDERİYORSANIZ: Alıcının Genel IP adresini yazın
HOST = '192.168.1.207'  # Şimdilik kendimize (localhost) gönderelim
PORT = 4444
BUFFER_SIZE = 1024  # Parça boyutu

# Gönderilecek dosyanın adı
FILENAME = 'WhatsApp Image 2025-08-02 at 23.56.37.jpeg'
# UDP soketi oluştur
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Dosyayı 'binary read' modunda aç
with open(FILENAME, 'rb') as f:
    while True:
        # Dosyadan bir parça (chunk) oku
        data = f.read(BUFFER_SIZE)

        # Eğer dosyanın sonuna gelindiyse döngüyü kır
        if not data:
            break

        # Okunan parçayı hedefe gönder
        s.sendto(data, (HOST, PORT))
        print(f"[+] {len(data)} byte'lik parca gonderildi.")
        # Paketlerin birbirine girmemesi için küçük bir bekleme ekleyebiliriz (opsiyonel)
        # time.sleep(0.001)

# Transferin bittiğini belirtmek için boş bir paket gönder
s.sendto(b'', (HOST, PORT))
print("[*] Dosya gonderme islemi tamamlandi.")

# Soketi kapat
s.close()