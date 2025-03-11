from pathlib import Path

# Crossref API
tool_name = "Asura Interview Prep"
tool_version = "0.1"
tool_url = ""
tool_email = "asura.enkhbayar@gmail.com"

# Ratelimits for API
CALLS = 50
PERIOD = 1

# directories
bronze_dir = Path("../data/bronze")
silver_dir = Path("../data/silver")
gold_dir = Path("../data/gold")

# files
bronze_sample = bronze_dir / "sample.jsonl"  # 10,000 records

silver_sample = silver_dir / "sample.jsonl"
