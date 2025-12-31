import os
from models.diffusion_pipeline import DiffusionPipelineWrapper
from utils.video_utils import save_video


class VideoGenerator:
    def __init__(self):
        self.pipeline = DiffusionPipelineWrapper()

    def generate_video(self, prompt: str, filename: str):
        frames = self.pipeline.generate(prompt)

        output_path = os.path.join("outputs", "generated_videos", filename)
        save_video(frames, output_path)

        return output_path
