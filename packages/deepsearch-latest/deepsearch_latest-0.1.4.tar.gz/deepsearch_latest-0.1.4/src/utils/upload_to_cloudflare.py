import os
import boto3
from pathlib import Path
from datetime import datetime
from typing import Dict, Optional, Tuple
from dotenv import load_dotenv
# Load environment variables
load_dotenv()

# Get Cloudflare R2 credentials from environment variables
CLOUDFLARE_ACCOUNT_ID = os.getenv('CLOUDFLARE_ACCOUNT_ID')
CLOUDFLARE_ACCESS_KEY_ID = os.getenv('CLOUDFLARE_ACCESS_KEY_ID')
CLOUDFLARE_SECRET_ACCESS_KEY = os.getenv('CLOUDFLARE_SECRET_ACCESS_KEY')


class CloudflareUploader:
    def __init__(self):
        self.s3 = boto3.client(
            's3',
            endpoint_url=os.getenv('R2_ENDPOINT'),
            aws_access_key_id=os.getenv('R2_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('R2_SECRET_ACCESS_KEY')
        )
        self.bucket = os.getenv('R2_BUCKET_NAME')

    def upload_document(self, file_path: str, metadata: Dict) -> Tuple[Optional[str], Optional[Dict]]:
        """
        Upload a document to Cloudflare R2.

        Args:
            file_path (str): Path to the file to upload
            metadata (Dict): Not used, kept for interface compatibility

        Returns:
            Tuple[Optional[str], Optional[Dict]]: The R2 path where the file was uploaded, and the metadata
        """
        try:
            # Generate R2 path: documents/filename_YYYYMMDD_HHMMSS
            file_name = Path(file_path).name
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            base_name, ext = os.path.splitext(file_name)
            r2_path = f"documents/{base_name}_{timestamp}{ext}"

            # Upload file without metadata
            with open(file_path, 'rb') as f:
                self.s3.put_object(
                    Bucket=self.bucket,
                    Key=r2_path,
                    Body=f
                )

            # Update metadata
            metadata = {
                'original_filename': os.path.basename(file_path),
                'upload_date': datetime.now().isoformat(),
                'file_size': os.path.getsize(file_path)
            }

            return r2_path, metadata

        except Exception as e:
            print(f"Upload error: {str(e)}")
            return None, None

    def _fetch_document_text(self, file_path: str) -> Optional[str]:
        """Fetch document text from Cloudflare R2."""
        try:
            response = self.s3.get_object(
                Bucket=self.bucket,
                Key=file_path
            )
            return response['Body'].read().decode('utf-8')
        except Exception:
            return None
