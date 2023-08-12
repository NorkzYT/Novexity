<h1 align="center">Novexity</h1>
<div align="center">
    <img src="https://github.com/NorkzYT/NexusAPI/assets/53381649/2a2634c0-ada0-4795-ba5b-bdc60414baa9" width="200">
</div>

<h4 align="center">Open Source SerpAPI Google Search Alternative 🌐</h4>
<h5 align="center">Scrape Google Search Results Fast and Easy ✨</h5>

<div align="center">

<a href="https://github.com/NorkzYT/NexusAPI/graphs/contributors"><img src="https://img.shields.io/github/contributors/NorkzYT/NexusAPI.svg" alt="Contributors"></a>
<a href="https://github.com/NorkzYT/NexusAPI/network/members"><img src="https://img.shields.io/github/forks/NorkzYT/NexusAPI.svg" alt="Forks"></a>
<a href="https://github.com/NorkzYT/NexusAPI/stargazers"><img src="https://img.shields.io/github/stars/NorkzYT/NexusAPI.svg" alt="Stargazers"></a>
<a href="https://github.com/NorkzYT/NexusAPI/issues"><img src="https://img.shields.io/github/issues/NorkzYT/NexusAPI.svg" alt="Issues"></a>
<a href="https://github.com/NorkzYT/NexusAPI/issues?q=is%3Aissue+is%3Aclosed"><img src="https://img.shields.io/github/issues-closed/NorkzYT/NexusAPI.svg" alt="Closed Issues"></a>
<a href="https://github.com/NorkzYT/NexusAPI/blob/master/LICENSE"><img src="https://img.shields.io/github/license/NorkzYT/NexusAPI.svg" alt="MIT License"></a>

</div>

<h2 align="left">🔧 Installation</h2>

```bash
pip install Novexity
```

<h2 align="left">🛠 Setup</h2>

Make an AWS account and create a new IAM user with the permission of `AmazonAPIGatewayAdministrator`. Then, to find your access key ID and secret access key, follow the [official AWS tutorial](https://docs.aws.amazon.com/powershell/latest/userguide/pstools-appendix-sign-up.html).

Set up your AWS credentials in a `.env` file or with [awscli](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) by running `aws configure``.

```env
GOOGLE_SEARCH_AWS_ACCESS_KEY_ID=your_access_key_id
GOOGLE_SEARCH_AWS_SECRET_ACCESS_KEY=your_secret_access_key
```

<h2 align="left">📖 Usage</h2>

Example usage:

```python
from dotenv import load_dotenv
import json

load_dotenv()

from novexity.search import search

results = search("Time")
print(json.dumps(results, indent=4))
```

Output:

```json
{
  "organic_results": [
    {
      "position": 1,
      "title": "Time.is - exact time, any time zone",
      "link": "https://time.is/",
      "displayed_link": "Time.is https://time.is",
      "favicon": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAVFBMVEVHcEzOMULqFjLrByrxDC3yFTLxACnwFDHuHDakT1jKQlDkITjrEzDrGzXxABwAq6PrDi31b3r//v7wAAj3iZL6vMH81djzO0395OXfHjUAsaDGMD8ufdWhAAAAHHRSTlMAVMLx////zXckOpPo0/8H3v//////////ugp3X9i4HQAAALFJREFUeAG90kUCwzAMAEEFrLJBcvj/7yyEQSm3c16z4W+CMIrVFV6pqzjabGFkgwK1g06Iohhae1xxgMYBVxzFFYQ1TrhCzQK9KEwTWGy4+H6gHfWTaM3CDOxJ3QrN7JKUlwFyQhmz8inlXqMQIKfkc6IkY41ykBDljhmvxEB7T56xZxYXpa9QCAR/CtSzz33AFfbZLwcFiqKyC0qxOO5gEBT2GI0cbViVMGHKCQNfcwEXFBWOnAumeQAAAABJRU5ErkJggg==",
      "description": "7 million locations, 57 languages, synchronized with atomic clock time.",
      "snippet": "7 million locations, 57 languages, synchronized with atomic clock time.",
      "source": ""
    },
    {
      "position": 2,
      "title": "TIME | Current & Breaking News | National & World Updates",
      "link": "https://time.com/",
      "displayed_link": "Time Magazine https://time.com",
      "favicon": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAV1BMVEXpBgbpBATpAwPpAgLwWVn0hYXzfX3zdnbzdHTycHDybW30gYH3pqb////pDQ3ya2v97e3+8vLuR0fsJCT84eH96OjsKCjsLi7vUVHuPDztNDTxX1/xZma8Pt5HAAAAhklEQVR4Ae3TRRLEIAAAQdxhNZ7/fzPuLtdMFOgqToBDQYTwLIRgBwhlvEhIKZVSxVvwIk06YOxiBjQ5JV917G3thzYDzjrwBbju97fW85uBI64HdbACAWqmww74iwBEDWiagaZV8AB4EzwA4hpgtALipDoXOoxXQFScljQtnu/qFk0InCgHwCwQIEC0gnAAAAAASUVORK5CYII=",
      "description": "Breaking news and analysis from TIME.com. Politics, world news, photos, video, tech reviews, health, science and entertainment news.",
      "snippet": "Breaking news and analysis from TIME.com. Politics, world news, photos, video, tech reviews, health, science and entertainment news.",
      "source": ""
    },
    {
      "position": 3,
      "title": "Time",
      "link": "https://en.wikipedia.org/wiki/Time",
      "displayed_link": "Wikipedia https://en.wikipedia.org \u203a wiki \u203a Time",
      "favicon": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAM1BMVEUAAAD+/v41NTUBAQEAAABZWVknJycWFhaZmZmIiIjp6ellZWXMzMzX19eurq54eHhHR0dExXFyAAAAAXRSTlMAQObYZgAAAPtJREFUeAG8kAWOBDAMA9d1Sin+/7XXbpZZdBaURlMrhx28ycGCD/n0bvkBwJf8C+AoIvRAWGtMyHGtCWkfxW+DRopuuIjUtTQJDStevNoXWaRjRSllLd1O8FFhgEZx2BmkAmHC8HwpOUyxSA50VqOjXgAl50URvNWPBRcAnmwnhbcduthqQCO9KYTFBG7eDWoK1T47AZX9DuiUYT/TuhX3MGpnD51kPprSA9Dl+BCKl7jWHHEHmHsLWhNZZMxPQCLTEuy+cYF6D9i8Q5e2Lcyz4AGwKdJbX0p7AegC2qnvxAsAxQRAYH8J6Dg1a/lvpKRJinMW4cxLMPsDAJjSCaG8cPmnAAAAAElFTkSuQmCC",
      "description": "Time is the continued sequence of existence and events that occurs in an apparently irreversible succession from the past, through the present, into the\u00a0...",
      "snippet": "Time is the continued sequence of existence and events that occurs in an apparently irreversible succession from the past, through the present, into the\u00a0...",
      "source": ""
    },
    {
      "position": 4,
      "title": "TIME | English meaning - Cambridge Dictionary",
      "link": "https://dictionary.cambridge.org/dictionary/english/time",
      "displayed_link": "Cambridge Dictionary https://dictionary.cambridge.org \u203a dictionary \u203a time",
      "favicon": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBwgHBgkIBwgKCgkLDRYPDQwMDRsUFRAWIB0iIiAdHx8kKDQsJCYxJx8fLT0tMTU3Ojo6Iys/RD84QzQ5OjcBCgoKDQwNGg8PGjclHyU3Nzc3Nzc3Nzc1Nzc3Nzc3NzU3Nzg3Mjc3Ny03Nzc3Nzc3NzcuNzc1Nzc3MjU3OC01N//AABEIACAAIAMBEQACEQEDEQH/xAAaAAACAgMAAAAAAAAAAAAAAAAEBgIFAQMH/8QAKRAAAQMCBQQBBQEAAAAAAAAAAQIDEQAEBRIhIjETFEFhUQcVJFKRBv/EABkBAAMBAQEAAAAAAAAAAAAAAAECAwUABP/EACMRAAEEAgEEAwEAAAAAAAAAAAEAAgMRITFRBBLR8AUikRP/2gAMAwEAAhEDEQA/AOVAVoKKOw7C7zEnEN2TBdUtxLSRmA3KMAan3UZOpiieGPNE6VWQPkaXNGAp3+FXmHOravWemtDhbUMwVuGhEg+qMXUxSvMbDZCEkL42hzhgoMoNeilK1gJoUuTr9P7q2Qex7RBv37tAYuy7CmJhKVBEQrKrdB540rL+QpsrCW3eL4NrR6LMbvtgWSOcfudLf/uLi2cUbEWiO9Zul9e8Dm58jMlRKIATJM6cRHun+N+07z2axfOkOvxG2zuiBwK53jSUFNitchZdodktpcQXgotBQKwkwSmdY9xU06bLbCWGHmne0xPrpzrCrZxtKUlJgFG9SiQYndIP8pe6xWEdGxaI+22j/Wdu7XG+qTnU4rKtbhk+f2Mg6/HPMsHluBSUi8m0qurRnV05yScubmPE1UlLSCFRCcqxTid6ZJuVknkwNfGulARM9J8ru4qRxO8AP5CtZnaPIg+Pij/NvpPld3FVy10SVwC//9k=",
      "description": "a particular period of time for which something has been happening, or that is needed for something: After a time, it became clear that nobody was interested in\u00a0...",
      "snippet": "a particular period of time for which something has been happening, or that is needed for something: After a time, it became clear that nobody was interested in\u00a0...",
      "source": ""
    },
    {
      "position": 5,
      "title": "Time (TV Series 2021",
      "link": "https://www.imdb.com/title/tt13138834/",
      "displayed_link": "IMDb https://www.imdb.com \u203a title",
      "favicon": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAXVBMVEX1xRiigg9FNwZWRQjCnBNiTwnluBbUqxR6YgxsVwqJbg2BaAwAAAAYEwKtixEJBwDIoRMRDQGnhhA2LAW6lRKQcw4nHwNcSglNPgcyKAQ9MQaRdA55YQuXeg7arxVEfIgDAAAAiElEQVR4Ae3ONQKEMAAAwRwui7v+/5mHO5RUbKSaiHi1r58kK5KkapIk6VKXIUzJEptsHBc8BfAhgDBCPQOsEcSQdMB1D8BD8kbg9cADew9SvHQDspx8DwqHfANU9QRKzGegkgzAgKp7Qj4BG3cAdPvwyVrM+c2vbVy90ZpudvnCbZSmEa/29Qd3QQxgg+pf3wAAAABJRU5ErkJggg==",
      "description": "Time: Created by Jimmy McGovern. With Siobhan Finneran, Sean Bean, Stephen Graham, James Nelson-Joyce. Eric is a prison officer who tries to protect those\u00a0...",
      "snippet": "Time: Created by Jimmy McGovern. With Siobhan Finneran, Sean Bean, Stephen Graham, James Nelson-Joyce. Eric is a prison officer who tries to protect those\u00a0...",
      "source": ""
    },
    {
      "position": 6,
      "title": "Time Definition & Meaning",
      "link": "https://www.dictionary.com/browse/time",
      "displayed_link": "Dictionary.com https://www.dictionary.com \u203a browse \u203a time",
      "favicon": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABHElEQVR4AWNgUO6+z6DS/X8gMNhuEGNAMS6JUQeMOoAUcP/xx//7Tzz6H1+27b+C/Ux6OwAT1E88Sl0HvP/0nWRHnL/26r+A0STqOOD+kw//C5r3/XeIXvE/oWz7/wnzz4CCHOQwQo6gahSALMWIYwPfBXgd0TDxKNXTACg04OoU7GfhVfv+4w9QVFDXAfPXXkZxACGQULZtQB0ASjMD64ANu27T2QGYiXfAHTDC04B/xga6OgC9FAWpGzgHxJdtHzgHrN8Nzn50dgAi5VNWGy4AWkKaAxBVd0HLPuo0yQIy14MSESEHgFpE4ODOb9kH8jX124QNk46CfIbsALo3SkHtAHi00N8BCAxqFYGy1nBqlo86QLlrwLrnILsBIthS4ofLBq4AAAAASUVORK5CYII=",
      "description": "Sometimes Time . \u00b7 a limited period or interval, as between two successive events: a long time. \u00b7 a particular period considered as distinct from other periods:\u00a0...",
      "snippet": "Sometimes Time . \u00b7 a limited period or interval, as between two successive events: a long time. \u00b7 a particular period considered as distinct from other periods:\u00a0...",
      "source": ""
    }
  ]
}
```

<h2 align="left">🤝 Contributing</h2>

1. 🍴 Fork the repo!

2. 🧪 Run the tests to ensure everything is working: `python -m unittest tests.test_google_search`

3. 🔧 Make your changes.

4. 📦 Push your changes to a new branch and create a Pull Request.

Every contribution is welcome! 💖

<h2 align="left">📄 License</h2>

This project is licensed under the MIT License. For more details, see [LICENSE](https://github.com/NorkzYT/NexusAPI/blob/master/LICENSE).
