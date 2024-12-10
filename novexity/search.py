import os
import json
from urllib.parse import urlparse, parse_qs, unquote
import requests
from bs4 import BeautifulSoup
from collections import OrderedDict
from .requests_ip_rotator.ip_rotator import ApiGateway
from .user_agents import get_useragent


class Configuration:
    """
    Configuration class to manage AWS access keys.
    """

    def __init__(self):
        self.AWS_ACCESS_KEY_ID = os.getenv("GOOGLE_SEARCH_AWS_ACCESS_KEY_ID")
        self.AWS_ACCESS_KEY_SECRET = os.getenv("GOOGLE_SEARCH_AWS_SECRET_ACCESS_KEY")


config = Configuration()  # Initialize the configuration

# Valid keys for search result fields
VALID_KEYS = {
    "position",
    "title",
    "link",
    "displayed_link",
    "favicon",
    "snippet",
    "source",
}

# Titles to be excluded from search results
invalid_titles = ["Description"]


class NovexitySearch:
    """
    Class for managing the Novexity search with gateway lifecycle.
    """

    gateway = None  # Shared gateway instance across all searches

    @classmethod
    def init_gateway(cls, regions=None):
        """
        Initialize the API gateway.
        """
        if cls.gateway is None:
            cls.gateway = ApiGateway(
                "https://www.google.com",
                access_key_id=config.AWS_ACCESS_KEY_ID,
                access_key_secret=config.AWS_ACCESS_KEY_SECRET,
                regions=regions or ["us-east-1", "us-west-1"],
                verbose=True,
            )
            cls.gateway.start()
        else:
            print("Gateway is already initialized.")

    @classmethod
    def shutdown_gateway(cls):
        """
        Shutdown the API gateway.
        """
        if cls.gateway:
            cls.gateway.shutdown()
            cls.gateway = None
        else:
            print("Gateway is not initialized.")

    def __init__(self, params):
        self.query = params.get("q")
        self.country = params.get("country")
        self.lang = params.get("lang", "en")
        self.lang_restrict = params.get("lang_restrict")
        self.location = params.get("location")
        self.fields = params.get("fields", [])

    def get_dict(self):
        """
        Perform a search and return results.
        """
        if not NovexitySearch.gateway:
            raise RuntimeError("Gateway is not initialized. Call `init_gateway` first.")
        return self._search(
            self.query,
            *self.fields,
            country=self.country,
            lang=self.lang,
            location=self.location,
        )

    def _search(
        self, query, *fields, country=None, lang="en", location=None, lang_restrict=None
    ):
        """
        Perform the search and fetch results using the API gateway.
        """
        session = requests.Session()
        session.mount("https://www.google.com", NovexitySearch.gateway)

        url = f"https://www.google.com/search?q={query}"
        if country:
            url += f"&gl={country}"
        if lang:
            url += f"&hl={lang}"
        if lang_restrict:
            url += f"&lr={lang_restrict}"
        if location:
            url += f"&uule={location}"

        search_results = []
        headers = {"User-Agent": get_useragent()}
        position = 0

        while True:
            try:
                response = session.get(url, headers=headers)
                if response.status_code == 200:
                    print("Received a 200 OK response!")
                    break
                print("Status Code:", response.status_code, "Switching IP...")
                headers["User-Agent"] = get_useragent()
            except requests.exceptions.Timeout:
                print("Request timed out. Switching IP...")
            except requests.ConnectionError:
                print("Connection error. Switching IP...")
            except Exception as error:
                print("Unexpected error:", error, ". Switching IP...")
                headers["User-Agent"] = get_useragent()

        if response.status_code != 200:
            return {"error": f"Failed with status code {response.status_code}"}

        soup = BeautifulSoup(response.text, "html.parser")
        if not soup.select_one("div#search"):
            return {"error": "Search results not loaded."}

        for result in soup.select(".tF2Cxc"):
            result_dict = OrderedDict()

            if "position" in fields or not fields:
                position += 1
                result_dict["position"] = position

            title_element = result.select_one("h3")
            if title_element and ("title" in fields or not fields):
                result_dict["title"] = title_element.get_text()

            link_element = result.select_one("a")
            if (
                link_element
                and link_element.has_attr("href")
                and ("link" in fields or not fields)
            ):
                result_dict["link"] = clean_url(link_element["href"])

            displayed_link_element = result.select_one(".TbwUpd.NJjxre")
            if displayed_link_element and ("displayed_link" in fields or not fields):
                result_dict["displayed_link"] = displayed_link_element.get_text()

            favicon_element = result.select_one(".TbwUpd.NJjxre img")
            if favicon_element and ("favicon" in fields or not fields):
                result_dict["favicon"] = favicon_element["src"]

            snippet_parts = result.select(".VwiC3b.yXK7lf span")
            if snippet_parts and ("snippet" in fields or not fields):
                result_dict["snippet"] = " ".join(
                    part.get_text() for part in snippet_parts
                )

            source_element = result.select_one("cite")
            if source_element and ("source" in fields or not fields):
                result_dict["source"] = source_element.get_text()

            if result_dict.get("title") not in invalid_titles:
                search_results.append(result_dict)

        return {"organic_results": search_results}


def configure(aws_access_key_id=None, aws_secret_access_key=None):
    """
    Configure AWS keys for the search function.
    """
    if aws_access_key_id:
        config.AWS_ACCESS_KEY_ID = aws_access_key_id
    if aws_secret_access_key:
        config.AWS_ACCESS_KEY_SECRET = aws_secret_access_key


def format_json_output(data):
    """
    Format data into a JSON string.
    """
    return json.dumps(data, indent=4, ensure_ascii=False)


def clean_url(url):
    """
    Clean and extract the actual URL from the query string.
    """
    parsed = urlparse(url)
    url_qs = parse_qs(parsed.query)
    if "q" in url_qs:
        return unquote(url_qs["q"][0])
    elif "url" in url_qs:
        return unquote(url_qs["url"][0])
    return url
