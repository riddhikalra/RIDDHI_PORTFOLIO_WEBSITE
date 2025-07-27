from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
import uuid

class ContactInfo(BaseModel):
    email: str
    phone: str
    linkedin: str

class EducationInfo(BaseModel):
    degree: str
    university: str
    period: str

class Profile(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    about: str
    contact: ContactInfo
    education: EducationInfo
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class ProfileCreate(BaseModel):
    about: str
    contact: ContactInfo
    education: EducationInfo

class Project(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    description: str
    highlights: List[str]
    technologies: List[str]
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class ProjectCreate(BaseModel):
    title: str
    description: str
    highlights: List[str]
    technologies: List[str]

class SkillCategory(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    category: str
    items: List[str]
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class SkillCategoryCreate(BaseModel):
    category: str
    items: List[str]

class Achievement(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    description: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class AchievementCreate(BaseModel):
    title: str
    description: str

class Certification(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    issuer: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class CertificationCreate(BaseModel):
    name: str
    issuer: str