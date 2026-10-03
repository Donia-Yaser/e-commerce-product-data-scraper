# E-Commerce Product Data Scraper

A Python web scraping project that extracts product informatio from Shopkund's men's kurta category and saves the collected data to a csv file.

## Features

- Scrapes product data from multiple pages
- Automatically follows the website's pagination
- Extracts product names, urls, special prices, and old prices

## Technologies

- Pyhton
- Requests
- Selectolax
- Pandas

## How it works

The scraper starts from the men's kurta category page and extracts the products available on the page.

It then looks for the website's **Next** page link. If another page exists, the scraper follows the link and repeats the process.

This continues automatically until there are no more pages.

# Installation

Clone the repository:

```bash
git clone https://github.com/Donia-Yaser/e-commerce-product-data-scraper.git