import asyncio
from database import (
    profiles_collection, projects_collection, skills_collection,
    achievements_collection, certifications_collection, init_database
)
from models import Profile, Project, SkillCategory, Achievement, Certification
import logging

logger = logging.getLogger(__name__)

# Mock data to seed the database
MOCK_DATA = {
    "profile": {
        "about": "I'm a Solution Developer with over 2.5 years of experience specializing in Java-based middleware solutions, API development, and system integration. My technical toolkit includes Apache Camel, Spring Boot, and REST/SOAP services, with a proven track record of delivering scalable, secure, and business-aligned microservices. Currently, I'm contributing to enterprise-grade integration systems at Tata Technologies, where I've independently developed and deployed multiple middleware services for critical business workflows.",
        "contact": {
            "email": "riddhikalra0209@gmail.com",
            "phone": "+91 8360230427",
            "linkedin": "linkedin.com/in/riddhikalra"
        },
        "education": {
            "degree": "B.E. in Computer Science and Engineering",
            "university": "Chitkara University",
            "period": "2019 – 2023"
        }
    },
    "projects": [
        {
            "title": "Middleware API Suite for Manufacturing Platform",
            "description": "Designed and developed over 10 standalone middleware services for internal business systems, focusing on enterprise-grade integration and workflow automation.",
            "highlights": [
                "Automated workflow schedulers using Camel DSL",
                "Optimized database interactions for high performance",
                "Implemented secure authentication and authorization",
                "Built scalable microservices architecture"
            ],
            "technologies": ["Apache Camel", "Java 8/17", "REST/SOAP", "Spring Boot", "MySQL"]
        },
        {
            "title": "Microservices with Spring Boot",
            "description": "Built high-performance microservices with advanced caching strategies and secure authentication systems for enterprise applications.",
            "highlights": [
                "Implemented JDG (Infinispan) caching for optimal performance",
                "Developed authentication APIs secured with Keycloak",
                "Created RESTful services following best practices",
                "Integrated with multiple external systems"
            ],
            "technologies": ["Spring Boot", "JDG", "Infinispan", "Keycloak", "REST API", "Java"]
        },
        {
            "title": "Platform Migration: FUSE to Camel",
            "description": "Led core development efforts in migrating enterprise services from RedHat FUSE to Apache Camel, ensuring zero downtime and improved performance.",
            "highlights": [
                "Collaborated directly with RedHat SMEs",
                "Maintained system stability during migration",
                "Improved overall system performance by 30%",
                "Provided technical leadership throughout the process"
            ],
            "technologies": ["RedHat FUSE", "Apache Camel", "Java", "Enterprise Integration", "Migration"]
        }
    ],
    "skills": [
        {
            "category": "Programming Languages",
            "items": ["Java (8/11/17)", "JavaScript", "SQL"]
        },
        {
            "category": "Frameworks & Technologies",
            "items": ["Spring Boot", "Apache Camel", "J2EE", "Hibernate", "React", "Node.js"]
        },
        {
            "category": "Tools & Platforms",
            "items": ["Git", "Jenkins", "ArgoCD", "CI/CD"]
        },
        {
            "category": "Concepts & Architecture",
            "items": ["REST/SOAP APIs", "Microservices Architecture", "Data Structures"]
        }
    ],
    "achievements": [
        {
            "title": "Champion of the Month",
            "description": "Recognized for outstanding project contributions and technical excellence at Tata Technologies"
        },
        {
            "title": "Snowflake Essentials Badges",
            "description": "Mastered essentials of data warehousing and cost optimization techniques"
        },
        {
            "title": "Enterprise Integration Expert",
            "description": "Successfully led multiple critical middleware integrations with zero downtime"
        }
    ],
    "certifications": [
        {
            "name": "Introduction to UI Design",
            "issuer": "Coursera"
        },
        {
            "name": "SQL Essential Training",
            "issuer": "LinkedIn Learning"
        },
        {
            "name": "Introduction to Cybersecurity",
            "issuer": "Cisco"
        },
        {
            "name": "Web Development Fundamentals",
            "issuer": "Various Platforms"
        }
    ]
}

async def clear_collections():
    """Clear all collections"""
    try:
        await profiles_collection.delete_many({})
        await projects_collection.delete_many({})
        await skills_collection.delete_many({})
        await achievements_collection.delete_many({})
        await certifications_collection.delete_many({})
        logger.info("All collections cleared")
    except Exception as e:
        logger.error(f"Error clearing collections: {e}")
        raise

async def seed_profile():
    """Seed profile data"""
    try:
        profile = Profile(**MOCK_DATA["profile"])
        await profiles_collection.insert_one(profile.dict())
        logger.info("Profile seeded successfully")
    except Exception as e:
        logger.error(f"Error seeding profile: {e}")
        raise

async def seed_projects():
    """Seed projects data"""
    try:
        projects = [Project(**project_data) for project_data in MOCK_DATA["projects"]]
        await projects_collection.insert_many([project.dict() for project in projects])
        logger.info(f"Seeded {len(projects)} projects")
    except Exception as e:
        logger.error(f"Error seeding projects: {e}")
        raise

async def seed_skills():
    """Seed skills data"""
    try:
        skills = [SkillCategory(**skill_data) for skill_data in MOCK_DATA["skills"]]
        await skills_collection.insert_many([skill.dict() for skill in skills])
        logger.info(f"Seeded {len(skills)} skill categories")
    except Exception as e:
        logger.error(f"Error seeding skills: {e}")
        raise

async def seed_achievements():
    """Seed achievements data"""
    try:
        achievements = [Achievement(**achievement_data) for achievement_data in MOCK_DATA["achievements"]]
        await achievements_collection.insert_many([achievement.dict() for achievement in achievements])
        logger.info(f"Seeded {len(achievements)} achievements")
    except Exception as e:
        logger.error(f"Error seeding achievements: {e}")
        raise

async def seed_certifications():
    """Seed certifications data"""
    try:
        certifications = [Certification(**cert_data) for cert_data in MOCK_DATA["certifications"]]
        await certifications_collection.insert_many([cert.dict() for cert in certifications])
        logger.info(f"Seeded {len(certifications)} certifications")
    except Exception as e:
        logger.error(f"Error seeding certifications: {e}")
        raise

async def seed_database():
    """Seed entire database"""
    try:
        await init_database()
        await clear_collections()
        await seed_profile()
        await seed_projects()
        await seed_skills()
        await seed_achievements()
        await seed_certifications()
        logger.info("Database seeded successfully")
    except Exception as e:
        logger.error(f"Error seeding database: {e}")
        raise

if __name__ == "__main__":
    asyncio.run(seed_database())