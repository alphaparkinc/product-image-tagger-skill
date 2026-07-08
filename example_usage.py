"""
example_usage.py -- Demonstrates ProductImageTaggerClient
"""
from client import ProductImageTaggerClient

def main():
    client = ProductImageTaggerClient()
    result = client.generate_tags(
        product_name="Glow Moisturizer",
        product_category="Skincare",
        features=["Organic Formula", "Glass Bottle"]
    )
    print("[Image Tagging Result]")
    print(f"Alt Tag: {result['generated_alt_tag']}")
    print(f"Metadata Tags: {result['image_metadata_tags']}")

if __name__ == "__main__":
    main()
