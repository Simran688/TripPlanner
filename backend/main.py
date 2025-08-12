from fastapi import FastAPI, Request, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from agent.agentic_workflow import GraphBuilder
import os
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import Optional

load_dotenv()

app = FastAPI()
api_router = APIRouter(prefix="/api")

# CORS middleware configuration
# Update the origins list with your frontend URL(s)
origins = [
    "http://localhost:3000",  # Default React development server
    "http://localhost:5173",  # Default Vite development server
    # Add your production frontend URL here
    # "https://your-frontend-domain.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

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

@api_router.post("/query")
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

# Include the API router
app.include_router(api_router)

# Health check endpoint
@api_router.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/")
def read_root():
    return {"AI Trip Planner": "Welcome to AI Trip Planner"}

if __name__ == "__main__":
    import uvicorn
    load_dotenv()
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)