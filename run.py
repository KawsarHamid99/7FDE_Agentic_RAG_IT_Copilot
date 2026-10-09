from app.core.config import get_settings
settings=get_settings()
print(f"App NAme: {settings.app_name}\n")
print(f"OpenAI_key: {settings.openai_api_key}")