"""
TravelMate AI - FastAPI Backend
Main entry point for the TravelMate AI travel itinerary generator.
Day 2: OpenAI integration for AI-powered itinerary generation
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from openai import OpenAI
import os
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize FastAPI application
app = FastAPI(
    title="TravelMate AI",
    description="AI-powered travel itinerary generator using OpenRouter",
    version="2.0.0"
)

# Configure OpenRouter API
# OpenRouter uses OpenAI-compatible API, but with different base URL
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client with OpenRouter configuration
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

# Validate that API key is set
if not api_key:
    print("⚠️  WARNING: OPENAI_API_KEY not found in environment variables!")
    print("Please create a .env file with your OpenRouter API key.")
else:
    print("✅ OpenRouter API key configured successfully!")


# Pydantic model for the itinerary request
# This defines the structure of the JSON body that clients must send
class ItineraryRequest(BaseModel):
    destination: str  # Where the user wants to travel
    days: int  # Number of days for the trip
    budget: str  # Budget range (e.g., "low", "medium", "high")
    interests: List[str]  # List of user interests (e.g., ["adventure", "culture", "food"])


# Root endpoint - Simple welcome message
@app.get("/")
async def root():
    """
    Root endpoint that returns a welcome message.
    This is useful for health checks and API status verification.
    """
    return {"message": "Welcome to TravelMate AI!"}


# Generate itinerary endpoint - Main functionality with OpenAI integration
@app.post("/generate-itinerary")
async def generate_itinerary(request: ItineraryRequest):
    """
    Generate a travel itinerary based on user input using OpenAI GPT-4.
    
    This endpoint uses OpenAI's Chat API to generate personalized travel itineraries
    based on the user's destination, trip duration, budget, and interests.
    
    Args:
        request: ItineraryRequest object containing destination, days, budget, and interests
    
    Returns:
        AI-generated itinerary with day-by-day activities, budget breakdown, and travel tips
    
    Raises:
        HTTPException: If OpenAI API fails or returns invalid response
    """
    
    # Check if API key is configured
    if not api_key:
        return {
            "error": "Unable to generate itinerary at the moment. API key not configured."
        }
    
    try:
        # Prepare the system prompt that defines TravelMate AI's behavior
        system_prompt = """You are TravelMate AI, an expert travel planning assistant.
Your role is to create detailed, personalized travel itineraries based on user preferences.

IMPORTANT: You must ALWAYS respond with valid JSON only, no additional text.

Your response must follow this exact structure:
{
  "title": "Trip title (e.g., '5-Day Cultural Adventure in Paris')",
  "summary": "Brief 2-3 sentence overview of the trip",
  "days": [
    {
      "day": 1,
      "morning": "Detailed morning activity with specific locations and tips",
      "afternoon": "Detailed afternoon activity with specific locations and tips",
      "evening": "Detailed evening activity with specific locations and tips"
    }
  ],
  "estimated_budget": {
    "flights": "Estimated flight cost (e.g., '$800')",
    "hotels": "Estimated hotel cost (e.g., '$600')",
    "food": "Estimated food cost (e.g., '$300')",
    "activities": "Estimated activities cost (e.g., '$200')",
    "total": "Total estimated cost (e.g., '$1,900')"
  },
  "tips": [
    "Practical tip 1",
    "Practical tip 2",
    "Practical tip 3"
  ]
}

Consider the user's budget level and interests when planning activities.
Provide realistic budget estimates in USD.
Include specific locations, restaurants, and attractions.
Make the itinerary practical and actionable."""

        # Create user message with trip details
        user_message = f"""Create a {request.days}-day travel itinerary for {request.destination}.

Budget Level: {request.budget}
Interests: {', '.join(request.interests)}

Please provide a detailed day-by-day plan with specific activities, locations, and practical tips."""

        # Call OpenRouter API (OpenAI-compatible)
        # Using Claude 3.5 Sonnet - excellent for detailed travel planning
        response = client.chat.completions.create(
            model="anthropic/claude-3.5-sonnet",  # Claude 3.5 Sonnet via OpenRouter
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ],
            temperature=0.7,  # Balanced creativity and consistency
            max_tokens=1500,   # Increased for Claude's detailed responses
        )
        
        # Extract the AI-generated content
        ai_response = response.choices[0].message.content
        
        # Parse the JSON response
        try:
            # Try to find JSON in the response (in case model adds extra text)
            # First, try direct parsing
            itinerary_data = json.loads(ai_response)
            return itinerary_data
        except json.JSONDecodeError:
            # If direct parsing fails, try to extract JSON from markdown code blocks
            import re
            json_match = re.search(r'```(?:json)?\s*(\{.*?\})\s*```', ai_response, re.DOTALL)
            if json_match:
                try:
                    itinerary_data = json.loads(json_match.group(1))
                    return itinerary_data
                except:
                    pass
            
            # If still fails, look for any JSON-like structure
            json_match = re.search(r'\{.*\}', ai_response, re.DOTALL)
            if json_match:
                try:
                    itinerary_data = json.loads(json_match.group(0))
                    return itinerary_data
                except:
                    pass
            
            # If all parsing fails, return error
            print(f"Failed to parse AI response: {ai_response[:200]}...")
            return {
                "error": "Unable to generate itinerary at the moment. Invalid response format."
            }
    
    except Exception as e:
        # Handle any errors
        error_message = str(e)
        print(f"API Error: {error_message}")
        
        # Provide user-friendly error messages
        if "authentication" in error_message.lower() or "api key" in error_message.lower():
            return {
                "error": "Unable to generate itinerary at the moment. Authentication failed."
            }
        elif "rate limit" in error_message.lower() or "quota" in error_message.lower():
            return {
                "error": "Unable to generate itinerary at the moment. Rate limit reached."
            }
        else:
            return {
                "error": "Unable to generate itinerary at the moment. Please try again."
            }


# Run the application
# To start the server, use: uvicorn main:app --reload
# The --reload flag enables auto-reload during development
if __name__ == "__main__":
    import uvicorn
    # Run the server on localhost:8000
    uvicorn.run(app, host="0.0.0.0", port=8000)
