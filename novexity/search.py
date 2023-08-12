import os
import time
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
        "Ensure both GOOGLE_SEARCH_AWS_ACCESS_KEY_ID and GOOGLE_SEARCH_AWS_SECRET_ACCESS_KEY are set in the .env file or system environment variables.")


def search(query: str):
    """
    Searches Google for a given query string and returns the organic search results.

    Args:
    - query (str): The search term or phrase to look up on Google.

    Returns:
    - dict: A dictionary containing the organic search results, including position, title,
            link, displayed link, favicon, description, snippet, and source for each result.

    Raises:
    - Returns an error dictionary if the search fails.
    """
    headers = {
        "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4454.0 Safari/537.36'
    }

    gateway = ApiGateway("https://www.google.com", access_key_id=aws_access_key_id,
                         access_key_secret=aws_access_key_secret)
    gateway.start()

    session = requests.Session()
    session.mount("https://www.google.com", gateway)

    url = f"https://www.google.com/search?q={query}"
    response = None

    while True:
        response = session.get(url, headers=headers)
        if response.status_code == 200:
            break
        print('Status Code:', response.status_code, "Switching IP...")
        time.sleep(5)

    if response.status_code != 200:
        return {"error": "Failed to retrieve web page."}

    soup = BeautifulSoup(response.text, 'html.parser')
    search_results = []

    for index, result in enumerate(soup.select('div.tF2Cxc')):
        position = index + 1

        title = result.select_one('h3').get_text(
        ) if result.select_one('h3') else ''
        link = unquote(result.select_one('a')['href'].split("&")[0].replace(
            "/url?q=", "")) if result.select_one('a') else ''

        # Adjusting the displayed_link extraction
        displayed_link_parts = result.select_one('.TbwUpd')
        displayed_link = " ".join(
            displayed_link_parts.stripped_strings) if displayed_link_parts else ''

        favicon = result.select_one('.eqA2re.NjwKYd img')[
            'src'] if result.select_one('.eqA2re.NjwKYd img') else ''

        description_parts = result.select(
            '.MUxGbd.yXK7lf.MUxGbd.yDYNvb.lyLwlc')
        description = ' '.join(part.get_text() for part in description_parts)

        snippet = result.select_one('.VwiC3b.yXK7lf.MUxGbd.yDYNvb.lyLwlc span:last-child').get_text(
        ) if result.select_one('.VwiC3b.yXK7lf.MUxGbd.yDYNvb.lyLwlc span:last-child') else ''
        source = result.select_one('.TbwUpd.NJjxre.iUh30.apx8Vc.ojE3Fb span.VuuXrf').get_text(
        ) if result.select_one('.TbwUpd.NJjxre.iUh30.apx8Vc.ojE3Fb span.VuuXrf') else ''

        result_dict = {
            "position": position,
            "title": title,
            "link": link,
            "displayed_link": displayed_link,
            "favicon": favicon,
            "description": description,
            "snippet": snippet,
            "source": source
        }

        search_results.append(result_dict)
    gateway.shutdown()

    return {
        "organic_results": search_results
    }
