from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"info": "My name is Srijan Sarkar"}

@app.get("/health")
def health():
    return {"messege":"OK"}

@app.get("/status")
def status():
    return {"status":"OK","server":"Server is running"}