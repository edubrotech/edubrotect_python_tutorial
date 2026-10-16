# 📌 Structural Pattern 02: Facade

## 📖 Intent
> *"Provide a unified interface to a set of interfaces in a subsystem. Facade defines a higher-level interface that makes the subsystem easier to use."* — Gang of Four

A Facade shields client code from the overwhelming complexity of multiple internal micro-libraries, subsystems, or external SDK steps by exposing a clean, high-level method.

```
                  ┌─────────────────────────────────────────┐
                  │                 CLIENT                  │
                  └────────────────────┬────────────────────┘
                                       │ calls clean API
                                       ▼
                  ┌─────────────────────────────────────────┐
                  │                 FACADE                  │
                  └──────┬─────────────┼─────────────┬──────┘
                         │             │             │
        ┌────────────────▼───┐  ┌──────▼──────┐  ┌───▼────────────────┐
        │ Subsystem A (Audio)│  │Subsystem B  │  │ Subsystem C (Codec)│
        └────────────────────┘  └─────────────┘  └────────────────────┘
```

---

## 🛠️ Implementation in Python: Video Transcoding Pipeline

```python
# Complex Subsystems:
class AudioExtractor:
    def extract_audio(self, video_file: str):
        print(f"🔊 Extracted audio track from {video_file}")
        return "raw_audio.pcm"

class VideoScaler:
    def rescale(self, video_file: str, resolution: str):
        print(f"📐 Scaled {video_file} to resolution {resolution}")
        return "scaled_video.raw"

class BitrateCompressor:
    def compress(self, video_stream, bitrate_kbps: int):
        print(f"🗜️ Compressed video to {bitrate_kbps} kbps")
        return "compressed.mp4"

class AudioVideoMuxer:
    def mux(self, video, audio, output_filename: str):
        print(f"🎬 Combined video and audio into final output: {output_filename}")
        return output_filename

# The Facade: Exposes a single, dead-simple method to clients
class VideoConverterFacade:
    def __init__(self):
        self.extractor = AudioExtractor()
        self.scaler = VideoScaler()
        self.compressor = BitrateCompressor()
        self.muxer = AudioVideoMuxer()

    def convert_for_mobile(self, input_video: str, output_name: str) -> str:
        """High-level one-step video processing method"""
        print(f"\n🚀 Starting Mobile Video Conversion for '{input_video}'...")
        audio = self.extractor.extract_audio(input_video)
        scaled = self.scaler.rescale(input_video, "720p")
        compressed = self.compressor.compress(scaled, bitrate_kbps=1500)
        final_file = self.muxer.mux(compressed, audio, output_name)
        print("✅ Conversion successfully completed!\n")
        return final_file

# Client Code: Doesn't need to know anything about scaling, bitrates, or muxing!
converter = VideoConverterFacade()
converter.convert_for_mobile("vacation_4k.mov", "vacation_mobile.mp4")
```

---

## 🧠 Top Interview Questions

1. **Q: What is the primary difference between Facade and Adapter?**
   * **A:**
     * **Adapter** wraps an existing object to make two incompatible interfaces work together.
     * **Facade** defines a brand-new, simplified interface over an entire complex subsystem consisting of many classes.
