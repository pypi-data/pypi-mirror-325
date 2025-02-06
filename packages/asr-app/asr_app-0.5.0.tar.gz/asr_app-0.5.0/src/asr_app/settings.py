from typing import Tuple

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    browse_files_initial_dir: str = Field(".")
    browse_dir_initial_dir: str = Field(".")

    audio_files_ext: Tuple[str, ...] = Field(
        default=('*.flac', '*.m4a', '*.mp3', '*.mp4', '*.mpeg', '*.mpga', '*.oga', '*.ogg',
                 '*.wav', '*.webm'),
    )

    whisper_models_names: list[str] = ['base', 'small', 'medium', 'large']
    whisper_default_model: str = 'large'

    temperature: float  = 0.6
    no_speech_threshold: float = 0.4 
    condition_on_previous_text: bool = False,


    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='ignore')


settings = Settings()
