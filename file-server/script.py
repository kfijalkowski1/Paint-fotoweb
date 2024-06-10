import zipfile

from fastapi import FastAPI, HTTPException, File, UploadFile, Form
from fastapi.responses import FileResponse
import os
import shutil
import uuid
from fastapi.middleware.cors import CORSMiddleware
import ssl

app = FastAPI()

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain('path/to/key', keyfile='path/to/key')

origins = [
    "https://fotoreporterzy-paint.netlify.app",
    "http://fotoreporterzy-paint.netlify.app",
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = "/home/gambolkf/data"  # TODO on server change to: /home/gambolkf/data
SECRET_KEY = os.environ.get('SECRET_FILE_KEY')


@app.get("/files/{file_path:path}")
async def get_file(file_path: str):
    file_location = os.path.join(BASE_DIR, file_path)
    print(file_location)
    if os.path.exists(file_location):
        return FileResponse(path=file_location, filename=os.path.basename(file_location))
    else:
        raise HTTPException(status_code=404, detail="File not found")


@app.post("/upload")
async def upload_file(file: UploadFile = File(...), secretKey: str = Form(...)):
    print(SECRET_KEY)
    if secretKey != SECRET_KEY:
        raise HTTPException(status_code=403, detail="Invalid secret key")

    if not file.filename.endswith('.zip'):
        raise HTTPException(status_code=400, detail="Invalid input: Only ZIP files are accepted")

    folderUUID = str(uuid.uuid4())
    folder_path = os.path.join(BASE_DIR, folderUUID)
    if os.path.exists(folder_path):
        folderUUID = str(uuid.uuid4())
    os.makedirs(folder_path, exist_ok=True)

    file_location = os.path.join(folder_path, file.filename)
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        with zipfile.ZipFile(file_location, 'r') as zip_ref:
            zip_ref.extractall(folder_path)
    except zipfile.BadZipFile:
        shutil.rmtree(folder_path)  # Clean up by removing the folder if the ZIP is invalid
        raise HTTPException(status_code=400, detail="Invalid input: Corrupted ZIP file")

    return {"uuid": folderUUID}


@app.get("/getFileList/{folder_path:path}")
async def get_file_list(folder_path: str) -> list[str]:
    if (folder_path == ""):
        raise HTTPException(status_code=400, detail="Invalid input: Folder path is empty")
    full_path = os.path.join(BASE_DIR, folder_path)
    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        raise HTTPException(status_code=404, detail="Folder not found")

    files = os.listdir(full_path)
    return files


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
