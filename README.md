# TravelMate AI 🌍✈️

An AI-powered travel itinerary generator that helps users plan their perfect trip.

## Day 1: Project Foundation

This is the initial setup with a FastAPI backend skeleton.

### Features (Current)
- ✅ FastAPI backend with two endpoints
- ✅ Root endpoint for health checks
- ✅ `/generate-itinerary` endpoint with dummy JSON response
- ✅ Structured request/response models using Pydantic

### Endpoints

#### 1. Root Endpoint
```
GET /
Response: {"message": "Welcome to TravelMate AI!"}
```

#### 2. Generate Itinerary
```
POST /generate-itinerary
Content-Type: application/json

Request Body:
{
  "destination": "Paris",
  "days": 5,
  "budget": "medium",
  "interests": ["culture", "food", "history"]
}

Response: Returns a sample itinerary (dummy data for now)
```

## Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Application
```bash
uvicorn main:app --reload
```

The server will start at: `http://localhost:8000`

### 3. Test the API

#### Option A: Using your browser
- Visit: `http://localhost:8000` (for the root endpoint)
- Visit: `http://localhost:8000/docs` (for interactive API documentation)

#### Option B: Using curl (PowerShell)
```powershell
# Test root endpoint
curl http://localhost:8000

# Test generate-itinerary endpoint
curl -X POST http://localhost:8000/generate-itinerary -H "Content-Type: application/json" -d '{\"destination\":\"Paris\",\"days\":5,\"budget\":\"medium\",\"interests\":[\"culture\",\"food\"]}'
```

## Project Structure
```
TravelMate-AI/
├── main.py              # FastAPI application entry point
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Roadmap

### Day 1: ✅ Project Foundation (Current)
- Basic FastAPI setup
- Dummy endpoints with sample responses

### Day 2: 🔄 Coming Soon
- Integrate OpenAI API
- Generate AI-powered itineraries
- Add environment variable management

### Day 3: 🔄 Coming Soon
- Build frontend (React/Vue/HTML)
- Connect frontend to backend
- Styling and user experience

## Notes
- Currently using dummy data for testing the API structure
- OpenAI integration will be added in the next phase
- Frontend development will follow after backend is complete
