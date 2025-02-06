from typing import Optional
from pydantic import BaseModel, Field

class EmotionWeights(BaseModel):
    happiness: float = Field(ge=0, le=1)
    sadness: float = Field(ge=0, le=1)
    disgust: float = Field(ge=0, le=1)
    fear: float = Field(ge=0, le=1)
    surprise: float = Field(ge=0, le=1)
    anger: float = Field(ge=0, le=1)
    other: float = Field(ge=0, le=1)
    neutral: float = Field(ge=0, le=1)

class ConditioningSources(BaseModel):
    speaker: bool = True
    emotion: bool = True
    pitch_std: bool = False
    speaking_rate: bool = True
    fmax: bool = True
    vqscore: bool = False

class TTSParams(BaseModel):
    text: str
    speaker_audio: Optional[str] = None
    seconds: Optional[float] = Field(None, ge=1, le=30)
    temperature: Optional[float] = Field(None, ge=0.1, le=2.0)
    top_p: Optional[float] = Field(None, ge=0, le=1)
    top_k: Optional[int] = Field(None, ge=0, le=1024)
    min_p: Optional[float] = Field(None, ge=0, le=0.3)
    text_cfg: Optional[bool] = True
    audio_cfg: Optional[bool] = False
    keep_prefix: Optional[bool] = False
    seed: Optional[int] = Field(None, ge=-1, le=2147483647)
    cfg_scale: Optional[float] = Field(None, ge=1, le=10)
    fmax: Optional[int] = Field(None, ge=0, le=24000)
    vqscore: Optional[float] = Field(None, ge=0.5, le=1)
    pitch_std: Optional[float] = Field(None, ge=0, le=500)
    speaking_rate: Optional[float] = Field(None, ge=5, le=35)
    conditioning_sources: Optional[ConditioningSources] = None
    emotion: Optional[EmotionWeights] = None
    language_iso_code: Optional[str] = None
    mime_type: Optional[str] = None
