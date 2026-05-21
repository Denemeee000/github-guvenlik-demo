from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/login', methods=['GET'])
def login():
    kullanici_adi = request.args.get('username')

    conn = sqlite3.connect('siber_test.db')
    cursor = conn.cursor()

    # GÜVENLİ KOD: Veri, string birleştirmesi yerine tuple olarak (?) parametre ile gönderiliyor.
    # Bu sayede SQL Injection (CWE-89) tamamen engellenmiş olur!
    sorgu = "SELECT * FROM users WHERE username = ?"
    cursor.execute(sorgu, (kullanici_adi,))

    user = cursor.fetchone()
    if user:
        return "Giriş Başarılı"
    return "Hatalı Giriş"

if __name__ == '__main__':
    app.run(debug=True)
