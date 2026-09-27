from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """Loaded from the .env  file  
      Provide a single access point so every module import setting instead of reading os.environ directyl
    """

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    # dataBase_url 
    database_url : str

    # auth
    jwt_secret: str
    jwt_algorithm: str =  "HS256"
    access_token_expire_minutes : int = 60 * 24 * 7

    # storage 
    storage_backend: str = "local"
    storage_local_root : str 
    storage_public_base_url : str 

    # cors 
    frontend_origin: str

    # image url fetching (SSRF - safe fetch)
    image_fetch_timeout_seconds : float = 8.0
    image_fetch_max_bytes: int = 10 * 1024  * 1024 # 10MB
    image_fetch_allowed_content_types : tuple[str, ...] = (
        "image/png",
        "image/jpeg",
        "image/webp",
        "image/gif"
    )

@lru_cache  # caches the setting object so it isn't recreated everytime
def get_settings() -> Settings:
    return Settings()