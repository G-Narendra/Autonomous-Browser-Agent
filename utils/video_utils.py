import imageio
import numpy as np
import os

def save_video(frames, path, fps=8):
    os.makedirs(os.path.dirname(path), exist_ok=True)

    processed_frames = []
    for frame in frames:
        if hasattr(frame, "cpu"):
            frame = frame.cpu().numpy()
        processed_frames.append((frame * 255).astype("uint8"))

    imageio.mimsave(path, processed_frames, fps=fps)
