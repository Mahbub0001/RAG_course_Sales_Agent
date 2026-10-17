from app.core.config import Settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import get_settings

settings: Settings=get_settings()