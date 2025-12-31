import torch
from diffusers import TextToVideoSDPipeline
from utils.config import MODEL_NAME


class DiffusionPipelineWrapper:
    def __init__(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"

        dtype = torch.float16 if device == "cuda" else torch.float32

        self.pipe = TextToVideoSDPipeline.from_pretrained(
            MODEL_NAME,
            torch_dtype=dtype
        )

        self.pipe = self.pipe.to(device)

    def generate(self, prompt: str, num_frames=16):
        output = self.pipe(
            prompt=prompt,
            num_frames=num_frames
        )

        return output.frames
