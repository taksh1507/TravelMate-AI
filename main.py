"""
TravelMate AI - FastAPI Backend
Main entry point for the TravelMate AI travel itinerary generator.
Day 1: Basic FastAPI setup with dummy responses
"""

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

# Initialize FastAPI application
app = FastAPI(
    title="TravelMate AI",
    description="AI-powered travel itinerary generator",
    version="1.0.0"
)


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


# Generate itinerary endpoint - Main functionality
@app.post("/generate-itinerary")
async def generate_itinerary(request: ItineraryRequest):
    """
    Generate a travel itinerary based on user input.
    
    Currently returns dummy data for testing purposes.
    Later, this will be connected to OpenAI API for AI-generated itineraries.
    
    Args:
        request: ItineraryRequest object containing destination, days, budget, and interests
    
    Returns:
        A sample itinerary with day-by-day activities, budget breakdown, and travel tips
    """
    
    # TODO: In future iterations, this is where we'll integrate OpenAI API
    # For now, returning a dummy response to test the API structure
    
    dummy_response = {
        "title": "Sample Itinerary",
        "summary": "This is a test response",
        "days": [
            {
                "day": 1,
                "morning": "Sample activity",
                "afternoon": "Sample activity",
                "evening": "Sample activity"
            }
        ],
        "estimated_budget": {
            "flights": "$100",
            "hotels": "$200",
            "food": "$50",
            "activities": "$30",
            "total": "$380"
        },
        "tips": [
            "Sample tip 1",
            "Sample tip 2"
        ]
    }
    
    return dummy_response


# Run the application
# To start the server, use: uvicorn main:app --reload
# The --reload flag enables auto-reload during development
if __name__ == "__main__":
    import uvicorn
    # Run the server on localhost:8000
    uvicorn.run(app, host="0.0.0.0", port=8000)
