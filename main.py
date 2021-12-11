from fastapi import FastAPI
from routes.blobs import blob_routes
from routes.containers import container_routes

app = FastAPI()

app.include_router(blob_routes, prefix="/storage/blob")
app.include_router(container_routes, prefix="/storage/container")
