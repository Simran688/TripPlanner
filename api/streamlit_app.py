from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import subprocess
import uvicorn
import sys
import os
from pathlib import Path

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/stream")
async def stream():
    # This is a simplified example - you'll need to adapt this to your Streamlit app
    def generate():
        # Here you would run your Streamlit app and stream its output
        process = subprocess.Popen(
            [sys.executable, "-m", "streamlit", "run", "streamlit_app.py", "--server.headless", "true"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
            universal_newlines=True,
        )
        
        for line in process.stdout:
            yield f"data: {line}\n\n"
    
    return StreamingResponse(generate(), media_type="text/event-stream")

if __name__ == "__main__":
    uvicorn.run("api.streamlit_app:app", host="0.0.0.0", port=8000, reload=True)
