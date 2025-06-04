"""Masked PDF Translator GUI with automatic mask management."""

import json
import os


class PDFTranslatorApp:
    """Simplified translator class.

    This example includes only the mask loading/saving logic to
    demonstrate automation improvements.
    """

    def __init__(self):
        self.manual_elements = {}
        self.input_pdf_var = ""

    # ------------------------------------------------------------------
    # Mask handling helpers
    # ------------------------------------------------------------------
    def save_masks_to_path(self, filepath):
        """Save masks to the given JSON file."""
        data = {}
        for page, elements in self.manual_elements.items():
            serialised = []
            for item in elements:
                box = item.get("bbox")
                serialised.append({"type": item.get("type"), "bbox": box})
            if serialised:
                data[str(page)] = serialised

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    def load_masks_from_path(self, filepath):
        """Load masks from the given JSON file."""
        if not os.path.exists(filepath):
            return False

        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.manual_elements = {}
        for key, elements in data.items():
            page = int(key)
            self.manual_elements[page] = []
            for item in elements:
                self.manual_elements[page].append({
                    "type": item.get("type"),
                    "bbox": item.get("bbox"),
                })
        return True

    # ------------------------------------------------------------------
    # Example hooks for GUI operations (greatly simplified)
    # ------------------------------------------------------------------
    def load_pdf(self, filepath):
        """Load a PDF and automatically import masks if present."""
        self.input_pdf_var = filepath

        mask_path = os.path.splitext(filepath)[0] + "_masks.json"
        if self.load_masks_from_path(mask_path):
            print(f"Info: loaded masks from {mask_path}")

    def finish_translation(self):
        """Called when translation is finished."""
        if not self.input_pdf_var:
            return
        mask_path = os.path.splitext(self.input_pdf_var)[0] + "_masks.json"
        try:
            self.save_masks_to_path(mask_path)
            print(f"Info: masks saved to {mask_path}")
        except Exception as exc:  # pragma: no cover - example
            print(f"Failed to save masks: {exc}")


if __name__ == "__main__":
    app = PDFTranslatorApp()
    app.load_pdf("example.pdf")
    # ... user interaction here ...
    app.finish_translation()
