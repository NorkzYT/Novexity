<h1 align="center">Novexity</h1>
<div align="center">
    <img src="https://github.com/NorkzYT/NexusAPI/assets/53381649/2a2634c0-ada0-4795-ba5b-bdc60414baa9" width="200">
</div>

<h4 align="center">Open Source SerpAPI Google Search Alternative 🌍</h4>
<h5 align="center">Scrape Google Search Results Fast and Easy.</h5>

<div align="center">

<a href="https://github.com/NorkzYT/NexusAPI/graphs/contributors"><img src="https://img.shields.io/github/contributors/NorkzYT/NexusAPI.svg" alt="Contributors"></a>
<a href="https://github.com/NorkzYT/NexusAPI/network/members"><img src="https://img.shields.io/github/forks/NorkzYT/NexusAPI.svg" alt="Forks"></a>
<a href="https://github.com/NorkzYT/NexusAPI/stargazers"><img src="https://img.shields.io/github/stars/NorkzYT/NexusAPI.svg" alt="Stargazers"></a>
<a href="https://github.com/NorkzYT/NexusAPI/issues"><img src="https://img.shields.io/github/issues/NorkzYT/NexusAPI.svg" alt="Issues"></a>
<a href="https://github.com/NorkzYT/NexusAPI/issues?q=is%3Aissue+is%3Aclosed"><img src="https://img.shields.io/github/issues-closed/NorkzYT/NexusAPI.svg" alt="Closed Issues"></a>
<a href="https://github.com/NorkzYT/NexusAPI/blob/master/LICENSE"><img src="https://img.shields.io/github/license/NorkzYT/NexusAPI.svg" alt="MIT License"></a>

</div>

<h2 align="left">⚙ Installation</h2>

```bash
pip install NexusNova
```

<h2 align="left">📝 Usage</h2>

Make sure you have your AWS credentials set up in a .env file:

```env
GOOGLE_SEARCH_AWS_ACCESS_KEY_ID=your_access_key_id
GOOGLE_SEARCH_AWS_SECRET_ACCESS_KEY=your_secret_access_key
```

Use the `search` function to get Google search results:

```python
from nexus_nova.google_search import search
results = search("Your Query Here")
```

<h2 align="left">🤝 Contributing</h2>

1. 🍴 Fork the repo!

2. 🧪 Run the tests to ensure everything is working: `python -m unittest test_google_search.py`

3. 🔧 Make your changes.

4. 📦 Push your changes to a new branch and create a Pull Request.

Every contribution is welcome! 💖

<h2 align="left">📄 License</h2>

This project is licensed under the MIT License. For more details, see [LICENSE](https://github.com/NorkzYT/NexusAPI/blob/master/LICENSE).
