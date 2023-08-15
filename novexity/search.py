import os
import json
from urllib.parse import unquote
import requests
from bs4 import BeautifulSoup
from collections import OrderedDict
from .requests_ip_rotator.ip_rotator import ApiGateway


class Configuration:
    def __init__(self):
        self.AWS_ACCESS_KEY_ID = os.getenv('GOOGLE_SEARCH_AWS_ACCESS_KEY_ID')
        self.AWS_ACCESS_KEY_SECRET = os.getenv(
            'GOOGLE_SEARCH_AWS_SECRET_ACCESS_KEY')


config = Configuration()  # Initialize the configuration

VALID_KEYS = {'title', 'link', 'displayed_link',
              'favicon', 'snippet', 'source'}


def configure(aws_access_key_id=None, aws_secret_access_key=None):
    """
    Configures the AWS keys for the search function.

    Args:
    - aws_access_key_id (str): AWS access key ID.
    - aws_secret_access_key (str): AWS secret access key.
    """
    if aws_access_key_id:
        config.AWS_ACCESS_KEY_ID = aws_access_key_id
    if aws_secret_access_key:
        config.AWS_ACCESS_KEY_SECRET = aws_secret_access_key


def format_json_output(data):
    """
    Formats data into a JSON string with specified parameters.

    Args:
    - data (dict): The data to be formatted.

    Returns:
    - str: Formatted JSON string.
    """
    return json.dumps(data, indent=4, ensure_ascii=False)


def search(query: str, *fields, country=None):
    """
    Searches Google for a given query string and returns the organic search results.

    Args:
    - query (str): The search term or phrase to look up on Google.
    - *fields (str): Fields you want in the results. Options include: 'title', 
                     'link', 'displayed_link', 'favicon', 'snippet', 'source'.

    Returns:
    - dict: A dictionary containing the organic search results based on the requested fields.

    Raises:
    - Returns an error dictionary if the search fails.
    """
    # Check for the 'position' key and invalid keys:
    if 'position' in fields:
        return format_json_output({"error": "The 'position' key is not a valid choice."}), None
    invalid_keys = set(fields) - VALID_KEYS
    if invalid_keys:
        return format_json_output({"error": f"Invalid keys: {', '.join(invalid_keys)}"}), None

    headers = {
        "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64)'
        ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4454.0 Safari/537.36'
    }

    gateway = ApiGateway("https://www.google.com", access_key_id=config.AWS_ACCESS_KEY_ID,
                         access_key_secret=config.AWS_ACCESS_KEY_SECRET)
    gateway.start()

    session = requests.Session()
    session.mount("https://www.google.com", gateway)

    # Build the URL based on whether a country is specified or not
    if country:
        url = f"https://www.google.com/search?q={query}&gl={country}"
    else:
        url = f"https://www.google.com/search?q={query}"

    response = None

    try:  # Start of the try block
        while True:
            try:
                response = session.get(url, headers=headers)
                if response.status_code == 200:
                    print('Received a 200 OK response!')
                    break
                print('Status Code:', response.status_code, "Switching IP...")
            except requests.exceptions.Timeout:
                print('Request timed out. Switching IP...')
            except requests.ConnectionError:
                print('Connection error. Switching IP...')
            except Exception as error:
                print('An unexpected error occurred:',
                      error, ". Switching IP...")

        if response.status_code != 200:
            return format_json_output({"error": "Failed to retrieve web page."}), gateway

        soup = BeautifulSoup(response.text, 'html.parser')

        # Check if search results are loaded
        if not soup.select_one('div#search'):
            return {"error": "Search results not loaded."}, gateway

        search_results = []

        # Check which fields are requested
        fetch_all = not bool(fields)
        fetch_position = 'position' in fields or fetch_all
        fetch_title = 'title' in fields or fetch_all
        fetch_link = 'link' in fields or fetch_all
        fetch_displayed_link = 'displayed_link' in fields or fetch_all
        fetch_favicon = 'favicon' in fields or fetch_all
        fetch_snippet = 'snippet' in fields or fetch_all
        fetch_source = 'source' in fields or fetch_all

        # If any of these fields are fetched, always include position
        if any([fetch_title, fetch_link, fetch_displayed_link, fetch_favicon, fetch_snippet, fetch_source]) and 'position' not in fields:
            fetch_position = True

        position = 0
        for result in soup.select('.g'):
            # Here we build the result_dict based on the fields requested:
            result_dict = OrderedDict()

            if fetch_position:
                position += 1
                result_dict["position"] = position

            if fetch_title and result.select_one('h3'):
                result_dict["title"] = result.select_one('h3').get_text()
            if fetch_link and result.select_one('a'):
                anchor_tag = result.select_one('a')
                if anchor_tag.has_attr('href'):
                    result_dict["link"] = unquote(anchor_tag['href'].split("&")[
                                                  0].replace("/url?q=", ""))
            if fetch_displayed_link:
                displayed_link_parts = result.select_one('.TbwUpd')
                if displayed_link_parts:
                    result_dict["displayed_link"] = " ".join(
                        displayed_link_parts.stripped_strings)
            if fetch_favicon and result.select_one('.eqA2re.NjwKYd img'):
                result_dict["favicon"] = result.select_one(
                    '.eqA2re.NjwKYd img')['src']
            if fetch_snippet:
                snippet_parts = result.select(
                    '.MUxGbd.yXK7lf.MUxGbd.yDYNvb.lyLwlc')
                if snippet_parts:
                    result_dict["snippet"] = ' '.join(
                        part.get_text() for part in snippet_parts)
            if fetch_source:
                source_element = result.select_one('cite')
                if source_element:
                    result_dict["source"] = source_element.get_text()

            # At least one essential field (like title or link) must be present
            if result_dict.get("title") or result_dict.get("link"):
                # Ensure that the result is unique (based on title and link)
                if not any(existing_result.get("link") == result_dict.get("link") and
                           existing_result.get(
                               "title") == result_dict.get("title")
                           for existing_result in search_results):
                    search_results.append(result_dict)

        # Reset the position values to ensure they are sequential
        for idx, result in enumerate(search_results, 1):
            result["position"] = idx

        # Sort the search_results based on the position key
        search_results = sorted(
            search_results, key=lambda x: x.get('position', float('inf')))

        # Create a dictionary to store the final JSON result
        json_result = {
            "organic_results": search_results
        }

        return format_json_output(json_result), gateway

    except (ConnectionError, ValueError) as exc:
        error = {
            "error": str(exc)
        }
        return error, gateway
