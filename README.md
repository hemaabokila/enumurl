# enumurl

**enumurl** is a lightweight internal link scanner designed to crawl and analyze a specified website. Utilizing Python libraries such as `requests` and `BeautifulSoup`, this tool efficiently fetches web pages and extracts internal links.

> ![Screenshot_2024-09-25_10-32-49](https://github.com/user-attachments/assets/672b1723-a6c5-4ca3-a6dd-aa4e2cba66c8)

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Example](#Example)
- [Author](#Author)

## Features

- Crawl internal links within a website up to a depth of 2.
- Output discovered links directly in the command line.
- Handle errors gracefully while fetching pages.
- Lightweight and easy to use.

## Requirements

Before running the tool, ensure that you have the following Python packages installed:

- `requests`
- `beautifulsoup4`
- `colorama`

You can install these packages using pip:

```
pip install -r requirements.txt
```
## The required libraries:

- `requests`
- `beautifulsoup4`
- `colorama`
## installation
- **1.Clone the repository**:
```
git clone https://github.com/hemaabokila/enumurl.git
cd enumurl
pip install -r requirements.txt
sudo mv enumurl.py /usr/bin/enumurl && chmod +x /usr/bin/enumurl
```
- **2.Run the script with the following options**:
```
enumurl -t <url>

```


## Example:
- **To scan a target machine (https://www.google.com)**:

> ![Screenshot_2024-09-25_10-34-11](https://github.com/user-attachments/assets/8390a947-a6d6-4d47-a6e7-9d16acbfcfef)

```
enumurl -u https://www.google.com
```

## Example Output
- **After scanning, the tool will show results like this (for urls)**
```
https://www.google.com/setprefdomain?prefdom=EG&prev=https://www.google.com.eg/&sig=K_fPiOBoNY8udrSz5SB6Bri7MLVKQ%3D
https://www.google.com/imghp?hl=ar&tab=wi
https://www.google.com/intl/ar/about.html
https://www.google.com/setprefs?sig=0_1TpgmDOTv8yu9tsxuUH9ZtM_WnQ%3D&hl=en&source=homepage&sa=X&ved=0ahUKEwjOj9Sgr96IAxWCV0EAHQCwOEwQ2ZgBCAY
```

## Author
- **Developed by Ibrahem abo kila**
- **Feel free to reach out for any questions or suggestions!**
  - `LinkedIn: Connect with me`
  - `YouTube: Watch my videos`





