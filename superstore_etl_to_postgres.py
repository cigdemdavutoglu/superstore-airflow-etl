from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL bağlantı bilgileri
DB_USER = 'train'
DB_PASSWORD = 'Ankara06'
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'traindb'

# SQLAlchemy engine oluşturuluyor
engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

# Airflow DAG ayarları
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1
}

dag = DAG(
    dag_id='superstore_etl_to_postgres_unique_append',
    default_args=default_args,
    description='Load only new unique Superstore records from CSVs to PostgreSQL',
    schedule_interval='@daily',
    catchup=False
)

def load_unique_to_postgres(table_name, csv_path, unique_key):
    # CSV'yi oku
    df = pd.read_csv(csv_path)

    # Mevcut kayıtların unique key'lerini çek
    try:
        existing_keys = pd.read_sql(f"SELECT {unique_key} FROM {table_name}", engine)
        existing_keys_set = set(existing_keys[unique_key])
    except Exception as e:
        print(f"[WARN] Tablo yok veya sorgu başarısız, tabloya tamamen yazılacak: {e}")
        existing_keys_set = set()

    # Yeni benzersiz kayıtlar
    df_new = df[~df[unique_key].isin(existing_keys_set)]

    if not df_new.empty:
        df_new.to_sql(table_name, engine, if_exists='append', index=False)
        print(f"[INFO] {table_name} tablosuna {len(df_new)} yeni kayıt eklendi.")
    else:
        print(f"[INFO] {table_name} tablosunda eklenecek yeni kayıt yok.")

# Her tablo için benzersiz kayıt ekleme fonksiyonları 
def load_dim_customer():
    load_unique_to_postgres('dim_customer', '/home/train/datasets/dim_customer.csv', 'customer_id')

def load_dim_product():
    load_unique_to_postgres('dim_product', '/home/train/datasets/dim_product.csv', 'product_id')

def load_dim_date():
    load_unique_to_postgres('dim_date', '/home/train/datasets/dim_date.csv', 'order_date_id')

def load_fact_sales():
    load_unique_to_postgres('fact_sales', '/home/train/datasets/fact_sales.csv', 'order_id')

# Airflow görevleri
t1 = PythonOperator(task_id='load_dim_customer', python_callable=load_dim_customer, dag=dag)
t2 = PythonOperator(task_id='load_dim_product', python_callable=load_dim_product, dag=dag)
t3 = PythonOperator(task_id='load_dim_date', python_callable=load_dim_date, dag=dag)
t4 = PythonOperator(task_id='load_fact_sales', python_callable=load_fact_sales, dag=dag)

# Görev sıralaması: önce dim tablolar, sonra fact tablo
[t1, t2, t3] >> t4
