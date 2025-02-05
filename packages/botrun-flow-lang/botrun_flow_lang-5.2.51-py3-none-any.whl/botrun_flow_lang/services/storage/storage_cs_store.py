from google.cloud import storage
from google.cloud.exceptions import NotFound
from google.oauth2 import service_account
from io import BytesIO
import os
from typing import Optional, Tuple
from datetime import datetime, timedelta, UTC

from botrun_flow_lang.constants import HATCH_BUCKET_NAME
from botrun_flow_lang.services.storage.storage_store import StorageStore


class StorageCsStore(StorageStore):
    def __init__(self, env_name: str):
        google_service_account_key_path = os.getenv(
            "GOOGLE_APPLICATION_CREDENTIALS_FOR_FASTAPI",
            "/app/keys/scoop-386004-d22d99a7afd9.json",
        )
        credentials = service_account.Credentials.from_service_account_file(
            google_service_account_key_path,
            scopes=["https://www.googleapis.com/auth/devstorage.full_control"],
        )

        self.storage_client = storage.Client(credentials=credentials)
        self.bucket_name = f"{HATCH_BUCKET_NAME}-{env_name}"
        self.bucket = self.create_bucket(self.bucket_name)
        if not self.bucket:
            raise Exception(f"Failed to create or get bucket: {self.bucket_name}")

    def create_bucket(self, bucket_name: str) -> Optional[storage.Bucket]:
        """創建新的 bucket，如果已存在則返回現有的"""
        try:
            bucket = self.storage_client.bucket(bucket_name)

            if not bucket.exists():
                print(f"Creating new bucket: {bucket_name}")
                bucket = self.storage_client.create_bucket(
                    bucket_name, location="asia-east1"
                )
                print(f"Created bucket {bucket_name} in asia-east1")
            else:
                print(f"Bucket {bucket_name} already exists")

            # 檢查並設定預設的 lifecycle rule
            lifecycle_config = {
                "rule": [
                    {
                        "action": {"type": "Delete"},
                        "condition": {"age": 7, "matchesPrefix": ["tmp/"]},
                    }
                ]
            }

            bucket.lifecycle_rules = lifecycle_config["rule"]
            bucket.patch()
            print(f"Set lifecycle rules for bucket {bucket_name}")

            return bucket
        except Exception as e:
            print(f"Error creating bucket {bucket_name}: {str(e)}")
            return None

    async def store_file(
        self,
        filepath: str,
        file_object: BytesIO,
        public: bool = False,
        content_type: str = None,
    ) -> Tuple[bool, Optional[str]]:
        try:
            blob = self.bucket.blob(filepath)

            # 設定 content_type 和其他 metadata
            if content_type:
                blob.content_type = content_type
                # 如果是圖片，設定為 inline 顯示並加入 cache control
                if content_type.startswith("image/"):
                    blob.content_disposition = (
                        'inline; filename="' + filepath.split("/")[-1] + '"'
                    )
                    blob.cache_control = "public, max-age=3600, no-transform"

            # 上傳檔案
            blob.upload_from_file(file_object, rewind=True)

            # 確保 metadata 更新
            blob.patch()

            # 如果需要公開存取
            if public:
                blob.make_public()
                return True, blob.public_url

            return True, None
        except Exception as e:
            print(f"Error storing file in Cloud Storage: {e}")
            return False, None

    async def get_public_url(self, filepath: str) -> Optional[str]:
        try:
            blob = self.bucket.blob(filepath)
            if blob.exists():
                return blob.public_url
            return None
        except Exception as e:
            print(f"Error getting public URL: {e}")
            return None

    async def retrieve_file(self, filepath: str) -> Optional[BytesIO]:
        try:
            blob = self.bucket.blob(filepath)
            file_object = BytesIO()
            blob.download_to_file(file_object)
            file_object.seek(0)  # Rewind the file object to the beginning
            return file_object
        except NotFound:
            print(f"File not found in Cloud Storage: {filepath}")
            return None
        except Exception as e:
            print(f"Error retrieving file from Cloud Storage: {e}")
            return None

    async def delete_file(self, filepath: str) -> bool:
        try:
            blob = self.bucket.blob(filepath)
            blob.delete()
            return True
        except NotFound:
            print(f"File not found in Cloud Storage: {filepath}")
            return False
        except Exception as e:
            print(f"Error deleting file from Cloud Storage: {e}")
            return False

    async def file_exists(self, filepath: str) -> bool:
        try:
            blob = self.bucket.blob(filepath)
            return blob.exists()
        except Exception as e:
            print(f"Error checking file existence in Cloud Storage: {e}")
            return False
