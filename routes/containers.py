from fastapi import APIRouter, Form

from azure_blob_functions.container import create_container, delete_container, list_containers


container_routes = APIRouter()


@container_routes.post("/create")
def create(container: str = Form(...)):
    return create_container(container)


@container_routes.get("/containers")
def get():
    return list_containers()


@container_routes.delete("/delete")
def delete(container: str = Form(...)):
    return delete_container(container)