import os
import requests
import pandas as pd
from datetime import datetime, timezone
import boto3
from botocore.exceptions import ClientError
from src.config import S3_BUCKET

URL = "https://jsonplaceholder.typicode.com/users"

def extract_data():
    resp = requests.get(URL, timeout=30)
    resp.raise_for_status()
    return resp.json()

def transform_data(data):
    df = pd.json_normalize(data)
    df["ingestion_utc"] = datetime.now(timezone.utc).isoformat()
    return df

def save_local(df, file_name: str) -> str:
    os.makedirs("data", exist_ok=True)
    local_path = os.path.join("data", file_name)
    df.to_csv(local_path, index=False)
    return local_path

def upload_to_s3(local_path: str, s3_key: str):
    s3 = boto3.client("s3")
    try:
        s3.upload_file(local_path, S3_BUCKET, s3_key)
    except ClientError as e:
        raise RuntimeError(f"Falha ao subir para o S3: {e}") from e

if __name__ == "__main__":
    data = extract_data()
    df = transform_data(data)

    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    file_name = f"users_{ts}.csv"

    local_path = save_local(df, file_name)
    s3_key = f"raw/users/dt={datetime.now(timezone.utc).strftime('%Y-%m-%d')}/{file_name}"

    upload_to_s3(local_path, s3_key)

    print("OK ✅")
    print("Arquivo local:", local_path)
    print("S3:", f"s3://{S3_BUCKET}/{s3_key}")
