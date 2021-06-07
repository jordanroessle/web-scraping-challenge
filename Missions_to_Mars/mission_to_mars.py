import pandas as pd
from bs4 import BeautifulSoup
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager


# In[2]:


executable_path = {'executable_path': ChromeDriverManager().install()}


# In[3]:


browser = Browser('chrome', **executable_path, headless=False)
url = "https://redplanetscience.com/"

browser.visit(url)
soup = BeautifulSoup(browser.html, 'html.parser')
browser.quit()


# In[4]:


news_title = soup.find('div', class_ = 'content_title').text
news_title


# In[5]:


news_p = soup.find('div', class_ = 'article_teaser_body').text
news_p


# In[6]:


browser = Browser('chrome', **executable_path, headless=False)
url = "https://spaceimages-mars.com/"

browser.visit(url)
soup = BeautifulSoup(browser.html, "html.parser")
browser.quit()


# In[7]:


featured_image_url = soup.find("img", class_="headerimage fade-in")
featured_image_url = url + featured_image_url['src']
featured_image_url


# In[8]:


url = "https://galaxyfacts-mars.com/"
tables = pd.read_html(url)
df = tables[0]
df


# In[9]:


df = df.iloc[1:]
df.columns = ["Desciption", "Mars", "Earth"]
df.reset_index(drop=True, inplace=True)
df


# In[10]:


html_table = df.to_html("MarsVsEarth.html")


# In[11]:


browser = Browser('chrome', **executable_path, headless=False)
url = "https://marshemispheres.com/"


# In[12]:


hemisphere_image_urls = []


# In[13]:


for i in range(0,4):
    browser.visit(url)
    browser.links.find_by_partial_text('Hemisphere Enhanced')[i].click()
    soup = BeautifulSoup(browser.html, "html.parser")
    title = soup.find("h2", class_="title").text
    img = soup.find("img", class_="wide-image")['src']
    hemisphere_image_urls.append({
                    'title':title, 
                    'img_url':url + img
    })
browser.quit()    


# In[14]:


hemisphere_image_urls


# In[ ]:




