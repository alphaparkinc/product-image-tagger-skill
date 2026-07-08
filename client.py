"""
product-image-tagger-skill: Client SDK
Auto-compiles SEO tags and Alt-text strings from visible product dimensions.
"""
from __future__ import annotations
from typing import Optional


class ProductImageTaggerClient:
    """
    SDK for image asset cataloging.
    """

    def generate_tags(
        self,
        product_name: str,
        product_category: str,
        features: list[str],
    ) -> dict:
        alt_tag = f"Photo of {product_name} -- premium {product_category} featuring {', '.join(features[:2])}."
        
        meta_tags = [product_name.lower(), product_category.lower()] + [f.lower() for f in features]

        return {
            "generated_alt_tag": alt_tag,
            "image_metadata_tags": meta_tags
        }
