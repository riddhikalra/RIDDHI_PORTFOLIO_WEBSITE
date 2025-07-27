import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
from pathlib import Path
import logging

# Load environment variables
ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# MongoDB connection
mongo_url = os.environ.get('MONGO_URL')
if not mongo_url:
    raise ValueError("MONGO_URL environment variable is not set")

client = AsyncIOMotorClient(mongo_url)
db = client[os.environ.get('DB_NAME', 'portfolio')]

# Collection references
profiles_collection = db.profiles
projects_collection = db.projects
skills_collection = db.skills
achievements_collection = db.achievements
certifications_collection = db.certifications

async def init_database():
    """Initialize database with indexes and setup"""
    try:
        # Create indexes
        await profiles_collection.create_index("created_at")
        await projects_collection.create_index("created_at")
        await skills_collection.create_index("category")
        await achievements_collection.create_index("created_at")
        await certifications_collection.create_index("created_at")
        
        logger.info("Database initialized successfully")
    except Exception as e:
        logger.error(f"Failed to initialize database: {e}")
        raise

async def close_database():
    """Close database connection"""
    client.close()
    logger.info("Database connection closed")