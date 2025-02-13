from .client_ import GramosynthClient
from .exceptions import (
    MusicAPIError,
    AuthenticationError,
    ResourceNotFoundError,
    ValidationError,
    RateLimitError,
    ProcessingError
)

__version__ = "0.1.0"

__all__ = [
    'GramosynthClient',
    'StemReplacementRequest',
    'StemReplacementOutput',
    'RatingInput',
    'RatingOutput',
    'TextQueryInput',
    'SearchResult',
    'MusicAPIError',
    'AuthenticationError',
    'ResourceNotFoundError',
    'ValidationError',
    'RateLimitError',
    'ProcessingError'
]