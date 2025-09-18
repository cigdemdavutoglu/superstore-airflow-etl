# Superstore ETL Projesi

Bu proje, Kaggle üzerinde bulunan Superstore veri seti kullanılarak gerçekleştirilen bir ETL sürecini kapsamaktadır. 
Ham veriler Jupyter Notebook kullanılarak temizlenmiş, boyut (dimension) ve fakt (fact) tablolarına ayrılmıştır. Temizlenen veriler PostgreSQL veritabanına aktarılmış, bu sürecin otomasyonu için Apache Airflow kullanılarak günlük çalışan bir DAG tasarlanmıştır. Son aşamada veriler Power BI ile görselleştirilmiş ve raporlanmıştır.

## 🔧 Kullanılan Teknolojiler

- **Python (Pandas, SQLAlchemy)**
- **Jupyter Notebook**
- **PostgreSQL**
- **Apache Airflow**
- **Power BI**

## 📂 Proje Dosyaları

| Dosya Adı                         | Açıklama |
|----------------------------------|----------|
| `superstore.csv`                 | Ham veri dosyası |
| `superstore_cleaning.ipynb`      | Verinin temizlendiği Jupyter Notebook |
| `load_all_tables.py`             | Temizlenen CSV dosyalarını PostgreSQL’e yükler |
| `superstore_etl_to_postgres.py`  | Airflow DAG dosyası (ETL sürecini otomatize eder) |
| `superstore_report.pbix`         | Power BI raporu (PostgreSQL'e bağlı) |
| `requirements.txt`               | Gerekli Python paketleri |
| `.gitignore`                     | Takip edilmeyecek dosya/klasör listesi |
| `LICENSE`                        | Proje lisansı |
| `README.md`                      | Proje açıklaması (bu dosya) |


## 🔄 Süreç Açıklaması

1. `superstore_cleaning.ipynb` ile veri temizlenir ve boyut/fakt tabloları oluşturulur.
2. `load_all_tables.py` ile bu tablolar PostgreSQL veritabanına yüklenir.
3. `superstore_etl_to_postgres.py` dosyası, Airflow kullanılarak bu süreci otomatize eder.
4. `superstore_report.pbix` dosyası PostgreSQL'e bağlı şekilde raporlamayı içerir.

## ⚙️ Airflow Kullanımı

- `superstore_etl_to_postgres.py` dosyasını Airflow’un `dags` klasörüne taşıyın.
- Scheduler ve Webserver servislerini başlatın.
- DAG'i çalıştırarak yeni veriler PostgreSQL'e otomatik olarak yüklensin.


