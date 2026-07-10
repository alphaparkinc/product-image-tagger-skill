# genpark-product-image-tagger-skill

> **GenPark AI Agent Skill** -- Product image metadata SEO tagging simulator.

## Quick Start

```python
from client import ProductImageTaggerClient
client = ProductImageTaggerClient()
res = client.generate_tags("Serum", "Skincare", ["Liquid"])
print(res["generated_alt_tag"])
```
