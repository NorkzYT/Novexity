import os
import json
from urllib.parse import unquote
import requests
from bs4 import BeautifulSoup
from requests_ip_rotator import ApiGateway

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

aws_access_key_id = os.getenv('GOOGLE_SEARCH_AWS_ACCESS_KEY_ID')
aws_access_key_secret = os.getenv('GOOGLE_SEARCH_AWS_SECRET_ACCESS_KEY')

# Check if the necessary environment variables are set
if not aws_access_key_id or not aws_access_key_secret:
    raise ValueError(
        "Ensure both GOOGLE_SEARCH_AWS_ACCESS_KEY_ID and GOOGLE_SEARCH_AWS_SECRET_ACCESS_KEY"
        " are set in the .env file or system environment variables.")

TIMEOUT = 1  # Set this to an appropriate value


def format_json_output(data):
    """
    Formats data into a JSON string with specified parameters.

    Args:
    - data (dict): The data to be formatted.

    Returns:
    - str: Formatted JSON string.
    """
    return json.dumps(data, indent=4, ensure_ascii=False)


def search(query: str, *fields):
    """
    Searches Google for a given query string and returns the organic search results.

    Args:
    - query (str): The search term or phrase to look up on Google.
    - *fields (str): Fields you want in the results. Options include: 'position', 'title', 
                     'link', 'displayed_link', 'favicon', 'description', 'snippet', 'source'.

    Returns:
    - dict: A dictionary containing the organic search results based on the requested fields.

    Raises:
    - Returns an error dictionary if the search fails.
    """
    headers = {
        "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64)'
        ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4454.0 Safari/537.36'
    }

    gateway = ApiGateway("https://www.google.com", access_key_id=aws_access_key_id,
                         access_key_secret=aws_access_key_secret)
    gateway.start()

    session = requests.Session()
    session.mount("https://www.google.com", gateway)

    url = f"https://www.google.com/search?q={query}"
    response = None

    try:  # Start of the try block
        while True:
            try:
                response = session.get(url, headers=headers, timeout=TIMEOUT)
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
        fetch_description = 'description' in fields or fetch_all
        fetch_snippet = 'snippet' in fields or fetch_all
        fetch_source = 'source' in fields or fetch_all

        for index, result in enumerate(soup.select('div.tF2Cxc')):
            # Here we build the result_dict based on the fields requested:
            result_dict = {}

            if fetch_position:
                result_dict["position"] = index + 1
            if fetch_title and result.select_one('h3'):
                result_dict["title"] = result.select_one('h3').get_text()
            if fetch_link and result.select_one('a'):
                result_dict["link"] = unquote(result.select_one(
                    'a')['href'].split("&")[0].replace("/url?q=", ""))
            if fetch_displayed_link:
                displayed_link_parts = result.select_one('.TbwUpd')
                if displayed_link_parts:
                    result_dict["displayed_link"] = " ".join(
                        displayed_link_parts.stripped_strings)
            if fetch_favicon and result.select_one('.eqA2re.NjwKYd img'):
                result_dict["favicon"] = result.select_one(
                    '.eqA2re.NjwKYd img')['src']
            if fetch_description:
                description_parts = result.select(
                    '.MUxGbd.yXK7lf.MUxGbd.yDYNvb.lyLwlc')
                if description_parts:
                    result_dict["description"] = ' '.join(
                        part.get_text() for part in description_parts)
            if fetch_snippet:
                snippet_el = result.select_one(
                    '.VwiC3b.yXK7lf.MUxGbd.yDYNvb.lyLwlc span:last-child')
                if snippet_el:
                    result_dict["snippet"] = snippet_el.get_text()
            if fetch_source:
                source_element = result.select_one('cite')
                if source_element:
                    result_dict["source"] = source_element.get_text()

            search_results.append(result_dict)

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
