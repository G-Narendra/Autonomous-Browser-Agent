import sys
import os


PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)

from models.video_generator import VideoGenerator


def main():
    generator = VideoGenerator()

    prompt = "A cinematic sunset over mountains with flying birds"

    output_path = generator.generate_video(
        prompt=prompt,
        filename="demo_video.mp4"
    )

    print("Video saved at:", output_path)


if __name__ == "__main__":
    main()
