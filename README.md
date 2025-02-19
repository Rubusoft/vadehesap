# Vade Hesap

Kredi kartı taksit ve vade farkı hesaplama uygulaması.

## Özellikler

- Kredi kartı taksit hesaplama
- Vade farkı oranı hesaplama
- Admin paneli üzerinden taksit oranları yönetimi
- RESTful API desteği
- Swagger/ReDoc API dokümantasyonu

## Teknolojiler

- Python 3.13
- Django 5.1.6
- Django REST Framework
- PostgreSQL
- Bootstrap 5

## Kurulum

1. Projeyi klonlayın:
```bash
git clone https://github.com/KULLANICI_ADI/vadehesap.git
cd vadehesap
```

2. Sanal ortam oluşturun ve aktif edin:
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# veya
venv\Scripts\activate  # Windows
```

3. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

4. .env dosyasını oluşturun:
```
DEBUG=True
SECRET_KEY=your-secret-key
DB_NAME=vadehesap_db
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432
ALLOWED_HOSTS=localhost,127.0.0.1
```

5. Veritabanını oluşturun:
```bash
createdb vadehesap_db
python manage.py migrate
```

6. Süper kullanıcı oluşturun:
```bash
python manage.py createsuperuser
```

7. Geliştirme sunucusunu başlatın:
```bash
python manage.py runserver
```

## Kullanım

1. Tarayıcıda `http://localhost:8000` adresine gidin
2. Admin paneli için `http://localhost:8000/admin` adresini kullanın
3. API dokümantasyonu için:
   - Swagger UI: `http://localhost:8000/swagger/`
   - ReDoc: `http://localhost:8000/redoc/`

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın. 