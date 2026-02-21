"""Router for learner endpoints."""

from fastapi import APIRouter

from datetime import datetime

from fastapi import Depends
from sqlmodel.ext.asyncio.session import AsyncSession

from app.database import get_session
from app.db.learners import read_learners, create_learner
from app.models.learner import Learner, LearnerCreate

router = APIRouter()

# ===
# PART A: GET endpoint
# ===


@router.get("/learners", response_model=list[Learner])
async def read_learners_endpoint(
    enrolled_after: datetime = None,
    session: AsyncSession = Depends(get_session),
):
    """Get all learners, optionally filtered by enrollment date."""
    return await read_learners(session, enrolled_after)

# Reference:
# items GET -> reads from items table, returns list[Item]
# learners GET -> reads from learners table, returns list[Learner]
# Query parameter: ?enrolled_after= filters learners by enrolled_at date

# ===
# PART B: POST endpoint
# ===

@router.post("/learners", response_model=Learner, status_code=201)
async def create_learner_endpoint(
    learner: LearnerCreate,
    session: AsyncSession = Depends(get_session),
):
    """Create a new learner."""
    return await create_learner(session, name=learner.name, email=learner.email)

# Reference:
# items POST -> creates a row in items table, accepts ItemCreate, returns Item with status 201
# learners POST -> creates a row in learners table, accepts LearnerCreate, returns Learner with status 201
