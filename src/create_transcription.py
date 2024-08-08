from faster_whisper import WhisperModel

model_size = "medium.en"

# Run on GPU with FP16
# model = WhisperModel(model_size, device="cuda", compute_type="float16")
# or run on CPU with INT8
model = WhisperModel(model_size, device="cpu", compute_type="int8")

segments, info = model.transcribe("audio/output.mp3", beam_size=5)

print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

# for segment in segments:
#     print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
    
# Concatenate the text from all segments
full_text = ""
for segment in segments:
    full_text += segment.text + " "  # Append each segment's text

# Save the concatenated text to a file
output_text_file = "transcribed_text/transcription.txt"
with open(output_text_file, "w") as f:
    f.write(full_text.strip())  # Write the text to the file
print(full_text)
print(f"Transcription saved to {output_text_file}")