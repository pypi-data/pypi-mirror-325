import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv('../env')

class Settings:
    """Gateway SDK settings loaded from environment variables"""
    
    @property
    def base_url(self) -> str:
        """Get the base URL from environment variable or use default"""
        base_url = os.getenv("KOSMOY_API_BASE_URL").rstrip("/")
        if not base_url:
            raise ValueError("KOSMOY_API_BASE_URL is not set")
        return base_url

# Global settings instance
settings = Settings()
