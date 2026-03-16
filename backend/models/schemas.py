from pydantic import BaseModel, Field 
from typing import Optional 
from datetime import datetime

# This is what recruiter sens when creating a job
class JobDescriptionCreate(BaseModel):
    # (...) means required can't be empty.
    title: str = Field(..., description = "Job title")
    description: str = Field(..., description = "Full job description")
    # (default=[]) if not provided, use empty lists
    required_skills: list[str] = Field(default=[])
    nice_to_have: list[str] = Field(default=[])
    experience_years: Optional[int] = Field(None)

# This is what we send back after a job is created 
class JobsDescriptionResponse(BaseModel):
    job_id: str
    title: str
    description: str 
    required_skills: list[str]
    nice_to_have: list[str]
    experience_years: Optional[int]
    created_at: datetime

# Result for one candidate after analysis
class CadidateScore(BaseModel):
    candidate_id: str
    name: str
    email: Optional[str]
    filename: str
    overall_score: float = Field(..., ge=0, le=100)
    skills_match_score: float = Field(..., ge=0, le=100)
    experience_score: float = Field(..., ge=0, le=100)
    semantic_similarity_score: float = Field(..., ge=0, le=100)
    strengths: list[str]
    gaps: list[str]
    summary: str
    interview_questions: list[str]

# Full response when ranking is complete
class RankingResponse(BaseModel):
    job_id: str
    job_title: str
    total_candidates: int
    ranked_candidates: list[CadidateScore]
    processing_time_seconds: float


class UploadResponse(BaseModel):
    job_id: str
    uploaded_count: int
    failed_files: list[str]
    message: str


class ParsedResume(BaseModel):
    candidate_id: str
    filename: str
    raw_text: str
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None

class EmbeddedCandidate(BaseModel):
    candidate_id: str
    filename: str
    raw_text: str
    name: Optional[str] = None
    email: Optional[str] = None
    embedding: list[float]

