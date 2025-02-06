from pydantic import BaseModel
import boto3

class UploadS3(BaseModel):
    endpoint: str
    bucket: str
    access_key: str
    secret_key: str
    source_file: str
    dest_file: str


def upload_data(config: UploadS3):
    s3_endpoint = config.endpoint
    s3_bucket = config.bucket
    s3_access_key = config.access_key
    s3_secret_key = config.secret_key

    s3_client = boto3.client(
        service_name="s3",
        endpoint_url=s3_endpoint,
        aws_access_key_id=s3_access_key,
        aws_secret_access_key=s3_secret_key,
        region_name="auto"
    )

    response = s3_client.upload_file(config.source_file, s3_bucket,config.dest_file)
    return response