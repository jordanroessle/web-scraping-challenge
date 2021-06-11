import pandas as pd
from bs4 import BeautifulSoup
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager

def scrape():
    # browser setup
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # beautiful soup to grab html code from first webpage
    url = "https://redplanetscience.com/"
    browser.visit(url)
    soup = BeautifulSoup(browser.html, 'html.parser')
    browser.quit()

    # grab the newest news title and paragraph 
    news_title = soup.find('div', class_ = 'content_title').text
    news_p = soup.find('div', class_ = 'article_teaser_body').text

    # browser for next url, beautiful soup to grab html
    browser = Browser('chrome', **executable_path, headless=False)
    url = "https://spaceimages-mars.com/"
    browser.visit(url)
    soup = BeautifulSoup(browser.html, "html.parser")
    browser.quit()

    # grab desired image
    featured_image_url = soup.find("img", class_="headerimage fade-in")
    featured_image_url = url + featured_image_url['src']

    # use pandas read_html to grab table from the next url
    url = "https://galaxyfacts-mars.com/"
    tables = pd.read_html(url)
    df = tables[0]

    # cleaning the table, removing first line and renaming columns
    df = df.iloc[1:]
    df.columns = ["Desciption", "Mars", "Earth"]
    df.reset_index(drop=True, inplace=True)

    # exporting html code for table after cleaning 
    df.to_html("MarsVsEarth.html")

    # browser for next url,
    browser = Browser('chrome', **executable_path, headless=False)
    url = "https://marshemispheres.com/"

    # empty list for image paths to be stored in later
    hemisphere_image_urls = []

    # loop through hemisphere enhanced web pages 
    for i in range(0,4):
        browser.visit(url)
        browser.links.find_by_partial_text('Hemisphere Enhanced')[i].click()

        # use beautiful soup to grab desired image paths and titles
        soup = BeautifulSoup(browser.html, "html.parser")
        title = soup.find("h2", class_="title").text
        img = soup.find("img", class_="wide-image")['src']

        # append to list
        hemisphere_image_urls.append({
                        'title':title, 
                        'img_url':url + img
        })
    browser.quit()

    print(html_table)
    return export_dic = {
        'news_title':news_title,
        'news_p':news_p, 
        'mars_surface':featured_image_url,
        'html_file':"MarsVsEarth.html",
        'hemisphere_images':hemisphere_image_urls
    }
scrape()