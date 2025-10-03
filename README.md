# TravelMate AI 🌍✈️

> **An intelligent travel planning assistant powered by Claude 3.5 Sonnet**

TravelMate AI is an AI-powered travel itinerary generator that creates personalized, detailed travel plans tailored to your preferences. Using Claude 3.5 Sonnet via OpenRouter AI, it generates comprehensive day-by-day itineraries with specific locations, activities, budget estimates, and practical travel tips.

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115-green.svg)](https://fastapi.tiangolo.com/)
[![Claude](https://img.shields.io/badge/Claude-3.5%20Sonnet-purple.svg)](https://www.anthropic.com/claude)
[![OpenRouter](https://img.shields.io/badge/OpenRouter-API-orange.svg)](https://openrouter.ai/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 🎯 Current Status: Day 2 - Claude AI Integration ✅

### ✨ Features
- ✅ **FastAPI Backend** - Modern, fast, production-ready API
- ✅ **Claude 3.5 Sonnet Integration** - Premium AI model via OpenRouter
- ✅ **Structured JSON I/O** - Type-safe requests and responses using Pydantic
- ✅ **Intelligent Error Handling** - Comprehensive error management and user-friendly messages
- ✅ **Environment Configuration** - Secure API key management with `.env` files
- ✅ **Personalized Itineraries** - Custom plans based on destination, duration, budget, and interests
- ✅ **Smart JSON Parsing** - Handles various response formats including markdown code blocks
- ✅ **Auto-Reload Development** - Fast iteration with hot-reload enabled

## 📋 Table of Contents
- [Features](#-features)
- [Quick Start](#-quick-start)
- [API Endpoints](#-api-endpoints)
- [Configuration](#-configuration)
- [Usage Examples](#-usage-examples)
- [Technical Details](#-technical-details)
- [Project Structure](#-project-structure)
- [Development Roadmap](#-development-roadmap)
- [Contributing](#-contributing)

## 🚀 Quick Start

### Prerequisites
- Python 3.13 or higher
- pip package manager
- OpenRouter API key (free signup at [openrouter.ai](https://openrouter.ai))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/taksh1507/TravelMate-AI.git
   cd TravelMate-AI
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Key**
   ```bash
   # Copy the example environment file
   copy .env.example .env
   
   # Edit .env and add your OpenRouter API key
   OPENAI_API_KEY=sk-or-v1-your-actual-api-key-here
   ```

4. **Run the application**
   ```bash
   uvicorn main:app --reload
   ```

5. **Access the API**
   - API Server: `http://localhost:8000`
   - Interactive Docs: `http://localhost:8000/docs`
   - Alternative Docs: `http://localhost:8000/redoc`

## 🔌 API Endpoints

### 1. Health Check
```http
GET /
```

**Response:**
```json
{
  "message": "Welcome to TravelMate AI!"
}
```

### 2. Generate Itinerary
```http
POST /generate-itinerary
Content-Type: application/json
```

**Request Body:**
```json
{
  "destination": "Paris",
  "days": 5,
  "budget": "medium",
  "interests": ["culture", "food", "history"]
}
```

**Parameters:**
| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `destination` | string | Travel destination | `"Paris"`, `"Tokyo"`, `"Bali"` |
| `days` | integer | Number of days | `3`, `7`, `14` |
| `budget` | string | Budget level | `"low"`, `"medium"`, `"high"` |
| `interests` | array | List of interests | `["adventure", "culture", "food"]` |

**Success Response (200 OK):**
```json
{
  "title": "5-Day Cultural Journey in Paris",
  "summary": "Immerse yourself in Parisian culture...",
  "days": [
    {
      "day": 1,
      "morning": "Visit the Louvre Museum...",
      "afternoon": "Stroll through Tuileries Garden...",
      "evening": "Dinner at a traditional bistro..."
    }
  ],
  "estimated_budget": {
    "flights": "$800",
    "hotels": "$600",
    "food": "$300",
    "activities": "$200",
    "total": "$1,900"
  },
  "tips": [
    "Purchase a Paris Museum Pass for savings",
    "Use the Metro for efficient transportation"
  ]
}
```

**Error Response:**
```json
{
  "error": "Unable to generate itinerary at the moment"
}
```

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
# OpenRouter API Key (Required)
OPENAI_API_KEY=sk-or-v1-your-api-key-here
```

**Getting Your API Key:**
1. Sign up at [OpenRouter](https://openrouter.ai/keys)
2. Generate a new API key
3. Copy the key to your `.env` file

**Note:** OpenRouter offers both free and paid models. Claude 3.5 Sonnet is a premium model with affordable pay-as-you-go pricing.

## 💡 Usage Examples

### Using the Interactive Swagger UI (Recommended)
1. Navigate to `http://localhost:8000/docs`
2. Click on **POST /generate-itinerary**
3. Click **"Try it out"**
4. Enter your request data
5. Click **"Execute"**

### Using cURL (PowerShell)

**Example 1: Adventure Trip to Manali**
```powershell
curl -X POST http://localhost:8000/generate-itinerary `
  -H "Content-Type: application/json" `
  -d '{
    \"destination\": \"Manali\",
    \"days\": 5,
    \"budget\": \"medium\",
    \"interests\": [\"adventure\", \"trekking\", \"nature\", \"photography\"]
  }'
```

**Example 2: Cultural Trip to Paris**
```powershell
curl -X POST http://localhost:8000/generate-itinerary `
  -H "Content-Type: application/json" `
  -d '{
    \"destination\": \"Paris\",
    \"days\": 7,
    \"budget\": \"high\",
    \"interests\": [\"art\", \"culture\", \"food\", \"history\"]
  }'
```

**Example 3: Beach Vacation in Bali**
```powershell
curl -X POST http://localhost:8000/generate-itinerary `
  -H "Content-Type: application/json" `
  -d '{
    \"destination\": \"Bali\",
    \"days\": 10,
    \"budget\": \"low\",
    \"interests\": [\"beaches\", \"temples\", \"wellness\", \"surfing\"]
  }'
```

### Using Python Requests
```python
import requests
import json

url = "http://localhost:8000/generate-itinerary"
data = {
    "destination": "Tokyo",
    "days": 7,
    "budget": "medium",
    "interests": ["technology", "food", "culture", "shopping"]
}

response = requests.post(url, json=data)
itinerary = response.json()

print(json.dumps(itinerary, indent=2))
```

### Using JavaScript/Fetch
```javascript
const generateItinerary = async () => {
  const response = await fetch('http://localhost:8000/generate-itinerary', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      destination: 'Dubai',
      days: 5,
      budget: 'high',
      interests: ['luxury', 'shopping', 'architecture', 'desert']
    })
  });
  
  const itinerary = await response.json();
  console.log(itinerary);
};

generateItinerary();
```

## 📁 Project Structure
```
TravelMate-AI/
├── 📄 main.py              # FastAPI application with Claude integration
├── 📄 requirements.txt     # Python dependencies
├── 📄 .env                 # Environment variables (NOT in git)
├── 📄 .env.example         # Example environment configuration
├── 📄 .gitignore          # Git ignore rules
└── 📄 README.md           # Project documentation
```

## 🔧 Technical Details

### Technology Stack
| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Backend Framework** | FastAPI 0.115+ | High-performance async API framework |
| **AI Model** | Claude 3.5 Sonnet | Premium language model for travel planning |
| **API Gateway** | OpenRouter | Unified API access to multiple AI models |
| **Server** | Uvicorn | ASGI server with hot-reload support |
| **Validation** | Pydantic | Type-safe data validation |
| **Environment** | python-dotenv | Secure environment variable management |

### AI Configuration
```python
Model: anthropic/claude-3.5-sonnet
Temperature: 0.7           # Balanced creativity
Max Tokens: 1500          # Detailed responses
Base URL: https://openrouter.ai/api/v1
```

**Why Claude 3.5 Sonnet?**
- 🧠 **Superior Reasoning** - Excellent for complex travel planning
- 🎯 **Detail-Oriented** - Provides specific locations and practical advice
- 🌍 **Cultural Knowledge** - Deep understanding of global destinations
- 📝 **Structured Output** - Reliably follows JSON format requirements
- ⚡ **Fast Response** - Quick generation for real-time applications

### Error Handling
The API implements comprehensive error handling:

| Error Type | HTTP Status | Response |
|------------|-------------|----------|
| Missing API Key | 200 | `{"error": "API key not configured"}` |
| Authentication Failed | 200 | `{"error": "Authentication failed"}` |
| Rate Limit Exceeded | 200 | `{"error": "Rate limit reached"}` |
| Invalid JSON | 200 | `{"error": "Invalid response format"}` |
| Generic Error | 200 | `{"error": "Please try again"}` |

**Features:**
- ✅ Graceful degradation
- ✅ User-friendly error messages
- ✅ Detailed server-side logging
- ✅ Smart JSON extraction from various formats
- ✅ Retry logic support

## 🗺️ Development Roadmap

### Phase 1: Backend Foundation ✅ (Completed)
- [x] FastAPI project setup
- [x] Request/response models with Pydantic
- [x] Root and itinerary endpoints
- [x] Git repository initialization
- [x] Documentation and README

### Phase 2: AI Integration ✅ (Completed)
- [x] OpenRouter API integration
- [x] Claude 3.5 Sonnet implementation
- [x] Environment variable management
- [x] Comprehensive error handling
- [x] Smart JSON parsing
- [x] Production-ready API

### Phase 3: Frontend Development 🔄 (Next)
- [ ] React/Next.js frontend
- [ ] Modern UI with Tailwind CSS
- [ ] Interactive itinerary display
- [ ] Form validation and user input
- [ ] Loading states and animations
- [ ] Responsive design

### Phase 4: Enhanced Features � (Future)
- [ ] User authentication
- [ ] Save and share itineraries
- [ ] PDF export functionality
- [ ] Multiple AI model support
- [ ] Budget calculator
- [ ] Weather integration
- [ ] Flight and hotel search
- [ ] Map integration

### Phase 5: Deployment 🚀 (Future)
- [ ] Docker containerization
- [ ] CI/CD pipeline
- [ ] Cloud deployment (AWS/Vercel)
- [ ] Domain and SSL setup
- [ ] Performance monitoring
- [ ] Analytics integration

## 💰 Cost & Pricing

### OpenRouter Pricing (Claude 3.5 Sonnet)
- **Input**: ~$3.00 per million tokens
- **Output**: ~$15.00 per million tokens
- **Typical Request**: $0.01 - $0.05 per itinerary
- **Free Credits**: Available for new users

**Cost Optimization Tips:**
- Use smaller `max_tokens` for shorter trips
- Cache common requests (coming soon)
- Consider free models for development/testing

### Alternative Models on OpenRouter

| Model | Cost | Best For |
|-------|------|----------|
| Claude 3.5 Sonnet | Paid | Production (best quality) |
| Meta Llama 3.2 | Free | Development/testing |
| Google Gemini Flash | Free | Budget-friendly alternative |
| GPT-4 Turbo | Paid | Alternative premium option |

## 🔒 Security & Best Practices

### API Key Security
⚠️ **Critical Security Guidelines:**
- ✅ Never commit `.env` files to version control
- ✅ Use `.env.example` as a template only
- ✅ Rotate keys immediately if exposed
- ✅ Use environment-specific keys (dev/prod)
- ✅ Monitor API usage regularly
- ❌ Never share keys in screenshots or logs
- ❌ Don't hardcode keys in source code

### Production Considerations
- Use HTTPS in production
- Implement rate limiting
- Add request authentication
- Enable CORS properly
- Monitor error rates
- Set up logging and alerting

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### How to Contribute
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guide
- Add docstrings to functions
- Include type hints
- Write descriptive commit messages
- Test your changes thoroughly

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Taksh Gandhi**
- GitHub: [@taksh1507](https://github.com/taksh1507)
- Email: takshgandhi4@gmail.com

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) - Modern web framework
- [Anthropic](https://www.anthropic.com/) - Claude AI model
- [OpenRouter](https://openrouter.ai/) - AI model access platform
- [Uvicorn](https://www.uvicorn.org/) - ASGI server

## 📞 Support

If you encounter any issues or have questions:
- 🐛 [Report bugs](https://github.com/taksh1507/TravelMate-AI/issues)
- 💡 [Request features](https://github.com/taksh1507/TravelMate-AI/issues)
- 📧 Email: takshgandhi4@gmail.com

---

<div align="center">

**Made with ❤️ for travelers around the world**

⭐ Star this repo if you find it helpful!

</div>
