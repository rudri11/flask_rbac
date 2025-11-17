import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Secret key for sessions
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
    # Database configuratio
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Session configuration
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = False  
    PERMANENT_SESSION_LIFETIME = 3600  