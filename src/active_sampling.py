# src/active_sampling.py
class ActiveSamplingRouter:
    def __init__(self, lora_rank: int = 16, device: str = "cuda"):
        self.lora_rank = lora_rank
        self.device = device
        self.known_prototypes = {}  # dict of domain → geometric vector

    def __call__(self, parse: dict, document_image: str) -> dict:
        geom_features = self._extract_geometric_features(document_image)
        domain = self._route(geom_features)
        if domain in self.known_prototypes:
            # Apply pre-trained LoRA
            pass
        else:
            # Zero-shot nearest prototype
            pass
        return parse  # adapted parse

    def _extract_geometric_features(self, image_path: str):
        # Compute spatial entropy, line density, Voronoi, etc.
        return torch.rand(128)  # placeholder

    def _route(self, features):
        # KNN or cosine similarity to prototypes
        return "unknown"
