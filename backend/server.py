from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging
from database import init_database, close_database
from portfolio_routes import router as portfolio_router
from seed_data import seed_database
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    logger.info("Starting up...")
    await init_database()
    
    # Check if database is empty and seed if needed
    from database import profiles_collection
    profile_count = await profiles_collection.count_documents({})
    if profile_count == 0:
        logger.info("Database is empty, seeding with initial data...")
        await seed_database()
    
    yield
    
    # Shutdown
    logger.info("Shutting down...")
    await close_database()

# Create FastAPI app
app = FastAPI(
    title="Portfolio API",
    description="API for Portfolio Management",
    version="1.0.0",
    lifespan=lifespan
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(portfolio_router)

# Health check endpoint
@app.get("/api/health")
async def health_check():
    return {"status": "healthy", "message": "Portfolio API is running"}

# Root endpoint
@app.get("/api/")
async def root():
    return {"message": "Portfolio API - Ready to serve your professional journey!"}