import sqlite3

def guvensiz_giris(kullanici_adi, sifre):
    conn = sqlite3.connect('veritabani.db')
    cursor = conn.cursor()
    
    # KRİTİK ZAFİYET: Kullanıcı girdisi temizlenmeden (sanitize edilmeden) doğrudan sorguya ekleniyor!
    # Bu durum SQL Injection (CWE-89) açığına sebep olur.
    sorgu = f"SELECT * FROM kullanicilar WHERE username = '{kullanici_adi}' AND password = '{sifre}'"
    
    cursor.execute(sorgu)
    return cursor.fetchone()

# Test girdisi (Zafiyet tetikleme örneği)
user_input = "admin' OR '1'='1"
password_input = "rastgele"
guvensiz_giris(user_input, password_input)
