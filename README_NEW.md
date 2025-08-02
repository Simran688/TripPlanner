# 🌍 AI Travel Planner

## 📌 Overview
An intelligent travel planning assistant that creates personalized travel itineraries using AI and real-time data. The system generates comprehensive travel plans including accommodations, activities, dining options, and cost estimates.

## 🛠️ Technologies Used

### Backend
- **Framework**: FastAPI
- **AI/ML**: LangGraph, OpenAI/Groq
- **API Services**:
  - Google Maps/Places API
  - OpenWeatherMap API
  - Foursquare API
  - Currency Exchange Rate API
  - Tavilay API (travel services)

### Frontend
- **Framework**: Streamlit
- **UI Components**: Custom Markdown renderer

## 🚀 Features

### Core Features
- **Dual Itinerary System**: Both popular tourist and off-beat travel plans
- **Comprehensive Planning**:
  - Day-by-day detailed itinerary
  - Accommodation options with pricing
  - Attractions and activities
  - Restaurant recommendations
  - Transportation details
  - Weather information
  - Cost breakdown

### Technical Features
- Real-time data integration
- Modular architecture
- Environment-based configuration
- Clean Markdown output

## 🔄 Workflow

### Happy Flow ✅
1. **User Input**
   - User enters travel query (e.g., "Plan a 3-day trip to Rishikesh")
   - Submits the request through Streamlit interface

2. **Request Processing**
   - Request sent to FastAPI backend
   - AI agent analyzes the query using LangGraph
   - System identifies required information components

3. **Data Collection**
   - Fetches weather data from OpenWeatherMap
   - Searches for places using Google Places API
   - Gets accommodation options and pricing
   - Calculates currency conversions if needed

4. **Response Generation**
   - AI compiles all gathered information
   - Creates a structured travel plan
   - Formats response in clean Markdown

5. **Result Display**
   - Formatted response sent back to Streamlit
   - User receives comprehensive travel plan
   - Plan includes all requested details and recommendations

### Negative Flow ❌
1. **API Unavailable**
   - ❌ Weather service is down
   - ✅ System continues with other information
   - ⚠️ Shows warning about missing weather data

2. **No Results Found**
   - ❌ No accommodations found for given filters
   - ✅ Suggests alternative locations or dates
   - ⚠️ Informs user about limited options

3. **Invalid Input**
   - ❌ User enters incomplete information
   - ✅ System requests missing details
   - ⚠️ Provides examples of valid input

4. **Rate Limiting**
   - ❌ API rate limit reached
   - ✅ Implements exponential backoff
   - ⚠️ Shows user-friendly error message

5. **Network Issues**
   - ❌ Connection lost during request
   - ✅ Automatically retries the request
   - ⚠️ Informs user about the retry

## 🛠️ Setup & Installation

### Prerequisites
- Python 3.8+
- API keys for all required services

### Installation
1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file with your API keys (use `.env.name` as a template)
4. Run the backend:
   ```bash
   uvicorn main:app --reload
   ```
5. Run the frontend:
   ```bash
   streamlit run streamlit_app.py
   ```

## 🧪 Testing

### Unit Tests
```bash
pytest tests/
```

### Integration Tests
```bash
python -m pytest tests/integration/
```

## 📝 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📧 Contact
For any queries, please contact [Your Email]

---
*Created with ❤️ by WorkPotato's Travel Agent*
