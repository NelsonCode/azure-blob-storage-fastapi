from azure.storage.blob import BlobServiceClient
from os import getenv
from responses.response_json import response_json


blob_service_client = BlobServiceClient.from_connection_string(
    getenv("AZURE_STORAGE_CONNECTION_STRING"))


def create_container(container: str):
    try:
        blob_service_client.create_container(container)
        return response_json(message="success")
    except Exception as e:
        return response_json(message=e.message, status=500)


def delete_container(container: str):
    try:
        blob_service_client.delete_container(container)
        return response_json(message="success")
    except Exception as e:
        return response_json(message=e.message, status=500)


def list_containers():
    try:
        containers = blob_service_client.list_containers()

        return [container.name for container in containers]
    except Exception as e:
        return response_json(message=e.message, status=500)
