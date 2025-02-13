import requests
import json
import base64
import soundfile as sf
import io
import os

BASE_URL = "184.105.208.246:8000"

class GramosynthClient:
    def __init__(self):
        """
        Initialize the client with the API base URL.
        """
        self.base_url = BASE_URL.rstrip('/')

    def _make_request(self, method, endpoint, data=None):
        """
        Make an HTTP request to the API.
        
        Args:
            method (str): HTTP method (GET, POST, etc.)
            endpoint (str): API endpoint
            data (dict): Request data
            
        Returns:
            dict: Response data
        """
        url = f"{self.base_url}/{endpoint}"
        headers = {'Content-Type': 'application/json'}
        
        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            data=json.dumps(data) if data else None
        )
        
        response.raise_for_status()
        return response.json()

    def encode_audio_file(self, file_path):
        """
        Encode an audio file to base64.
        
        Args:
            file_path (str): Path to the audio file
            
        Returns:
            str: Base64 encoded audio string
        """
        audio_data, _ = sf.read(file_path)
        buffer = io.BytesIO()
        sf.write(buffer, audio_data, samplerate=32000, format='WAV')
        buffer.seek(0)
        return base64.b64encode(buffer.read()).decode()

    def decode_audio_data(self, base64_audio, output_path):
        """
        Decode base64 audio data and save to file.
        
        Args:
            base64_audio (str): Base64 encoded audio string
            output_path (str): Path to save the decoded audio file
            
        Returns:
            str: Path to the saved audio file
        """
        if not base64_audio:
            return None
            
        try:
            # Remove data URL prefix if present
            if ',' in base64_audio:
                base64_audio = base64_audio.split(',')[1]
                
            # Decode base64 to bytes
            audio_bytes = base64.b64decode(base64_audio)
            
            # Save to file
            with open(output_path, 'wb') as f:
                f.write(audio_bytes)
                
            return output_path
            
        except Exception as e:
            print(f"Error decoding audio data: {str(e)}")
            return None

    def initial_search(self, query, audio_file=None, limit=10):
        """
        Perform initial search using text query and optional audio.
        
        Args:
            query (str): Text search query
            audio_file (str, optional): Path to audio file
            limit (int): Maximum number of results
            
        Returns:
            dict: Search results
        """
        data = {
            "query": query,
            "limit": limit
        }
        
        if audio_file:
            data["audio_file"] = self.encode_audio_file(audio_file)
            
        return self._make_request("POST", "search/initial", data)

    def find_similar_tracks(self, track_id, n_variations=5):
        """
        Find similar tracks based on a selected track.
        
        Args:
            track_id (str): ID of the reference track
            n_variations (int): Number of variations to return
            
        Returns:
            dict: Similar tracks
        """
        data = {
            "track_id": track_id,
            "n_variations": n_variations
        }
        
        return self._make_request("POST", "search/similar", data)

    def create_stem_variations(self, source_track_id, target_tracks, stem_type, output_dir="variations"):
        """
        Create variations by swapping stems with target tracks.
        
        Args:
            source_track_id (str): ID of the source track
            target_tracks (list): List of target track IDs
            stem_type (str): Type of stem to swap
            output_dir (str): Directory to save audio files
            
        Returns:
            dict: Created variations with local audio file paths
        """
        data = {
            "source_track_id": source_track_id,
            "target_tracks": target_tracks,
            "stem_type": stem_type
        }
        
        response = self._make_request("POST", "mix/variations", data)
        
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Save audio files from variations
        for i, variation in enumerate(response["variations"]):
            if "mixed_audio" in variation:
                output_path = os.path.join(
                    output_dir, 
                    f"{source_track_id}_{target_tracks[i]}_{stem_type}.wav"
                )
                variation["local_audio_path"] = self.decode_audio_data(
                    variation["mixed_audio"],
                    output_path
                )
                
        return response

    def create_auto_variations(self, track_id, stem_type, n_variations=5, 
                             similarity_threshold=0.7, output_dir="variations"):
        """
        Automatically create variations for a track.
        
        Args:
            track_id (str): ID of the track
            stem_type (str): Type of stem to swap
            n_variations (int): Number of variations to create
            similarity_threshold (float): Minimum similarity score
            output_dir (str): Directory to save audio files
            
        Returns:
            dict: Created variations with local audio file paths
        """
        data = {
            "track_id": track_id,
            "stem_type": stem_type,
            "n_variations": n_variations,
            "similarity_threshold": similarity_threshold
        }
        
        response = self._make_request("POST", "mix/auto-variations", data)
        
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Save audio files from variations
        for i, variation in enumerate(response["variations"]):
            if "mixed_audio" in variation:
                output_path = os.path.join(
                    output_dir, 
                    f"{track_id}_auto_{i}_{stem_type}.wav"
                )
                variation["local_audio_path"] = self.decode_audio_data(
                    variation["mixed_audio"],
                    output_path
                )
                
        return response