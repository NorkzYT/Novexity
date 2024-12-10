import os
import json
from dotenv import load_dotenv
from novexity import NovexitySearch, configure

# Load environment variables
load_dotenv()

# Configure AWS keys
AWS_ACCESS_KEY_ID = os.getenv("GOOGLE_SEARCH_AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("GOOGLE_SEARCH_AWS_SECRET_ACCESS_KEY")
configure(
    aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

# Initialize API Gateway
NovexitySearch.init_gateway()

# Search parameters
params = {"q": "Minecraft", "country": "fr", "lang": "fr"}

# Perform search
novexity_search = NovexitySearch(params)
search_results = novexity_search.get_dict()

# Save the results to search.json
with open("google-search.json", "w", encoding="utf-8") as file:
    file.write(json.dumps(search_results, indent=4))

# Required and optional fields
required_fields = ["title", "link", "snippet"]
optional_fields = ["displayed_link", "favicon", "source"]

# Check and print field presence
for result in search_results.get("organic_results", []):
    position = result.get("position", "Unknown position")

    # Check for missing fields
    missing_required_fields = [
        field for field in required_fields if field not in result
    ]
    missing_optional_fields = [
        field for field in optional_fields if field not in result
    ]

    # Print missing required fields
    if missing_required_fields:
        print(
            f"Position {position}: Missing required fields: {missing_required_fields}"
        )
        NovexitySearch.shutdown_gateway()
        exit(1)

    # Print missing optional fields
    if missing_optional_fields:
        print(
            f"Position {position}: Warning: Missing optional fields: {missing_optional_fields}"
        )

print("All required fields are present.")

# Shut down the API Gateway
NovexitySearch.shutdown_gateway()
