from fastapi import FastAPI, File, UploadFile

# 1. Initialize FastAPI application

app=FastAPI(
    title="AI File Upload API",
    description="API to receive images or PDF documents for AI processing "
)

@app.get("/")
def home():
    return {"message": "File Upload API is ready!"}

# 2. Endpoint to upload a single file (Image or PDF)

@app.post("/upload-document")
async def upload_document(file: UploadFile = File(...)):
    # Read the contents of the uploaded file
    file_content = await file.read()

    # Calculate the file size in kilobytes (KB)

    file_size_kb = round(len(file_content) / 1024, 2)

    # Return file matadata (In real AI projects, this content goes to your ML/AI model)

    return {
        "status": "Success",
        "filename": file.filename,
        "content_type": file.content_type,
        "file_size_kb": f"{file_size_kb}"
    }