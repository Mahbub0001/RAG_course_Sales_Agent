from fastapi import FastAPI,Depends
from app.core.config import Settings, get_settings

app = FastAPI(title="Sales Agent")

@app.get("/health")
async def health(settings:Settings=Depends(get_settings))->dict[str,str]:
    return{
        "status":"ok",
        "app name":settings.APP_NAME

    }