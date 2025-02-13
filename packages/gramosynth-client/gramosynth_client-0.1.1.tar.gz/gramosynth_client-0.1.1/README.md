# Gramosynth API Client

A Python client library for interacting with the Gramosynth API. This library provides an easy-to-use interface for searching music tracks, finding similar tracks, and creating variations by mixing different stems.

## Installation

```bash
pip install gramosynth_client
```

## Quick Start

```python
from gramosynth_client import GramosynthClient

# Initialize the client
client = GramosynthClient()

# Perform a text search
results = client.initial_search("jazz piano")

# Create variations and save audio files
variations = client.create_auto_variations(
    track_id="track_id_here",
    stem_type="piano",
    output_dir="my_variations"
)
```

## API Reference

### GramosynthClient

The main class for interacting with the Gramosynth API.

```python
client = GramosynthClient()
```

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
        "similarity_score": 0.85
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

Create variations by swapping stems with specific target tracks and save the audio files locally.

```python
variations = client.create_stem_variations(
    source_track_id="source_id",
    target_tracks=["target_id_1", "target_id_2"],
    stem_type="piano",
    output_dir="variations"
)
```

##### Parameters

- `source_track_id` (str): ID of the source track
- `target_tracks` (list): List of target track IDs
- `stem_type` (str): Type of stem to swap (e.g., "piano", "drums", "vocals")
- `output_dir` (str, optional): Directory to save the audio files. Defaults to "variations"

##### Returns

Dictionary containing the created variations:
```python
{
    "variations": [
        {
            "mixed_audio": "base64_encoded_audio_data",
            "local_audio_path": "variations/mixed_1.wav",
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
    similarity_threshold=0.7,
    output_dir="variations"
)
```

##### Parameters

- `track_id` (str): ID of the track
- `stem_type` (str): Type of stem to swap
- `n_variations` (int, optional): Number of variations to create. Defaults to 5.
- `similarity_threshold` (float, optional): Minimum similarity score (0-1) for finding similar tracks. Defaults to 0.7.
- `output_dir` (str, optional): Directory to save the audio files. Defaults to "variations"

##### Returns

Dictionary containing the original track and created variations:
```python
{
    "original_track": {
        # Original track information
    },
    "variations": [
        {
            "mixed_audio": "base64_encoded_audio_data",
            "local_audio_path": "variations/auto_1.wav",
            # ... other variation info
        }
    ],
    "total_variations": 5
}
```

## Utility Methods

### encode_audio_file

Encode an audio file to base64 format.

```python
encoded = client.encode_audio_file("path/to/audio.wav")
```

### decode_audio_data

Decode base64 audio data and save to a file.

```python
output_path = client.decode_audio_data(base64_audio_data, "output.wav")
```

## Error Handling

The client raises `requests.exceptions.RequestException` for API-related errors:

```python
from requests.exceptions import RequestException

try:
    results = client.initial_search("jazz piano")
except RequestException as e:
    print(f"API Error: {str(e)}")
except Exception as e:
    print(f"Error: {str(e)}")
```

## Examples

### Basic Search and Variation Creation

```python
# Initialize client
client = GramosynthClient()

# Search for tracks
results = client.initial_search("jazz piano", limit=5)

if results:
    # Get the first track
    track_id = results[0]['id']
    
    # Create variations and save audio files
    variations = client.create_auto_variations(
        track_id=track_id,
        stem_type="piano",
        n_variations=3,
        output_dir="my_variations"
    )
    
    # The variations will be saved in the "my_variations" directory
    print("Created variations:", variations)
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
    stem_type="piano",
    output_dir="custom_variations"
)

# Access the local audio files
for variation in variations["variations"]:
    print(f"Variation saved to: {variation['local_audio_path']}")
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.