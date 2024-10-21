# url-enumeration
[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)


**enumurl** is a lightweight internal link scanner designed to crawl and analyze a specified website. Utilizing Python libraries such as `requests` and `BeautifulSoup`, this tool efficiently fetches web pages and extracts internal links.



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



## installation
- **1.Clone the repository**:
```
git clone https://github.com/hemaabokila/url-enumeration.git
cd url-enumeration
sudo pip install .
```
- **2.Run the script with the following options**:
```
enumurl <url>

```


## Example:
- **To scan a target machine (https://www.google.com)**:


```
enumurl www.google.com
```

## Example Output
- **After scanning, the tool will show results like this (for urls)**
```
https://www.google.com/setprefdomain?prefdom=EG&prev=
https://www.google.com.eg/&sig=K_fPiOBoNY8udrSz5SB6Bri7MLVKQ%3D
https://www.google.com/imghp?hl=ar&tab=wi
https://www.google.com/intl/ar/about.html
https://www.google.com/setprefs?sig=0_1TpgmDOTv8yu9tsxuUH9ZtM_WnQ%3D&hl=en&
```
## License
This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

## Author
- **Developed by Ibrahem abo kila**
- **Feel free to reach out for any questions or suggestions!**
  - `LinkedIn: `https://www.linkedin.com/in/ibrahem-abo-kila
  - `YouTube: `https://www.youtube.com/@cryptodome22





