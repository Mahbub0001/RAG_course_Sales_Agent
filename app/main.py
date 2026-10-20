from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import Settings, get_settings
from app.db.session import get_session

app = FastAPI(title="Sales Agent")


@app.get("/health")
async def health(settings: Settings = Depends(get_settings)) -> dict[str, str]:
    return {
        "status": "ok",
        "app_name": settings.APP_NAME,
    }


@app.get("/health/db")
async def health_db(session: AsyncSession = Depends(get_session)) -> dict[str, str]:
    try:
        await session.execute(text("SELECT 1"))
        result = await session.execute(
            text("SELECT extversion FROM pg_extension WHERE extname = 'vector'")
        )
        vector_version = result.scalar_one_or_none()
    except SQLAlchemyError as exc:
        raise HTTPException(
            status_code=503,
            detail="Database health check failed",
        ) from exc

    if vector_version is None:
        raise HTTPException(
            status_code=503,
            detail={"database": "ok", "pgvector": "not installed"},
        )

    return {
        "database": "ok",
        "pgvector": "ok",
        "pgvector_version": vector_version,
    }