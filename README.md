<h1 align="center">Novexity</h1>
<div align="center">
    <img src="https://github.com/NorkzYT/NexusAPI/assets/53381649/2a2634c0-ada0-4795-ba5b-bdc60414baa9" width="200">
</div>

<h4 align="center">Open Source SerpAPI Google Search Alternative 🌐</h4>
<h5 align="center">Freely Scrape Google Search Results Fast and Easy ✨</h5>

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

Set up your AWS credentials in your `.env` file or with [awscli](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) by running `aws configure`.

```env
GOOGLE_SEARCH_AWS_ACCESS_KEY_ID=your_access_key_id
GOOGLE_SEARCH_AWS_SECRET_ACCESS_KEY=your_secret_access_key
```

<h2 align="left">📖 Usage</h2>

Example usage:

```python
from dotenv import load_dotenv
load_dotenv()

from novexity import search

# Call the search function
formatted_json_string, returned_gateway = search(
    "Time",)

# Print the formatted JSON string
print(formatted_json_string)

# Shut down the gateways
returned_gateway.shutdown()

```

Please remember that if gateways are not shutdown via the `shutdown()` method, you may be charged in the future.

### 🎯 Filtering Fields

🔍 You can filter events based on specific fields, if you do not choose any to filter with then all will appear in output. Here are the available fields:

- `position`
- `title`
- `link`
- `displayed_link`
- `favicon`
- `description`
- `snippet`
- `source`

🌟 **Example use**:

```python
# Call the search function with the fields you want to filter with
formatted_json_string, returned_gateway = search(
    "Time", 'position', 'title', 'link', 'description', 'source')
```

Output:

```json
{
  "organic_results": [
    {
      "position": 1,
      "title": "TIME | Current & Breaking News | National & World Updates",
      "link": "https://time.com/",
      "displayed_link": "Time Magazine https://time.com",
      "favicon": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAV1BMVEXpBgbpBATpAwPpAgLwWVn0hYXzfX3zdnbzdHTycHDybW30gYH3pqb////pDQ3ya2v97e3+8vLuR0fsJCT84eH96OjsKCjsLi7vUVHuPDztNDTxX1/xZma8Pt5HAAAAhklEQVR4Ae3TRRLEIAAAQdxhNZ7/fzPuLtdMFOgqToBDQYTwLIRgBwhlvEhIKZVSxVvwIk06YOxiBjQ5JV917G3thzYDzjrwBbju97fW85uBI64HdbACAWqmww74iwBEDWiagaZV8AB4EzwA4hpgtALipDoXOoxXQFScljQtnu/qFk0InCgHwCwQIEC0gnAAAAAASUVORK5CYII=",
      "description": "Breaking news and analysis from TIME.com. Politics, world news, photos, video, tech reviews, health, science and entertainment news.",
      "snippet": "Breaking news and analysis from TIME.com. Politics, world news, photos, video, tech reviews, health, science and entertainment news.",
      "source": "https://time.com"
    },
    {
      "position": 2,
      "title": "Time.is - exact time, any time zone",
      "link": "https://time.is/",
      "displayed_link": "Time.is https://time.is",
      "favicon": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAVFBMVEVHcEzOMULqFjLrByrxDC3yFTLxACnwFDHuHDakT1jKQlDkITjrEzDrGzXxABwAq6PrDi31b3r//v7wAAj3iZL6vMH81djzO0395OXfHjUAsaDGMD8ufdWhAAAAHHRSTlMAVMLx////zXckOpPo0/8H3v//////////ugp3X9i4HQAAALFJREFUeAG90kUCwzAMAEEFrLJBcvj/7yyEQSm3c16z4W+CMIrVFV6pqzjabGFkgwK1g06Iohhae1xxgMYBVxzFFYQ1TrhCzQK9KEwTWGy4+H6gHfWTaM3CDOxJ3QrN7JKUlwFyQhmz8inlXqMQIKfkc6IkY41ykBDljhmvxEB7T56xZxYXpa9QCAR/CtSzz33AFfbZLwcFiqKyC0qxOO5gEBT2GI0cbViVMGHKCQNfcwEXFBWOnAumeQAAAABJRU5ErkJggg==",
      "description": "Your clock is 28 minutes and 23.7 seconds behind. Accuracy of synchronization was ±0.005 seconds. Time in New York, United States now: 11:28:29pm.",
      "snippet": "Your clock is 28 minutes and 23.7 seconds behind. Accuracy of synchronization was ±0.005 seconds. Time in New York, United States now: 11:28:29pm.",
      "source": "https://time.is"
    },
    {
      "position": 3,
      "title": "Time.gov",
      "link": "https://www.time.gov/",
      "displayed_link": "time.gov https://www.time.gov",
      "favicon": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAACFklEQVR4Ae2TA4ydQRSFZ23bthEugtpunNRRGSd1g1qxa9u2jah2G9R+vj03mT+Z5xdVO19yxjP3jIRGo9FoGCJKEX+KESNGZE6ePPn+ggULjnz69Kmn8EBGRkb34ODguwIEBQVdNspMampqOfrHy7bPnHvRHUNK2y2Rlpa2MzIykrKzs2n16tUWIhogXECQ3ZmZmSRAenr6YQTkMs/tDb3Lysoi7kfuUzzGGMfxeB2RkpLyMzc391l7e/vn8vJyWrduncnVBIJswmDDwA7IIY1d5nbU54kA4OChoaEvXXf3PTk5+eD+/fsHDhgw4EdxcbGbCQTZiCCGge2QVbY/hrmfKI5WNF7mEzh3NYBsn3DZ3TfoogB79+7tM3DgQFNJSYlhop96AooBkgam8aLyFKyQXRG3v8HcSaoBvnevBpgdO3YMBCY+iY0bN/4kolY0r8RkVwMGo70JBj5CFKiBINUErsNUXV1NixcvPtvZ2XkmKSnJLg3sgQhzMoVveO0ZCOrbABzaMPC6YkA9CXNZWRkVFRX9xFtxyEVX8CuGifOYu1U+ym2quF32vVFPgOfBwG2hgkHPoUOqAYOtW7cOGTlypL2hoYEweZ4AeLC5WPQADJkwzwKZvcjCV4AptcpmP8DADaGCo03ArmKFF65du9b3xIkTs4nIyWBCQkJSokJhYaFTbiAU8N2Ta2pqwoVGo9Fo/iZ+AX4C+JSMhaGwAAAAAElFTkSuQmCC",
      "description": "Alaska DAYLIGHT Time. AKDT (UTC-8). 03:25:04 A.M.. Alaska Map. Aleutian DAYLIGHT Time. HADT (UTC-9). 02:25:04 A.M.. Hawaii Standard Time. HST (UTC-10).",
      "snippet": "Alaska DAYLIGHT Time. AKDT (UTC-8). 03:25:04 A.M.. Alaska Map. Aleutian DAYLIGHT Time. HADT (UTC-9). 02:25:04 A.M.. Hawaii Standard Time. HST (UTC-10).",
      "source": "https://www.time.gov"
    },
    {
      "position": 4,
      "title": "Time Definition & Meaning",
      "link": "https://www.dictionary.com/browse/time",
      "displayed_link": "Dictionary.com https://www.dictionary.com › browse › time",
      "favicon": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABHElEQVR4AWNgUO6+z6DS/X8gMNhuEGNAMS6JUQeMOoAUcP/xx//7Tzz6H1+27b+C/Ux6OwAT1E88Sl0HvP/0nWRHnL/26r+A0STqOOD+kw//C5r3/XeIXvE/oWz7/wnzz4CCHOQwQo6gahSALMWIYwPfBXgd0TDxKNXTACg04OoU7GfhVfv+4w9QVFDXAfPXXkZxACGQULZtQB0ASjMD64ANu27T2QGYiXfAHTDC04B/xga6OgC9FAWpGzgHxJdtHzgHrN8Nzn50dgAi5VNWGy4AWkKaAxBVd0HLPuo0yQIy14MSESEHgFpE4ODOb9kH8jX124QNk46CfIbsALo3SkHtAHi00N8BCAxqFYGy1nBqlo86QLlrwLrnILsBIthS4ofLBq4AAAAASUVORK5CYII=",
      "description": "Sometimes Time . · a limited period or interval, as between two successive events: a long time. · a particular period considered as distinct from other periods: ...",
      "snippet": "Sometimes Time . · a limited period or interval, as between two successive events: a long time. · a particular period considered as distinct from other periods: ...",
      "source": "https://www.dictionary.com › browse › time"
    },
    {
      "position": 5,
      "title": "Time Definition & Meaning",
      "link": "https://www.merriam-webster.com/dictionary/time",
      "displayed_link": "Merriam-Webster https://www.merriam-webster.com › dictionary › time",
      "favicon": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAtFBMVEX/////+/v0yszplZfham3eVlrokpT88PDlgIPVAADgXGDspKbspafhZWjkeHvSAADdUVT20tTojZDdS1D429zYHCTbPEH++PjZJi7cQ0jfXWHXCxjrnJ7439/76Onnh4rjcnWesMupudDs8PW1w9jT3Oh6lLqInsDCz9/l6vHt+v/I0uEAGn5jg7AAJ4KSpsQmWZnb4uxSd6gAOolHbaMARo82Y50ANIcATpPwvL10jrZae6tsTasqAAABVElEQVR4Aa2TBY7CQBRAH07dcIcq7ta9/7nWJpkF2myMF6l8N95KoVgqVyrlarFAHrW6oqhVTS8ZimLWyFCy7CIIHMNyX717ihQDNJqt9pO8032N2+s/anhdMhgtJAOlQJaOK/O3iuQwtEYIxh65TEwEooA8FyKyY8F05gPBLMSP4sCP42QeRYu+sBzYsFxF4K/WQLiB7Q7WCaYrQo1hfzhCfFoDnJdcrj430A3RkgEk08OMXXIBiCN/fZgtI7jbUmEWLHfJNjyyPgT78zYJTuu9VJi4sE24nf39BuD7Df+6A/SeSLIC6Z7tB/4KgDSF0xaou6JMheT0LQ1ZiyzDPSRzoFn8v1Ejqw0AdZVc6hM5LCffwUiuW58cWmMk3QoZzBZICk01IxcZSo1us/EUv/W8tEDVmkiVUd0ak6FmKn1Tv9/1etOajMg/Pdew7Z57b/NOvgDpER404SSr2gAAAABJRU5ErkJggg==",
      "description": "1 of 3. noun · ˈtīm. plural times. Synonyms of time. 1. a. : the measured or measurable period during which an action, process, or condition exists or continues ...",
      "snippet": "1 of 3. noun · ˈtīm. plural times. Synonyms of time. 1. a. : the measured or measurable period during which an action, process, or condition exists or continues ...",
      "source": "https://www.merriam-webster.com › dictionary › time"
    },
    {
      "position": 6,
      "title": "Time",
      "link": "https://en.wikipedia.org/wiki/Time",
      "displayed_link": "Wikipedia https://en.wikipedia.org › wiki › Time",
      "favicon": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAM1BMVEUAAAD+/v41NTUBAQEAAABZWVknJycWFhaZmZmIiIjp6ellZWXMzMzX19eurq54eHhHR0dExXFyAAAAAXRSTlMAQObYZgAAAPtJREFUeAG8kAWOBDAMA9d1Sin+/7XXbpZZdBaURlMrhx28ycGCD/n0bvkBwJf8C+AoIvRAWGtMyHGtCWkfxW+DRopuuIjUtTQJDStevNoXWaRjRSllLd1O8FFhgEZx2BmkAmHC8HwpOUyxSA50VqOjXgAl50URvNWPBRcAnmwnhbcduthqQCO9KYTFBG7eDWoK1T47AZX9DuiUYT/TuhX3MGpnD51kPprSA9Dl+BCKl7jWHHEHmHsLWhNZZMxPQCLTEuy+cYF6D9i8Q5e2Lcyz4AGwKdJbX0p7AegC2qnvxAsAxQRAYH8J6Dg1a/lvpKRJinMW4cxLMPsDAJjSCaG8cPmnAAAAAElFTkSuQmCC",
      "description": "Time is the continued sequence of existence and events that occurs in an apparently irreversible succession from the past, through the present, into the ...",
      "snippet": "Time is the continued sequence of existence and events that occurs in an apparently irreversible succession from the past, through the present, into the ...",
      "source": "https://en.wikipedia.org › wiki › Time"
    },
    {
      "position": 7,
      "title": "TIME | definition in the Cambridge English Dictionary",
      "link": "https://dictionary.cambridge.org/us/dictionary/english/time",
      "displayed_link": "Cambridge Dictionary https://dictionary.cambridge.org › dictionary › time",
      "favicon": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBwgHBgkIBwgKCgkLDRYPDQwMDRsUFRAWIB0iIiAdHx8kKDQsJCYxJx8fLT0tMTU3Ojo6Iys/RD84QzQ5OjcBCgoKDQwNGg8PGjclHyU3Nzc3Nzc3Nzc1Nzc3Nzc3NzU3Nzg3Mjc3Ny03Nzc3Nzc3NzcuNzc1Nzc3MjU3OC01N//AABEIACAAIAMBEQACEQEDEQH/xAAaAAACAgMAAAAAAAAAAAAAAAAEBgIFAQMH/8QAKRAAAQMCBQQBBQEAAAAAAAAAAQIDEQAEBRIhIjETFEFhUQcVJFKRBv/EABkBAAMBAQEAAAAAAAAAAAAAAAECAwUABP/EACMRAAEEAgEEAwEAAAAAAAAAAAEAAgMRITFRBBLR8AUikRP/2gAMAwEAAhEDEQA/AOVAVoKKOw7C7zEnEN2TBdUtxLSRmA3KMAan3UZOpiieGPNE6VWQPkaXNGAp3+FXmHOravWemtDhbUMwVuGhEg+qMXUxSvMbDZCEkL42hzhgoMoNeilK1gJoUuTr9P7q2Qex7RBv37tAYuy7CmJhKVBEQrKrdB540rL+QpsrCW3eL4NrR6LMbvtgWSOcfudLf/uLi2cUbEWiO9Zul9e8Dm58jMlRKIATJM6cRHun+N+07z2axfOkOvxG2zuiBwK53jSUFNitchZdodktpcQXgotBQKwkwSmdY9xU06bLbCWGHmne0xPrpzrCrZxtKUlJgFG9SiQYndIP8pe6xWEdGxaI+22j/Wdu7XG+qTnU4rKtbhk+f2Mg6/HPMsHluBSUi8m0qurRnV05yScubmPE1UlLSCFRCcqxTid6ZJuVknkwNfGulARM9J8ru4qRxO8AP5CtZnaPIg+Pij/NvpPld3FVy10SVwC//9k=",
      "description": "time meaning: 1. the part of existence that is measured in minutes, days, years, etc., or this process considered…. Learn more.",
      "snippet": "time meaning: 1. the part of existence that is measured in minutes, days, years, etc., or this process considered…. Learn more.",
      "source": "https://dictionary.cambridge.org › dictionary › time"
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
