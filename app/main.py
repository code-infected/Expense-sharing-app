from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controllers import user_controller, expense_controller

# Create the FastAPI app instance
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins for testing
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

# Include the routers from your controllers
app.include_router(user_controller.router, prefix="/api/v1")
app.include_router(expense_controller.router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Welcome to the Daily Expenses Sharing API"}
