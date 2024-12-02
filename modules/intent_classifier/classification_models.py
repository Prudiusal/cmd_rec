from pydantic import BaseModel,Field, field_validator, model_validator
from enum import Enum
from typing import Union, Optional


class RequestCategory(str, Enum):
    VOICE_COMMAND = "voice_command"
    MUSIC_SUGGESTION = "music_suggestion"

class MusicGenre(str, Enum):
    TECHNO = 'techno'
    REGGAE = 'reggae'

class Command(str, Enum):
    BGCOLOR1 = "set_bg_color1"
    SPAWNASYNC = "spawn"
    SHOWBLOCKLIST = 'show_block_list'


class RGBColor(BaseModel):
    r: float = Field(..., description="Red component of the color (0.0 to 1.0)")
    g: float = Field(..., description="Green component of the color (0.0 to 1.0)")
    b: float = Field(..., description="Blue component of the color (0.0 to 1.0)")

    # description: str = "Color should be provided as an RGB tuple with each value between 0.0 and 1.0, e.g., [0.5, 0.2, 0.8]"

    # Custom Validator to enforce the RGB range
    @field_validator('r', 'g', 'b')
    def validate_color_range(cls, value):
        if not (0.0 <= value <= 1.0):
            raise ValueError('Color values must be between 0.0 and 1.0')
        return value


class SpawnArgument(str, Enum):
    OSC = 'oscillator'
    SPEAKER = 'speaker'
    NOIZE = 'noize'
    VIOLIN = 'violin'


class VoiceCommandArguments(BaseModel):
    command: Command
    arguments: Optional[Union[RGBColor, SpawnArgument]] = None

    @model_validator(mode='after')
    def validate_command_arguments(self):
        if self.command == Command.BGCOLOR1 and not isinstance(self.arguments, RGBColor):
            raise ValueError(f"{self.command} requires a ColorArgument.")
        if self.command == Command.SPAWNASYNC and not isinstance(self.arguments, SpawnArgument):
            raise ValueError(f"{self.command} requires a SpawnArgument.")
        if self.command == Command.SHOWBLOCKLIST and self.arguments is not None:
            raise ValueError(f"{self.command} does not accept arguments.")
        return self


class MusicSuggestionArguments(BaseModel):
    genre: MusicGenre
    mood: Optional[str] = Field(None, description="Optional mood descriptor for the suggestion.")


class ExtractIntention(BaseModel):
    intention: RequestCategory
    details: Union[VoiceCommandArguments, MusicSuggestionArguments]

    @model_validator(mode='after')
    def validate_intention(self):
        if self.intention == RequestCategory.VOICE_COMMAND and not isinstance(self.details, VoiceCommandArguments):
            raise ValueError(f"{self.intention} requires VoiceCommandArguments.")
        if self.intention == RequestCategory.MUSIC_SUGGESTION and not isinstance(self.details, MusicSuggestionArguments):
            raise ValueError(f"{self.intention} requires MusicSuggestionArguments.")
        return self
