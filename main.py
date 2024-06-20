from Airbnb import scraper

scraper = scraper.WebScrape

def main(web_scrape):
    urls = [
                'https://www.airbnb.co.uk/rooms/33571268',
                'https://www.airbnb.co.uk/rooms/33090114',
                'https://www.airbnb.co.uk/rooms/50633275'
                ]
    
    web_scrape(urls)

if __name__ == '__main__':
  main(scraper)