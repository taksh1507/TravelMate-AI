# TravelMate AI 🌍✈️

An AI-powered travel itinerary generator that helps users plan their perfect trip using Claude 3.5 Sonnet via OpenRouter AI.

## Current Status: Day 2 - Claude AI Integration ✅

### Features
- ✅ FastAPI backend with RESTful endpoints
- ✅ OpenRouter AI integration with **Claude 3.5 Sonnet** (Anthropic's flagship model)
- ✅ Structured JSON request/response using Pydantic
- ✅ Comprehensive error handling
- ✅ Environment variable management for API keys
- ✅ Personalized itineraries based on destination, duration, budget, and interests

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

### 1. Clone the Repository (if not already done)
```bash
git clone https://github.com/taksh1507/TravelMate-AI.git
cd TravelMate-AI
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure OpenRouter API Key
1. Get your API key from [OpenRouter](https://openrouter.ai/keys)
2. Copy `.env.example` to `.env`:
   ```bash
   copy .env.example .env
   ```
3. Open `.env` and add your OpenRouter API key:
   ```
   OPENAI_API_KEY=sk-or-v1-your-actual-api-key-here
   ```

**Note**: OpenRouter provides free access to many models including Google Gemini 2.0 Flash!

### 4. Run the Application
```bash
uvicorn main:app --reload
```

The server will start at: `http://localhost:8000`

### 3. Test the API

#### Option A: Using Interactive API Documentation
- Visit: `http://localhost:8000/docs` (Swagger UI)
- Try the `/generate-itinerary` endpoint with sample data

#### Option B: Using curl (PowerShell)
```powershell
# Test root endpoint
curl http://localhost:8000

# Test AI-powered itinerary generation
curl -X POST http://localhost:8000/generate-itinerary -H "Content-Type: application/json" -d '{\"destination\":\"Paris\",\"days\":5,\"budget\":\"medium\",\"interests\":[\"culture\",\"food\",\"history\"]}'
```

#### Sample Request:
```json
{
  "destination": "Tokyo",
  "days": 7,
  "budget": "medium",
  "interests": ["technology", "food", "culture"]
}
```

#### Sample Response:
```json
{
  "title": "7-Day Tech & Culture Journey in Tokyo",
  "summary": "Experience the perfect blend of cutting-edge technology and traditional culture...",
  "days": [
    {
      "day": 1,
      "morning": "Visit Senso-ji Temple in Asakusa...",
      "afternoon": "Explore Akihabara's electronics district...",
      "evening": "Dinner at a traditional izakaya..."
    }
  ],
  "estimated_budget": {
    "flights": "$1,200",
    "hotels": "$840",
    "food": "$420",
    "activities": "$350",
    "total": "$2,810"
  },
  "tips": [
    "Purchase a JR Pass for unlimited train travel",
    "Download Google Translate for easier navigation",
    "Bring cash as many places don't accept cards"
  ]
}
```

## Project Structure
```
TravelMate-AI/
├── main.py              # FastAPI application with OpenAI integration
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (API keys) - NOT in git
├── .env.example         # Example environment file
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## Technical Details

### API Configuration
- **Provider**: OpenRouter AI (OpenAI-compatible API)
- **Model**: Claude 3.5 Sonnet (Anthropic's most capable model)
- **Temperature**: 0.7 (balanced creativity)
- **Max Tokens**: 1500 (optimal for detailed, high-quality itineraries)
- **Response Format**: Structured JSON with intelligent parsing
- **Why Claude?**: Exceptional reasoning, detailed responses, and excellent instruction-following

### Error Handling
The API includes comprehensive error handling for:
- Missing API key
- API service errors
- Rate limit errors
- Authentication errors
- JSON parsing errors (with intelligent extraction from markdown)
- Unexpected errors

All errors return a consistent format:
```json
{
  "error": "Unable to generate itinerary at the moment"
}
```

## Roadmap

### Day 1: ✅ Project Foundation (Complete)
- Basic FastAPI setup
- Dummy endpoints with sample responses
- Git repository setup

### Day 2: ✅ Claude AI Integration (Complete)
- OpenRouter AI with Claude 3.5 Sonnet integration
- Premium AI-powered itinerary generation
- Environment variable management
- Comprehensive error handling
- Structured JSON responses with intelligent parsing

### Day 3: 🔄 Coming Soon
- Build frontend (React/Vue/HTML)
- Connect frontend to backend
- Styling and user experience
- Deployment

## Notes
- **Security**: Never commit your `.env` file with API keys to git
- **Cost**: OpenRouter offers pay-as-you-go pricing for Claude 3.5 Sonnet (very affordable)
- **Model**: Currently using `anthropic/claude-3.5-sonnet` - premium quality for travel planning
- **Alternative Models**: You can switch to other models on OpenRouter:
  - Free options: `meta-llama/llama-3.2-3b-instruct:free`, `google/gemini-2.0-flash-exp:free`
  - Premium options: `openai/gpt-4`, `google/gemini-pro-1.5`
- **Why Claude?**: Best-in-class for detailed planning, cultural insights, and practical travel advice
- **Rate Limits**: Based on your OpenRouter credits
- **Frontend**: API is designed to be frontend-agnostic - use with any frontend framework

## API Key Security
⚠️ **Important**: 
- Your `.env` file contains sensitive API keys
- It is automatically ignored by git (listed in `.gitignore`)
- Never share your API key publicly
- Rotate your API key if accidentally exposed
