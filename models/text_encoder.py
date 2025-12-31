from transformers import CLIPTokenizer, CLIPTextModel
import torch


class TextEncoder:
    def __init__(self, model_name="openai/clip-vit-base-patch32", device="cpu"):
        self.tokenizer = CLIPTokenizer.from_pretrained(model_name)
        self.text_encoder = CLIPTextModel.from_pretrained(model_name).to(device)
        self.device = device

    def encode(self, prompt):
        inputs = self.tokenizer(
            prompt,
            return_tensors="pt",
            padding=True,
            truncation=True
        ).to(self.device)

        with torch.no_grad():
            embeddings = self.text_encoder(**inputs).last_hidden_state

        return embeddings
