import os
import json
from dotenv import load_dotenv
from novexity import NovexitySearch, configure

load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv("GOOGLE_SEARCH_AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("GOOGLE_SEARCH_AWS_SECRET_ACCESS_KEY")
configure(
    aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

params = {"q": "Minecraft", "country": "fr", "lang": "fr"}

# Initialize NovexitySearch with the parameters
novexity_search = NovexitySearch(params)

# Get the search results
novexity, returned_gateway = novexity_search.get_dict()

# Save the results to search.json
with open("google-search.json", "w", encoding="utf-8") as file:
    file.write(novexity)

# Shut down the gateways
returned_gateway.shutdown()

# Check if the required and optional fields are present in the output
required_fields = ["title", "link", "snippet"]
optional_fields = ["displayed_link", "favicon", "source"]

output_json = json.loads(novexity)
for result in output_json.get("organic_results", []):
    position = result.get("position", "Unknown position")

    missing_required_fields = [
        field for field in required_fields if field not in result
    ]
    missing_optional_fields = [
        field for field in optional_fields if field not in result
    ]

    if missing_required_fields:
        print(
            f"Position {position}: Missing required fields: {missing_required_fields}"
        )
        exit(1)

    if missing_optional_fields:
        print(
            f"Position {position}: Warning: Missing optional fields: {missing_optional_fields}"
        )

print("All required fields are present.")
