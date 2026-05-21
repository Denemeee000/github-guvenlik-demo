from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/login', methods=['GET'])
def login():
    # 1. SOURCE (GİRİŞ NOKTASI): CodeQL burayı dışarıdan gelen tehlikeli veri olarak işaretler.
    kullanici_adi = request.args.get('username')
    
    conn = sqlite3.connect('siber_test.db')
    cursor = conn.cursor()
    
    # 2. DATA FLOW (AKIŞ): Kirli veri hiçbir kontrolden geçmeden SQL stringiyle birleşiyor.
    sorgu = "SELECT * FROM users WHERE username = '" + kullanici_adi + "'"
    
    # 3. SINK (ÇIKIŞ NOKTASI): CodeQL burayı görür ve "Kritik Zafiyet" alarmını tetikler!
    cursor.execute(sorgu)
    
    user = cursor.fetchone()
    if user:
        return "Giriş Başarılı"
    return "Hatalı Giriş"

if __name__ == '__main__':
    app.run(debug=True)
