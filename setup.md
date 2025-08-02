
# 🛠️ Project Setup Guide

## Prerequisites
- Python 3.10 or higher
- Git
- UV package manager
- Required API keys (see [API Setup](#api-setup))

## 1. Environment Setup

### Install UV Package Manager
```bash
pip install uv
```

### Verify UV Installation
```bash
uv --version
```

## 2. Clone the Repository
```bash
git clone https://github.com/yourusername/AI_Trip_Planner.git
cd AI_Trip_Planner
```

## 3. Create and Activate Virtual Environment

### For Windows:
```bash
uv venv .venv
.venv\Scripts\activate
```

### For macOS/Linux:
```bash
uv venv .venv
source .venv/bin/activate
```

## 4. Install Dependencies

### Using UV (Recommended):
```bash
uv pip install -r requirements.txt
```

### Or using pip:
```bash
pip install -r requirements.txt
```

## 5. API Setup

1. Create a `.env` file in the project root:
   ```bash
   cp .env.name .env
   ```

2. Add your API keys to the `.env` file:
   ```
   OPENAI_API_KEY=your_openai_key
   GROQ_API_KEY=your_groq_key
   GOOGLE_API_KEY=your_google_key
   # Add other API keys as needed
   ```

## 6. Database Setup (if applicable)

### Initialize Database:
```bash
python init_db.py
```

## 7. Run the Application

### Start the Backend Server:
```bash
uvicorn main:app --reload
```

### Start the Frontend:
```bash
streamlit run streamlit_app.py
```

## 8. Access the Application
- Frontend: http://localhost:8501
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs

## 9. Development Tools

### Run Tests:
```bash
pytest
```

### Check Code Style:
```bash
flake8 .
```

## 10. Troubleshooting

### Common Issues:
1. **Missing Dependencies**:
   ```bash
   uv pip install -r requirements.txt --upgrade
   ```

2. **Port Already in Use**:
   - Check for running processes and terminate them
   - Or change the port in the respective configuration

3. **API Key Errors**:
   - Verify all API keys in `.env`
   - Ensure the `.env` file is in the root directory

## 11. Deployment

### Build for Production:
```bash
uv pip install -r requirements-prod.txt
```

### Run with Gunicorn (Production):
```bash
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
```

---
*Need help? Open an issue on our [GitHub repository](https://github.com/yourusername/AI_Trip_Planner/issues)*

#if you have conda then first deactivate that
```conda deactivate```

```uv venv env --python cpython-3.10.18-windows-x86_64-none```

## use this command from your virtual env
```C:\Users\sunny\AI_Trip_Planner\env\Scripts\activate.bat```


```
streamlit run streamlit_app.py
```

```
uvicorn main:app --reload --port 8000
```