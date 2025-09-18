import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL bağlantı bilgileri
DB_USER = 'train'
DB_PASS = 'Ankara06'
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'traindb'

engine = create_engine(f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

# CSV dosyaları ve karşılık gelen tablo isimleri
files_and_tables = [
    ('/home/train/datasets/dim_customer.csv', 'dim_customer'),
    ('/home/train/datasets/fact_sales.csv', 'fact_sales'),
    ('/home/train/datasets/dim_product.csv', 'dim_product'),
    ('/home/train/datasets/dim_date.csv', 'dim_date'),
]

for file_path, table_name in files_and_tables:
    print(f"Yükleniyor: {file_path} -> {table_name}")
    df = pd.read_csv(file_path)
nkara06



    # Tabloyu oluştur ve verileri yükle
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"{table_name} yüklendi.\n")

print("Tüm tablolar başarıyla yüklendi!")

