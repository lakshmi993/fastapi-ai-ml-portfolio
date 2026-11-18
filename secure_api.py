from fastapi import FastAPI, File, UploadFile, Header, HTTPException

app = FastAPI(
    title="Secure AI File Upload API",
    description="Protected API requiring a valid API key to upload files")


# 1. Define a secret API Key
SECRET_API_KEY = "my-secret-ai-key-2026"

@app.get("/")
def home():
    return {"Message": "Secure AI API is running!"}

# 2. Protected Endpoint: Checks the 'x-api-key' header before processing the file 

@app.post("/upload-document")
async def upload_document(
    file: UploadFile = File(...),
    x_api_key: str = Header(..., description="Enter you secret API key")):

    #  Verify if the provided API key matches our secret key

    if x_api_key != SECRET_API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key! Access Denied.")

    # Process the file only if the key is valid

    file_content = await file.read()
    file_size_kb = round(len(file_content) / 1024, 2)

    return {
        "Status": "Authorized & Uploaded",
        "filename": file.filename,
        "content_type": file.content_type, 
        "file_size_kb": f"{file_size_kb} KB"
    }






