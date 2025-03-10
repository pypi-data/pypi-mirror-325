import base64
from io import BytesIO

from loguru import logger
from PIL import Image


def get_base64_image(filepath, width=200):
    try:
        with Image.open(filepath) as img:
            # Convert to RGB if needed
            if img.mode != "RGB":
                img = img.convert("RGB")
            
            aspect_ratio = img.height / img.width
            height = int(width * aspect_ratio)
            img = img.resize((width, height), Image.Resampling.LANCZOS)
            buffered = BytesIO()
            img.save(buffered, format="JPEG")
            img_str = base64.b64encode(buffered.getvalue()).decode()
            return f'<img src="data:image/jpeg;base64,{img_str}" width="{width}" alt="Sample Image">'
    except Exception as e:
        logger.warning(f"Failed to encode image {filepath}: {e}")
        return None
