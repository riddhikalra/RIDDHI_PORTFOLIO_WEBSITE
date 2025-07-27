from fastapi import APIRouter, HTTPException
from typing import List
from models import (
    Profile, ProfileCreate, Project, ProjectCreate, 
    SkillCategory, SkillCategoryCreate, Achievement, AchievementCreate,
    Certification, CertificationCreate
)
from database import (
    profiles_collection, projects_collection, skills_collection,
    achievements_collection, certifications_collection
)
import logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/portfolio", tags=["portfolio"])

# Profile routes
@router.get("/profile", response_model=Profile)
async def get_profile():
    try:
        profile = await profiles_collection.find_one()
        if not profile:
            raise HTTPException(status_code=404, detail="Profile not found")
        return Profile(**profile)
    except Exception as e:
        logger.error(f"Error getting profile: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.post("/profile", response_model=Profile)
async def create_profile(profile_data: ProfileCreate):
    try:
        profile = Profile(**profile_data.dict())
        await profiles_collection.insert_one(profile.dict())
        return profile
    except Exception as e:
        logger.error(f"Error creating profile: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

# Project routes
@router.get("/projects", response_model=List[Project])
async def get_projects():
    try:
        projects = await projects_collection.find().sort("created_at", -1).to_list(100)
        return [Project(**project) for project in projects]
    except Exception as e:
        logger.error(f"Error getting projects: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.post("/projects", response_model=Project)
async def create_project(project_data: ProjectCreate):
    try:
        project = Project(**project_data.dict())
        await projects_collection.insert_one(project.dict())
        return project
    except Exception as e:
        logger.error(f"Error creating project: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

# Skills routes
@router.get("/skills", response_model=List[SkillCategory])
async def get_skills():
    try:
        skills = await skills_collection.find().sort("category", 1).to_list(100)
        return [SkillCategory(**skill) for skill in skills]
    except Exception as e:
        logger.error(f"Error getting skills: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.post("/skills", response_model=SkillCategory)
async def create_skill_category(skill_data: SkillCategoryCreate):
    try:
        skill_category = SkillCategory(**skill_data.dict())
        await skills_collection.insert_one(skill_category.dict())
        return skill_category
    except Exception as e:
        logger.error(f"Error creating skill category: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

# Achievements routes
@router.get("/achievements", response_model=List[Achievement])
async def get_achievements():
    try:
        achievements = await achievements_collection.find().sort("created_at", -1).to_list(100)
        return [Achievement(**achievement) for achievement in achievements]
    except Exception as e:
        logger.error(f"Error getting achievements: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.post("/achievements", response_model=Achievement)
async def create_achievement(achievement_data: AchievementCreate):
    try:
        achievement = Achievement(**achievement_data.dict())
        await achievements_collection.insert_one(achievement.dict())
        return achievement
    except Exception as e:
        logger.error(f"Error creating achievement: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

# Certifications routes
@router.get("/certifications", response_model=List[Certification])
async def get_certifications():
    try:
        certifications = await certifications_collection.find().sort("created_at", -1).to_list(100)
        return [Certification(**certification) for certification in certifications]
    except Exception as e:
        logger.error(f"Error getting certifications: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.post("/certifications", response_model=Certification)
async def create_certification(certification_data: CertificationCreate):
    try:
        certification = Certification(**certification_data.dict())
        await certifications_collection.insert_one(certification.dict())
        return certification
    except Exception as e:
        logger.error(f"Error creating certification: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")