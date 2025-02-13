# Music Stem Mixing API Client

A Python client library for interacting with the Music Stem Mixing API. This library provides an easy-to-use interface for searching music tracks, finding similar tracks, and creating variations by mixing different stems.

## Installation

```bash
pip install music-stem-mixing-client
```

## Quick Start

```python
from music_stem_mixing import MusicStemMixingClient

# Initialize the client
client = MusicStemMixingClient("http://your-api-url:8000")

# Perform a text search
results = client.initial_search("jazz piano")

# Create variations
variations = client.create_auto_variations(
    track_id="track_id_here",
    stem_type="piano"
)
```

## API Reference

### MusicStemMixingClient

The main class for interacting with the Music Stem Mixing API.

```python
client = MusicStemMixingClient(base_url="http://localhost:8000")
```

#### Parameters

- `base_url` (str): The base URL of the API server. Defaults to "http://localhost:8000".

### Methods

#### initial_search

Search for tracks using text query and optionally an audio file.

```python
results = client.initial_search(
    query="jazz piano",
    audio_file="path/to/audio.wav",  # optional
    limit=10
)
```

##### Parameters

- `query` (str): Text search query
- `audio_file` (str, optional): Path to an audio file for similarity search
- `limit` (int, optional): Maximum number of results to return. Defaults to 10.

##### Returns

List of dictionaries containing track information:
```python
[
    {
        "id": "track_id",
        "title": "Track Title",
        "artist": "Artist Name",
        "genre": "Genre",
        "key": "C",
        "tempo": 120,
        "similarity_score": 0.85,
        "audio_file": "path/to/audio.wav",
        "stems": [
            {
                "type": "piano",
                "file": "path/to/stem.wav"
            }
        ]
    }
]
```

#### find_similar_tracks

Find similar tracks based on a selected track.

```python
similar = client.find_similar_tracks(
    track_id="track_id_here",
    n_variations=5
)
```

##### Parameters

- `track_id` (str): ID of the reference track
- `n_variations` (int, optional): Number of similar tracks to return. Defaults to 5.

##### Returns

Dictionary containing original track and similar tracks:
```python
{
    "original_track": {
        "id": "track_id",
        "title": "Track Title",
        # ... other track info
    },
    "similar_tracks": [
        # List of similar track dictionaries
    ]
}
```

#### create_stem_variations

Create variations by swapping stems with specific target tracks.

```python
variations = client.create_stem_variations(
    source_track_id="source_id",
    target_tracks=["target_id_1", "target_id_2"],
    stem_type="piano"
)
```

##### Parameters

- `source_track_id` (str): ID of the source track
- `target_tracks` (list): List of target track IDs
- `stem_type` (str): Type of stem to swap (e.g., "piano", "drums", "vocals")

##### Returns

Dictionary containing the created variations:
```python
{
    "variations": [
        {
            "mixed_audio_path": "path/to/mixed.wav",
            "source_track": { /* source track info */ },
            "target_track": { /* target track info */ },
            "swapped_stem": "piano"
        }
    ]
}
```

#### create_auto_variations

Automatically create variations for a track by finding similar tracks and swapping stems.

```python
variations = client.create_auto_variations(
    track_id="track_id_here",
    stem_type="piano",
    n_variations=5,
    similarity_threshold=0.7
)
```

##### Parameters

- `track_id` (str): ID of the track
- `stem_type` (str): Type of stem to swap
- `n_variations` (int, optional): Number of variations to create. Defaults to 5.
- `similarity_threshold` (float, optional): Minimum similarity score (0-1) for finding similar tracks. Defaults to 0.7.

##### Returns

Dictionary containing the original track and created variations:
```python
{
    "original_track": {
        # Original track information
    },
    "variations": [
        # List of variation dictionaries
    ],
    "total_variations": 5
}
```

## Error Handling

The client raises `requests.exceptions.RequestException` for API-related errors. It's recommended to handle these exceptions in your code:

```python
from requests.exceptions import RequestException

try:
    results = client.initial_search("jazz piano")
except RequestException as e:
    print(f"API Error: {str(e)}")
except Exception as e:
    print(f"Error: {str(e)}")
```

## Utility Methods

### encode_audio_file

Utility method to encode an audio file to base64 format.

```python
encoded = client.encode_audio_file("path/to/audio.wav")
```

##### Parameters

- `file_path` (str): Path to the audio file

##### Returns

- Base64 encoded string of the audio file

## Examples

### Basic Search and Variation Creation

```python
# Initialize client
client = MusicStemMixingClient("http://localhost:8000")

# Search for tracks
results = client.initial_search("jazz piano", limit=5)

if results:
    # Get the first track
    track_id = results[0]['id']
    
    # Find similar tracks
    similar = client.find_similar_tracks(track_id)
    
    # Create variations
    variations = client.create_auto_variations(
        track_id=track_id,
        stem_type="piano",
        n_variations=3
    )
```

### Search with Audio File

```python
# Search using both text and audio
results = client.initial_search(
    query="jazz piano",
    audio_file="path/to/reference.wav",
    limit=5
)
```

### Creating Specific Variations

```python
# Create variations with specific target tracks
variations = client.create_stem_variations(
    source_track_id="source_id",
    target_tracks=["target_1", "target_2", "target_3"],
    stem_type="piano"
)
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.