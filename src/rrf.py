# src/rrf.py
class RRFRefiner:
    def __init__(self, max_iters: int = 3, base_model=None):
        self.max_iters = max_iters
        self.base_model = base_model  # shared MonkeyOCR instance

    def __call__(self, draft_parse: dict, document_image: str) -> dict:
        current = draft_parse.copy()
        for _ in range(self.max_iters):
            errors = self._detect_inconsistencies(current)
            if not errors:
                break
            corrections = self._visual_verification(document_image, errors)
            current = self._apply_corrections(current, corrections)
        return current

    def _detect_inconsistencies(self, parse: dict):
        # Placeholder: implement hierarchy mismatch, table sum errors, etc.
        return []  # list of error dicts {region, type, confidence}

    def _visual_verification(self, image_path: str, errors: list):
        # Placeholder: use base_model to re-query regions with prompts
        return {}  # correction dicts

    def _apply_corrections(self, parse: dict, corrections: dict):
        # Merge corrections into parse
        return parse
