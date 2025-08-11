from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from agent.agentic_workflow import GraphBuilder
from utils.save_to_document import save_document
import os
from dotenv import load_dotenv
from pydantic import BaseModel
from pathlib import Path

load_dotenv()

app = FastAPI()

# Mount static files
# Serve static files from the frontend directory
frontend_dir = Path(__file__).parent.parent / "frontend"
app.mount("/static", StaticFiles(directory=str(frontend_dir / "static")), name="static")

# CORS middleware - Configure to allow all origins for development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
    expose_headers=["*"],  # Expose all headers
)
class QueryRequest(BaseModel):
    question: str

@app.post("/query")
async def query_travel_agent(query: QueryRequest):
    try:
        print("Received query:", query)
        
        # Initialize the graph with the model provider
        graph = GraphBuilder(model_provider="groq")
        react_app = graph()

        # Save the graph visualization (optional)
        try:
            png_graph = react_app.get_graph().draw_mermaid_png()
            with open("my_graph.png", "wb") as f:
                f.write(png_graph)
            print(f"Graph visualization saved as 'my_graph.png'")
        except Exception as e:
            print(f"Could not save graph visualization: {e}")
        
        # Process the query
        messages = {"messages": [query.question]}
        print("Sending to AI model:", messages)
        
        output = react_app.invoke(messages)
        print("Raw AI response:", output)

        # Process the AI response
        if isinstance(output, dict) and "messages" in output and output["messages"]:
            final_output = output["messages"][-1].content
        elif isinstance(output, str):
            final_output = output
        else:
            final_output = str(output)
        
        print("Final response:", final_output)
        return {"answer": final_output}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.get("/")
async def read_index():
    return FileResponse("static/index.html", media_type="text/html")

if __name__ == "__main__":
    import uvicorn
    # Ensure frontend/static directory exists
    frontend_dir = Path(__file__).parent.parent / "frontend"
    (frontend_dir / "static").mkdir(parents=True, exist_ok=True)
    
    # Load environment variables
    load_dotenv()
    uvicorn.run(app, host="0.0.0.0", port=8000)