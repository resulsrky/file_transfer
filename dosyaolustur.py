try:
    with open('gonderilecek_dosya.txt', 'w') as f:
        f.write("Merhaba dunya, bu bir UDP dosya transferi denemesidir.\n")
        f.write("Bu ikinci satir.\n")
        f.write("Ve bu da ucuncu satir.\n")
    print("'gonderilecek_dosya.txt' adli dosya basariyla olusturuldu.")
except IOError as e:
    print(f"Dosya olusturulurken bir hata olustu: {e}")