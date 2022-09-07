# SeekSneak

![Python Lover](https://forthebadge.com/images/badges/made-with-python.svg) ![Built with Love](https://forthebadge.com/images/badges/built-with-love.svg)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
  - [Already severals APIs Available](#already-severals-apis-available)
  - [APIs coming soon](#apis-coming-soon)
- [User Guide](#user-Guide)
  - [Prerequisite](#prerequisite)
  - [Python Libraries](#python-libraries)
  - [Deploying](#deploying)
- [Proxies](#proxies)
- [Contributing](#contributing)

## Introduction

SeekSneak is a bot to find the best prices to buy and resell sneakers. It compares inventory and other information across many sites to give you the best choices for making money buying and selling. Simply type the desired pair into our search tool.

![Sneakers](https://media.giphy.com/media/5WlXGaNnB0N6o/giphy.gif)

Our algorithm scrapes the sites for you and uses their APIs.

## Features

### Already severals APIs Available:
- **StockX**
- **Restocks**
- **Goat**

### APIs coming soon:
- **Flight Club**

Many websites and data will be added to our bot to improve its research and give you the most relevant results possible.

## User Guide

### Prerequisite:

Here is the list of languages, package manager and libraries useful for deploying the bot :

- **Python 3.8.10**
- **pip 22.0.3**

### Python Libraries:
- werkzeug
   ```bash
   $ pip install Werkzeug
   ```
- flask
   ```bash
   $ pip install Flask
   ```
- flask_login
   ```bash
   $ pip install Flask-Login
   ```
- flask_wtf
   ```bash
   $ pip install Flask-WTF
   ```
- flask_ckeditor
   ```bash
   $ pip install Flask-CKEditor
   ```
- sqlalchemy
   ```bash
   $ pip install SQLAlchemy
   ```
- beautifulsoup4
   ```bash
   $ pip install beautifulsoup4
   ```
- requests
   ```bash
   $ pip install requests
   ```
- json
   ```bash
   $ pip install json
   ```

### Deploying

1. After installing all dependencies, please clone the repository:
   ```bash
   $ git clone git@github.com:RobinLandraud/Sneaker.git
   ```

2. To launch the bot on your browser, launch the main.py file at the root of the repository:
   ```bash
   $ ./main.py
   ```
   OR
   ```bash
   $ python main.py
   ```

3. After testing all the proxies, your command prompt should show you the url on which you can use the bot with a web GUI. Here is an example:
   ```bash
   $ Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
   ```

## Proxies

Our bot uses a list of proxies in order to avoid captcha and to be as fast and secure as possible. You can change or modify this list from the proxies.txt file available at the root of the project. 

To add a proxy, please give the information in order separated by a colon: IP, PORT and TYPE.
Here is an example:
   ```bash
   $ 166.111.185.77:7078:HTTP
   ```

## Contributing

SeekSneak welcomes any contributions from anyone! Please make SeekSneak a better tool for every reseller!

![Work on my Machine](https://forthebadge.com/images/badges/works-on-my-machine.svg)