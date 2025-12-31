import torch

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
MODEL_NAME = "damo-vilab/text-to-video-ms-1.7b"

NUM_FRAMES = 16
FPS = 8
HEIGHT = 256
WIDTH = 256

OUTPUT_DIR = "outputs/generated_videos"
