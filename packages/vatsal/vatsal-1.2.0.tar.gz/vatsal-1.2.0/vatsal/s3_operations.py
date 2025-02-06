"""
This module contains a class for all S3 operations using boto3 client. It also contains a callback function to
show the progress of file upload.

Author: vatsal1306
"""
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Any, Optional

import boto3
from botocore.exceptions import ClientError

from vatsal.utils import ProgressPercentage


class S3:
    """Class for all S3 operations using boto3 client."""

    def __init__(self, aws_access_key: str, aws_secret_key: str, region="ap-south-1"):
        """
        Initialize S3 client.
        :param region: AWS region (default: ap-south-1)
        :param aws_access_key: AWS access key
        :param aws_secret_key: AWS secret key
        """
        self.region = region
        session = boto3.Session(
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key
        )
        self._s3 = session.client('s3', region_name=region)

    def create_bucket(self, bucket_name: str) -> bool:
        """
        Create a new S3 bucket.
        :param bucket_name: Name of the bucket
        :return: True if bucket is created, else raise Exception
        """
        try:
            self._s3.create_bucket(Bucket=bucket_name,
                                   CreateBucketConfiguration={'LocationConstraint': self.region})
            return True
        except Exception as e:
            raise e

    def get_all_buckets(self) -> List[str]:
        """Return a List of all S3 buckets."""
        return [bucket['Name'] for bucket in self._s3.list_buckets()['Buckets']]

    def _upload_large_file(self, file_path: str, bucket: str, object_name: str) -> bool:
        """
        Upload a large file using multipart upload.
        :param file_path: Absolute path to file
        :param bucket: Bucket to upload to
        :param object_name: S3 object name
        """
        config = boto3.s3.transfer.TransferConfig(multipart_threshold=5 * 1024 * 1024,
                                                  max_concurrency=15,
                                                  multipart_chunksize=5 * 1024 * 1024,
                                                  use_threads=True)
        try:
            self._s3.upload_file(file_path, bucket, object_name, Config=config, Callback=ProgressPercentage(file_path))
        except ClientError as e:
            print(f"Failed to upload large file {file_path}: {e}")
            return False
        return True

    def upload_file(self, file_path: str, bucket: str, object_name=None) -> bool:
        """
        Upload a file to an S3 bucket.
        :param file_path: Absolute path to file
        :param bucket: Bucket to upload to
        :param object_name: S3 object name. If not specified then file_path is used
        :return: True if file is uploaded, else raise Exception
        """
        try:
            if object_name is None:
                object_name = os.path.basename(file_path)

            file_size = os.path.getsize(file_path)
            if file_size > 10 * 1024 * 1024:  # 10MB threshold for multipart upload
                return self._upload_large_file(file_path, bucket, object_name)
            else:
                self._s3.upload_file(file_path, bucket, object_name, Callback=ProgressPercentage(file_path))
            return True
        except Exception as e:
            raise e

    def upload_directory(self, directory: str, bucket: str, key: str) -> None:
        """
        Upload a directory to S3 bucket. This function uses ThreadPoolExecutor to upload files in parallel.
        :param directory: Path to directory
        :param bucket: Bucket to upload to
        :param key: S3 object key
        """
        files = os.listdir(directory)
        print(f"Uploading {len(files)} files from {directory} to {bucket}/{key}")
        with ThreadPoolExecutor(max_workers=15) as executor:
            future_to_file = {executor.submit(self.upload_file, os.path.join(directory, file), bucket,
                                              f"{key}/{os.path.basename(file)}"): file for file in files}
            for future in as_completed(future_to_file):
                file = future_to_file[future]
                try:
                    result = future.result()
                    if not result:
                        print(f"Failed to upload {file}")
                except Exception as e:
                    print(f"Exception occurred while uploading {file}: {e}")

    def download_file(self, bucket: str, object_name: str, file_name: str, transfer_config: bool = False) -> bool:
        """
        Download a file from S3 bucket.
        :param transfer_config: Transfer configuration for multipart download
        :param bucket: Bucket to download from
        :param object_name: S3 object name
        :param file_name: Absolute path to save the file
        :return: True if file is downloaded, else raise Exception
        """
        try:
            if transfer_config:
                threshold = 1024 ** 3
                transfer_config = boto3.s3.transfer.TransferConfig(multipart_threshold=threshold, max_concurrency=100)
                self._s3.download_file(bucket, object_name, file_name, Callback=ProgressPercentage(object_name),
                                       Config=transfer_config)
            else:
                self._s3.download_file(bucket, object_name, file_name, Callback=ProgressPercentage(object_name))
            return True
        except Exception as e:
            raise e

    def check_bucket_exists(self, bucket_name: str) -> bool:
        """
        Check if a bucket exists in S3.
        :param bucket_name: Name of the bucket
        :return: True if the bucket exists, else False
        """
        try:
            self._s3.head_bucket(Bucket=bucket_name)
            return True
        except ClientError:
            return False

    def delete_bucket(self, bucket_name: str) -> bool:
        """
        Delete a bucket from S3.
        :param bucket_name: Name of the bucket
        :return: True if the bucket is deleted, else raise Exception
        """
        try:
            self._s3.delete_bucket(Bucket=bucket_name)
            return True
        except Exception as e:
            raise e

    def delete_object(self, bucket_name: str, object_name: str) -> bool:
        """
        Delete an object from S3.
        :param bucket_name: Name of the bucket
        :param object_name: Name of the object
        :return: True if the object is deleted, else raise Exception
        """
        try:
            self._s3.delete_object(Bucket=bucket_name, Key=object_name)
            return True
        except Exception as e:
            raise e

    def write_create_file(self, bucket_name: str, file_name: str, object_name: str = None,
                          data: Optional[Any] = b'') -> bool:
        """
        Write data to a file in S3 or create an empty file.
        :param bucket_name: Name of the bucket
        :param object_name: Name of the object
        :param file_name: Name of the file to write or to create
        :param data: Data to write. If None, empty file is created
        :return: True if data is written, else raise Exception
        """
        try:
            if object_name is None:
                object_name = os.path.basename(file_name)
            else:
                object_name = object_name + '/' + os.path.basename(file_name)

            self._s3.put_object(Bucket=bucket_name, Key=object_name, Body=data)
            return True
        except Exception as e:
            raise e

    def read_file(self, bucket_name: str, file_name: str, object_name: str = None) -> str:
        """
        Read a file from S3.
        :param file_name: Name of the file
        :param bucket_name: Name of the bucket
        :param object_name: Name of the object. if None, file_name is used to search in bucket
        :return: Data read from the file in string format.
        """
        try:
            if object_name is None:
                object_name = os.path.basename(file_name)
            else:
                object_name = object_name + '/' + os.path.basename(file_name)

            response = self._s3.get_object(Bucket=bucket_name, Key=object_name)
            return response['Body'].read().decode('utf-8')
        except Exception as e:
            raise e
