# Beginner-Friendly Python Toolkit for Web Scraping

[![Documentation Status](https://readthedocs.org/projects/524-group29-webscraping/badge/?version=latest)](https://524-group29-webscraping.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/github/UBC-MDS/524_group29_webscraping/graph/badge.svg?token=uJT3IDb3z1)](https://codecov.io/github/UBC-MDS/524_group29_webscraping)
[![ci-cd](https://github.com/UBC-MDS/524_group29_webscraping/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/UBC-MDS/524_group29_webscraping/actions/workflows/ci-cd.yml)

A Python package for simplified web scraping functionality for data scientists new to web scraping.

## Create Virtual Environment

We recommend that you first create a new `conda` environment with the latest version of Python (if not, then version 3.9 or higher). You can do so with the command below:

```bash
conda create --name webscraping python=3.12 -y
```

After the environment is created, activate the environment:

```bash
conda activate webscraping
```

## Installation

You can then install the package in your environment using the command:

```bash
pip install dsci524_group29_webscraping
```

After installation, have fun scraping the web!

## Functions

The package has three functions that you can use in a typical web scraping workflow as follows:

- `fetch_html(url)`: Retrieves the raw HTML content from the specified URL, handling HTTP requests and potential errors. You can capture the results in a `string` variable to use later in your pipeline.
- `parse_content(html, selector, selector_type)`: Parses the provided HTML content using CSS selectors or XPath to extract specified data. The `html` parameter is a `string` value retrieved using `fetch_html(url)`. This function returns a list of values that you can use in the final part of your pipeline.
- `save_data(data, format, destination)`: Saves the extracted data into the desired format (e.g., TXT, CSV, JSON) at the specified destination path.

## Usage

The examples below demonstrate how to use the main functions in this package. The examples fetch content from the [IANA Example Domain](https://example.com):

### 1. Fetch HTML Content
```python
from dsci524_group29_webscraping import fetch_html

# Fetch the raw HTML content from a webpage
url = "https://example.com"
html_content = fetch_html(url)
print(html_content)  # Outputs the HTML content of the page
```

### 2. Parse Content
```python
from dsci524_group29_webscraping import parse_content

# Parse the HTML content to extract specific elements
selector = "h1"  # Example: extract all <h1> header elements
selector_type = "css"  # Use CSS selectors
extracted_data = parse_content(html_content, selector, selector_type)
print(extracted_data)  # Outputs a list of the extracted data
```

### 3. Save Data
```python
from dsci524_group29_webscraping import save_data

# Save the extracted data to a CSV file
data = [{'value': 'Example Domain'}]  # Example data
file_path = save_data(data, format="csv", destination="output.csv")
print(f"Data saved to: {file_path}")
```

This package simplifies the process of fetching, parsing, and saving web data, making it ideal for beginners.
Usage is simplified by following the three simple steps above.

## Python Ecosystem

While libraries like [`BeautifulSoup`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) 
and [`Scrapy`](https://scrapy.org/) offer comprehensive web scraping capabilities,
*dsci524_group29_webscraping* aims to provide a more streamlined and beginner-friendly approach. 
By focusing on three core functions, it abstracts 
the complexities involved in web scraping, making 
it accessible for quick tasks and educational purposes.

**Similar Packages:**

- [`webscraping`](https://github.com/richardpenman/webscraping): Provides web scraping functions but contains a rich set of functionality that is beyond beginner level.
- [`webscraping_tools`](https://github.com/Jack-Tilley/webscraping_tools): Offers similar functionalities and many more that in our opinion, places it in the intermediate level.

*dsci524_group29_webscraping* differentiates itself by offering a simple set of functions 
that do the job for simple, beginner level needs.

## Contributors

- Lixuan Lin
- Hui Tang
- Sienko Ikhabi

## Contributing

Interested in contributing? Check out the [contributing](CONTRIBUTING.md) guidelines. 

Please note that this project is released with a [Code of Conduct](CONDUCT.md). By contributing to this project, you agree to abide by the specified terms.

## License

Package `dsci524_group29_webscraping` was created by Lixuan Lin, Hui Tang and Sienko Ikhabi for the Master of Data Science, University of British Columbia. It is licensed under the terms of the MIT license.

## Credits

This project was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) from the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
