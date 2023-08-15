<h1 align="center">Novexity</h1>
<div align="center">
    <img src="https://github.com/NorkzYT/Novexity/assets/53381649/0ecb64b3-1465-4ddb-8947-dbcb192db5d4" width="200">
</div>

<h4 align="center">Open Source SerpAPI Google Search Alternative 🌐</h4>
<h5 align="center">Freely Scrape Google Search Results Fast and Easy ✨</h5>

<div align="center">

<a href="https://github.com/NorkzYT/Novexity/graphs/contributors"><img src="https://img.shields.io/github/contributors/NorkzYT/Novexity.svg" alt="Contributors"></a>
<a href="https://github.com/NorkzYT/Novexity/network/members"><img src="https://img.shields.io/github/forks/NorkzYT/Novexity.svg" alt="Forks"></a>
<a href="https://github.com/NorkzYT/Novexity/stargazers"><img src="https://img.shields.io/github/stars/NorkzYT/Novexity.svg" alt="Stargazers"></a>
<a href="https://github.com/NorkzYT/Novexity/issues"><img src="https://img.shields.io/github/issues/NorkzYT/Novexity.svg" alt="Issues"></a>
<a href="https://github.com/NorkzYT/Novexity/issues?q=is%3Aissue+is%3Aclosed"><img src="https://img.shields.io/github/issues-closed/NorkzYT/Novexity.svg" alt="Closed Issues"></a>
<a href="https://github.com/NorkzYT/Novexity/blob/master/LICENSE"><img src="https://img.shields.io/github/license/NorkzYT/Novexity.svg" alt="MIT License"></a>

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
import os
from novexity import search, configure
from dotenv import load_dotenv
load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv('GOOGLE_SEARCH_AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('GOOGLE_SEARCH_AWS_SECRET_ACCESS_KEY')
configure(aws_access_key_id=AWS_ACCESS_KEY_ID,
          aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

# Call the search function
novexity, returned_gateway = search(
    "Time")

# Save the results to search.json
with open("google-search.json", "w", encoding="utf-8") as file:
    file.write(novexity)

# Shut down the gateways
returned_gateway.shutdown()

```

Please remember that if gateways are not shutdown via the `shutdown()` method, you may be charged in the future.

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
      "snippet": "Your clock is 38 minutes and 57.8 seconds behind. Accuracy of synchronization was ±0.005 seconds. Time in New York, United States now: 11:39:03am.",
      "source": "https://time.is"
    },
    {
      "position": 2,
      "title": "TIME | Current & Breaking News | National & World Updates",
      "link": "https://time.com/",
      "displayed_link": "Time Magazine https://time.com",
      "favicon": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgAQMAAABJtOi3AAAABlBMVEX////0DAxCDAtVAAAAAXRSTlMAQObYZgAAAB5JREFUeAFjkP///weEEGA+wIFOMDAfYBg4Qv4HAwCWWB254jDUcwAAAABJRU5ErkJggg==",
      "snippet": "Breaking news and analysis from TIME.com. Politics, world news, photos, video, tech reviews, health, science and entertainment news.",
      "source": "https://time.com"
    },
    {
      "position": 3,
      "title": "Time",
      "link": "https://en.wikipedia.org/wiki/Time",
      "displayed_link": "Wikipedia https://en.wikipedia.org › wiki › Time",
      "favicon": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAM1BMVEUAAAD+/v41NTUBAQEAAABZWVknJycWFhaZmZmIiIjp6ellZWXMzMzX19eurq54eHhHR0dExXFyAAAAAXRSTlMAQObYZgAAAPtJREFUeAG8kAWOBDAMA9d1Sin+/7XXbpZZdBaURlMrhx28ycGCD/n0bvkBwJf8C+AoIvRAWGtMyHGtCWkfxW+DRopuuIjUtTQJDStevNoXWaRjRSllLd1O8FFhgEZx2BmkAmHC8HwpOUyxSA50VqOjXgAl50URvNWPBRcAnmwnhbcduthqQCO9KYTFBG7eDWoK1T47AZX9DuiUYT/TuhX3MGpnD51kPprSA9Dl+BCKl7jWHHEHmHsLWhNZZMxPQCLTEuy+cYF6D9i8Q5e2Lcyz4AGwKdJbX0p7AegC2qnvxAsAxQRAYH8J6Dg1a/lvpKRJinMW4cxLMPsDAJjSCaG8cPmnAAAAAElFTkSuQmCC",
      "snippet": "Time is the continued sequence of existence and events that occurs in an apparently irreversible succession from the past, through the present, into the ...",
      "source": "https://en.wikipedia.org › wiki › Time"
    },
    {
      "position": 4,
      "title": "Time and Date",
      "link": "https://www.timeanddate.com/",
      "displayed_link": "Time and Date https://www.timeanddate.com",
      "favicon": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAA0lBMVEVHcEz////////////9/v/////////////////////r6+v////////////////////////1+vH////////////////////++/fj5+D96tL3+fgWndn/xQD81+T/++13uT/f8PnsC2D19ObMzMzR58GZynPy7+7woW/BwcH/56//34JxvuWnp6f/6KP1v53qdR7thjvpcQ7J5fT6xdXyb5nwVIijo6ONjY2Kw1y22Jvxh31KrN663/LuL3Sfz+v2p7yWlpahoaH/1E//00zqcwD41L+JE8JMAAAAFnRSTlMAPqzn/CzLBxhN7ppdsr5+jvF2gtiD5PU8twAAAZFJREFUOI19k+eSgkAQhAkLQoFg6dUQlCCgeIc5W4bL7/9Kt7ugLKg3P0Doz55eaobjKqVIvMQ9K0kTgZao8Y07tSE1gSlZrSGKBrVqVlpJcl3HxZhI6IGOiZu/Ub60LIbgi3xMvGgyccqnF4UCavFfcnnt9d78kuhQAxrQshPEAI6TtyIWPPnhJvt9UgJO+jOlhIkBgfYeBMEgugJ+OpvNI/pRMYByhyAIDi44X98TC6bz2WJ67aEUEQ/YwgbfcXyw0sUijfL3eh6BNhkkbgH/pvPrYdvkkGFI2kR2ebz8EJ4HoHE6QJZdToQZMgh4q/f1xsKACmEXV7YEZI+Hpb4+9/t9D1qclAPHE3YYj3EKFBOj4aZPAZ3jAC0vWfdIAtrbEUC8pZ3W5837ygI8FfhLo3AZUmP7M7Y/4iKDR254JnQmGcS73chlnmUyDSzgjip6PjOtClHRZTp1ighPChUjpT4DzGJsG+3HuqDctqbzv46JB11ajE5Wo1mVxfruYRO5XB9Dv99eypiCYQimypr/AdnvS9Q5ruOyAAAAAElFTkSuQmCC",
      "snippet": "Current Time (World Clock) and online and printable Calendars for countries worldwide. Find the best time for web meetings (Meeting Planner) or use the Time ...",
      "source": "https://www.timeanddate.com"
    },
    {
      "position": 5,
      "title": "What time is it - Exact time - Any time zone",
      "link": "https://vclock.com/time/",
      "displayed_link": "vClock.com https://vclock.com › time",
      "favicon": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAY1BMVEX////4+/7O3fGqw+WWtN/7/v/T4fJpl9MAW7wAV7wAU7oodMfq8fkAWbwAX747ecdjktF4oNccbMMHZcAAW73Y5PRYjc8AY8FBfspmlNIncMXj7PeHq9ufu+LA0+y0y+l9pNjnYfitAAABAElEQVR4AbzSAxbFMBAF0FcjTmrvf5NfNY//rRHNDP7Msh3XdWwP1/wgjL5igis0YIwLqZQk8rK5Drnyrd9A3tV3k4gU96hOsn07K7exEYTi8L0IsGEzPvbvLS0EtkqmxtdVjZ8mp7v+kqkDkpT4aiMfW3YkLHx1LLG/l7jHjhOVGGVcAD5rsOdGA0Y+Zz012dRxUZ9+wMCNmcaDit3TEKAm0XM7GTm7SY66wMbIEpF9XOaOz8OlWckGnCgWHEO9k3LmY1EekwVPhMFTur0s0fShYFKRGP9YcglX6VhyqeKh9nFAy2/RlsNQCs5YQHFml8l7nGAgIsmEP+Mw0jm/AgDVXwzahod34wAAAABJRU5ErkJggg==",
      "snippet": "Online clock. What time is it in different regions of United States, Canada, Australia, Europe and the World.",
      "source": "https://vclock.com › time"
    },
    {
      "position": 6,
      "title": "Exact Time Clock Now (With Seconds, Milliseconds)",
      "link": "https://clock.zone/",
      "displayed_link": "Clock.Zone https://clock.zone",
      "favicon": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAALVBMVEVHcEwAAFUAAFUAAFUAAFUAAFX/AAAAAFhwAEGNADqxAC5OAEnLACIqAE/jABXKkiA9AAAABXRSTlMA7XPscvwJ5a0AAADoSURBVDiNlZPRFoQgCETNkhHN/v9zVywN3dbOzpPCVRhKY+zqfmq1xmy/06LNLHNgMfO8c/8BEF3L6EcALnIIeygEPJ2LBsDvdKpsEw0AapoOXFvWADindhbKl7gsdA8I+QBw5HiqfOqaTDEfjFKiViD0LlCuqa3VXvo5gEoLEI/NhJ5DqeBFUoG/AD5IKw6jjjTI9QCuMHtmDtVNX+I0KWJl4gaKyR2us9sBrXVoEwqgOv8yce9GQKZ3zh/a5Q2k5m0GoJVIjyUub/4RAHNtLP+dLa8/FtyT3t/F69OzcyA/bzu5Y7HmAzdJFrzSm6EUAAAAAElFTkSuQmCC",
      "snippet": "My main goal was to build a website where you can find real exact time. ... This clock shows time from our dedicated server synchronised with atomic clock.",
      "source": "https://clock.zone"
    },
    {
      "position": 7,
      "title": "TIME (@TIME) / X",
      "link": "https://twitter.com/TIME",
      "displayed_link": "Twitter https://twitter.com › TIME",
      "favicon": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAAAAABWESUoAAAA3ElEQVR4Ac2SGQDFMBBE1ylOcYpTner0neK0TnGpU53iFKc6xWl+p+f25D7InZ295Cv0mGjFUOzWDVVVa/WykaBiaBBFfsiyory3JASRjs8mInqxUGRw47CIBIy7Ew0Sh0nED4OXCwkNh8h7GrrgCkVK9a7w6Q2BjoVa6Oo9EZEDVJ7I1M4UeMDXzIEhvoukFxNMaP8o4gpon1l9qnqc7DcPIgpd7Ce0t/fJVO0q0qIsVeuY1XwNYK1gwm8J2GAqvHRF5mD7BcG0Rl6yegjw0BqdakE8Bni0RyjyDf4Y1Y0n0wNT4wAAAABJRU5ErkJggg==",
      "snippet": "isn't just the biggest K-pop act on the charts. They've become the biggest band in the world—full stop. “We climbed our way up slowly, so it feels like we ...",
      "source": "https://twitter.com › TIME"
    },
    {
      "position": 8,
      "title": "Time Converter and World Clock - Conversion at a Glance ...",
      "link": "https://www.worldtimebuddy.com/",
      "displayed_link": "World Time Buddy https://www.worldtimebuddy.com",
      "favicon": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAADwUlEQVR4AWJABqPAIaFdwSa5fb8NoJ1y3Jo0ieH4Xspex/K1bdu2bdvqXvPr2raNsY0byCTpyclbk2dwAVPn/E5YVf/uTnXpxDW0QDyJPF4yARyXcc4b6SNkr+mZ+AnPCLrr5U+VTV97qmwKnsSLGPQ5JiSWXDmiccDnHKE5PU9jTxFPl898FFQxA0EV08zT5YdwY1u/OyRK9xDk411GQDBezlSSCIZ9zZPV2n+nLsC5yzdg7ZUPOa99Ymc98ooREFI1C0zlDCJ+wIZWuTanZxtk/fzPSekTJLZWfSsgrHoOPKmyudzeHRXw70mnhiJ1TxUhOUTrVkB4zTwIEWSxma0L5/L6dw8L0JruRdx9nFPfCoisXQAP6ECTK+jfA1m//HvKe0/NXc4i0DcCouoWgYgWqz7h1IoG9kHWryggkF9g6+5b0H0uVkBM/RIEWGQrxDaoLxQNHqiA/06B7Il2+zjP2JwVQBfFNSwzsWwVrjVqrXjIB7J++++05LlPzhFBEbUL8tvzADJeQxjfuAJ3Zxnim5ZB/NJhK4AulAEMxksCf2gzgomNgISmFSASm1dBbGKTorVVKBvxg6yf6H/A8/0roYLmrIDkljVIwgsY9tfESo6/gVj8pPl9dzxD/R9gX2N9jmFsNW8FtK4DiUgJWMenTx+NgyNPqWriOZB15NRFyitY12fnPkHB8xmmtq1DamsA8ulyuph+W35K9frE3vv6Dzi8tl//WGra5xkrRkB6+wYQaXg5feU09TLZTD1byqGAP+HOdeT0RSgePJB+8zI0zzkrIKNjkz49Dxn91glIfJOSoBbKhv1w4cpN8Frvf/MnvxLu1zPo9UhM1nsIEwNDKC9AfLRUE1/J6dmBlZfeM2Iofuntb2hwZZ/BCJChY+wgIphHNKf9eb278PI736oCFYICP9AzFCsgrW0DDO2bPJASpzLriNsjterx5+Cj7/42Qr757SjVsFf3ec5ARjvSsQXip3OscN3NOf3kE7PPvA0Xr7o/C8Wyh841ArI6t4HpIitsGd/kBIm7tLb56kdw6baQNz/7jXLSYwXkdO9Abvcu5HTtAPmCxLkeueyubbSE1jiWM7DeOPMibOH/RPmw3+kzAvJ6duEw+b17btyj8QPjnOHuNwIK+/Y+Kujbh4K+PaaQ2Wc4T77WJXb7JK+YGtn83n2fEVDUtxtUPHAAxf0IWQefWukhPPo19rFfpL3kkz1W1OV79BGvVTbkCyod9P9UOuiDEqSUGPKz1ZyfYV+QvLMHMTX/R0VD7uUP1y08Jnm8PtpM8AAAAABJRU5ErkJggg==",
      "snippet": "Effortless time conversion and world time. Schedule conference calls, webinars & online meetings, plan travel and track flight arrival time across time ...",
      "source": "https://www.worldtimebuddy.com"
    }
  ]
}
```

### 🎯 Filtering Fields

🔍 You can filter info based on specific fields, if you do not choose any to filter with then all will appear in output. Here are the available fields:

- `title`
- `link`
- `displayed_link`
- `favicon`
- `snippet`
- `source`

🌟 **Example use**:

```python
# Call the search function with the fields you want to filter with
novexity, returned_gateway = search(
    "Time", 'title', 'link')
```

🌎 **Country-based Search**:

To tailor the search results to a specific country, you can use the `country` parameter. Simply provide the country's ISO 3166-1 alpha-2 code, available from [World Data's country codes list](https://www.worlddata.info/countrycodes.php).

```python
# Call the search function with the country parameter
novexity, returned_gateway = search(
    "Time", country="fr")
```

<h2 align="left">🤝 Contributing</h2>

1. 🍴 Fork the repo!

2. 🔧 Make your changes.

3. 📦 Push your changes to a new branch and create a Pull Request.

Every contribution is welcome! 💖

<h2 align="left">📄 License</h2>

This project is licensed under the MIT License. For more details, see [LICENSE](https://github.com/NorkzYT/Novexity/blob/master/LICENSE).
