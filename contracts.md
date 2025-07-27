# Portfolio API Contracts

## Overview
This document defines the API contracts for the Portfolio application. The frontend is currently using mock data from `/app/frontend/src/data/mock.js` that needs to be replaced with backend APIs.

## Mock Data Structure
The mock data contains:
- `about`: Personal description and bio
- `projects`: Array of project objects with title, description, highlights, technologies
- `skills`: Array of skill categories with items
- `achievements`: Array of achievement objects
- `certifications`: Array of certification objects  
- `contact`: Contact information object
- `education`: Education details object

## API Endpoints to Implement

### 1. GET /api/portfolio/profile
**Purpose**: Get complete portfolio profile information
**Response**: 
```json
{
  "about": "string",
  "contact": {
    "email": "string",
    "phone": "string", 
    "linkedin": "string"
  },
  "education": {
    "degree": "string",
    "university": "string",
    "period": "string"
  }
}
```

### 2. GET /api/portfolio/projects
**Purpose**: Get all projects
**Response**: Array of project objects
```json
[
  {
    "id": "string",
    "title": "string",
    "description": "string",
    "highlights": ["string"],
    "technologies": ["string"],
    "created_at": "datetime"
  }
]
```

### 3. GET /api/portfolio/skills
**Purpose**: Get all skills categorized
**Response**: Array of skill category objects
```json
[
  {
    "category": "string",
    "items": ["string"]
  }
]
```

### 4. GET /api/portfolio/achievements
**Purpose**: Get all achievements
**Response**: Array of achievement objects
```json
[
  {
    "id": "string",
    "title": "string", 
    "description": "string",
    "created_at": "datetime"
  }
]
```

### 5. GET /api/portfolio/certifications
**Purpose**: Get all certifications
**Response**: Array of certification objects
```json
[
  {
    "id": "string",
    "name": "string",
    "issuer": "string",
    "created_at": "datetime"
  }
]
```

## MongoDB Collections

### 1. profiles
```json
{
  "_id": "ObjectId",
  "about": "string",
  "contact": {
    "email": "string",
    "phone": "string",
    "linkedin": "string"
  },
  "education": {
    "degree": "string", 
    "university": "string",
    "period": "string"
  },
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

### 2. projects
```json
{
  "_id": "ObjectId",
  "title": "string",
  "description": "string", 
  "highlights": ["string"],
  "technologies": ["string"],
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

### 3. skills
```json
{
  "_id": "ObjectId",
  "category": "string",
  "items": ["string"],
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

### 4. achievements
```json
{
  "_id": "ObjectId",
  "title": "string",
  "description": "string",
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

### 5. certifications
```json
{
  "_id": "ObjectId",
  "name": "string",
  "issuer": "string", 
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

## Integration Plan

### Backend Implementation
1. Create MongoDB models for all collections
2. Implement API endpoints with proper error handling
3. Seed database with current mock data
4. Add proper validation and response formatting

### Frontend Integration
1. Create API service layer in `/app/frontend/src/services/api.js`
2. Replace mock data imports with API calls
3. Add loading states and error handling
4. Update components to handle async data loading

## Data Seeding
The backend will include a seeding script that populates the database with the current mock data to ensure no data loss during the transition.