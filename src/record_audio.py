import pyaudio
import wave
from pydub import AudioSegment
import os

def record_audio(output_filename="output.mp3", record_seconds=10):
    # Set up parameters
    format = pyaudio.paInt16  # Audio format
    channels = 1  # Mono audio
    rate = 44100  # Sampling rate
    chunk = 1024  # Buffer size
    wave_output_filename = "temp.wav"

    audio = pyaudio.PyAudio()

    # Start recording
    print("Recording...")
    stream = audio.open(format=format, channels=channels,
                        rate=rate, input=True,
                        frames_per_buffer=chunk)
    
    frames = []

    try:
        while True:
            data = stream.read(chunk)
            frames.append(data)
    except KeyboardInterrupt:
        pass

    print("Finished recording.")

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the recorded data as a WAV file
    wave_file = wave.open(wave_output_filename, 'wb')
    wave_file.setnchannels(channels)
    wave_file.setsampwidth(audio.get_sample_size(format))
    wave_file.setframerate(rate)
    wave_file.writeframes(b''.join(frames))
    wave_file.close()

    # Create the demo directory if it doesn't exist
    demo_folder = os.path.join(os.getcwd(), "audio")
    os.makedirs(demo_folder, exist_ok=True)

    # Path to save the MP3 file
    mp3_output_path = os.path.join(demo_folder, output_filename)

    # Convert WAV to MP3 using pydub
    audio_segment = AudioSegment.from_wav(wave_output_filename)
    audio_segment.export(mp3_output_path, format="mp3")

    # Remove the temporary WAV file
    os.remove(wave_output_filename)

    print(f"Audio saved as {mp3_output_path}")

if __name__ == "__main__":
    record_audio()
