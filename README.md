# AI Travel Planner

This is a travel planning application with a separate frontend and backend.

## Project Structure

```
AI_Trip_Planner/
├── backend/           # Backend FastAPI server
│   ├── agent/         # AI agent implementation
│   ├── config/        # Configuration files
│   ├── exception/     # Custom exceptions
│   ├── logger/        # Logging configuration
│   ├── prompt_library/# AI prompts
│   ├── tools/         # Custom tools for the AI
│   ├── utils/         # Utility functions
│   ├── .env          # Environment variables
│   ├── main.py       # FastAPI application
│   ├── requirements.txt
│   └── setup.py
└── frontend/         # Frontend static files
    └── static/
        ├── index.html
        ├── styles.css
        └── app.js
```

## Project Structure

```
AI_Trip_Planner/
├── backend/           # Backend FastAPI server
│   ├── agent/
│   ├── tools/
│   ├── utils/
│   ├── main.py
│   └── requirements.txt
└── frontend/          # Frontend static files
    └── static/
        ├── index.html
        ├── styles.css
        └── app.js
```

## Setup and Running

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the backend directory with your API keys:
   ```
   GROQ_API_KEY=your_groq_api_key
   TAVILY_API_KEY=your_tavily_api_key
   GOOGLE_PLACES_API_KEY=your_google_places_api_key
   ```

4. Start the backend server:
   ```bash
   python main.py
   ```
   The backend will be available at `http://localhost:8000`

### Frontend Setup

The frontend is a static website that's already built and ready to be served by the backend.

## Access the Application

1. Open your web browser and go to `http://localhost:8000`
2. The AI Travel Planner interface should load
3. Start asking questions to plan your trip!

## Development

- Backend: FastAPI (Python)
- Frontend: HTML, CSS, JavaScript

## Environment Variables

Make sure to set up the following environment variables in your `.env` file:

- `GROQ_API_KEY`: API key for Groq
- `TAVILY_API_KEY`: API key for Tavily search
- `GOOGLE_PLACES_API_KEY`: API key for Google Places

## License

MIT
