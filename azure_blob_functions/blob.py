from typing import BinaryIO
from azure.storage.blob import BlobServiceClient
from os import getenv

from responses.response_json import response_json
from responses.response_stream import response_stream

blob_service_client = BlobServiceClient.from_connection_string(
    getenv("AZURE_STORAGE_CONNECTION_STRING"))


def upload_blob(filename: str, container: str, data: BinaryIO):
    try:
        blob_client = blob_service_client.get_blob_client(
            container=container, blob=filename)

        blob_client.upload_blob(data)

        return response_json(message="success")
    except Exception as e:
        return response_json(message=e.message, status=500)


def get_blob(filename: str, container: str):
    try:
        blob_client = blob_service_client.get_blob_client(
            container=container, blob=filename)
        return response_stream(data=blob_client.download_blob().chunks(), download=False)
    except Exception as e:
        return response_json(message=e.message, status=500)



def download_blob(filename: str, container: str):
    try:
        blob_client = blob_service_client.get_blob_client(
            container=container, blob=filename)
        return response_stream(data=blob_client.download_blob().chunks(), download=True)
    except Exception as e:
        return response_json(message=e.message, status=500)


def delete_blob(filename: str, container: str):
    try:
        blob_client = blob_service_client.get_blob_client(
            container=container, blob=filename)

        blob_client.delete_blob()

        return response_json(message="success")
    except Exception as e:
        return response_json(message=e.message, status=500)