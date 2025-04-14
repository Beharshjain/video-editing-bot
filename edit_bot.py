import os
import subprocess

# Folders
input_folder = "input_videos"
output_folder = "output_videos"

# Make sure output folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through all video files
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".mp4", ".mov", ".avi", ".mkv")):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, f"edited_{filename}")

        # Corrected FFmpeg command
        command = [
            "ffmpeg",
            "-i", input_path,
            "-filter_complex",
            "[0:v]setpts=0.8333*PTS,eq=brightness=0.06:saturation=2.0:contrast=1.1[v];"
            "[0:a]atempo=1.2[a]",
            "-map", "[v]",
            "-map", "[a]",
            output_path
        ]

        subprocess.run(command)

print("All videos edited with audio successfully!")