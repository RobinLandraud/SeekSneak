# SeekSneak

![Python Lover](https://forthebadge.com/images/badges/made-with-python.svg) ![Built with Love](https://forthebadge.com/images/badges/built-with-love.svg)

SeekSneak is a bot to find the best prices to buy and resell sneakers. It compares inventory and other information across many sites to give you the best choices for making money buying and selling. Simply type the desired pair into our search tool.

![Sneakers](https://media.giphy.com/media/5WlXGaNnB0N6o/giphy.gif)

Our algorithm scrapes the sites for you and uses their APIs.

## Features

### Already severals APIs Available:
- **StockX**
- **Restocks**

### APIs coming soon:
- **Goat**

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

## Deploying

1. After installing all dependencies, please clone the repository:
   ```bash
   $ git clone git@github.com:RobinLandraud/Sneaker.git
   ```

2. To launch the bot on your browser, launch the main.py file at the root of the file:
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

![Work on my Machine](https://forthebadge.com/images/badges/works-on-my-machine.svg)