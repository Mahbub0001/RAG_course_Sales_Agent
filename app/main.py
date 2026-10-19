from fastapi import FastAPI,Depends
from app.core.config import Settings, get_settings

app = FastAPI(title="Sales Agent")

@app.get("/health")
async def health(settings:Settings=Depends(get_settings))->dict[str,str]:
    return{
        "status":"ok",
        "app name":settings.APP_NAME

    }

@app.get("/helth/db")
async def health_db(session:AsyncSession=Depends(get_settings))->dict[str,str]:
    try:
        await session.execute("SELECT 1")
        return {"status":"ok"}
    except Exception as e:
        return {"status":"error", "message":str(e)}