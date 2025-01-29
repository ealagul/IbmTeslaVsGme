#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install yfinance pandas beautifulsoup4 requests matplotlib')


# In[4]:


pip install --upgrade pip


# In[2]:


import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt


# In[3]:


# Download Tesla stock data
tesla = yf.Ticker("TSLA")
tesla_stock_data = tesla.history(period="max")

# Display the first few rows
print(tesla_stock_data.head())


# In[20]:


# Download Tesla stock data
tesla = yf.Ticker("TSLA")
tesla_stock_data = tesla.history(period="max")

# Reset index to make "Date" a column
tesla_stock_data.reset_index(inplace=True)

# Display the first few rows
print(tesla_stock_data.head())


# In[10]:


import requests

url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("Page retrieved successfully!")
    print(response.text[:1000])  # Print the first 1000 characters to check the content
else:
    print(f"Error: {response.status_code}")


# In[12]:


from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(response.text, "html.parser")

# Debugging: Check how many tables are found
tables = soup.find_all("table")
print(f"Found {len(tables)} tables.")

# If tables are found, proceed with extracting the data
if tables:
    tesla_revenue = pd.read_html(str(tables[0]))[0]  # Convert first table to DataFrame
    print(tesla_revenue.head())
else:
    print("No tables found. The page may use JavaScript to load data.")


# In[13]:


# Download GameStop stock data
gamestop = yf.Ticker("GME")
gamestop_stock_data = gamestop.history(period="max")

# Display the first few rows
print(gamestop_stock_data.head())


# In[21]:


# Download GameStop stock data
gamestop = yf.Ticker("GME")
gamestop_stock_data = gamestop.history(period="max")

# Reset index to make "Date" a column
gamestop_stock_data.reset_index(inplace=True)

# Display the first few rows
print(gamestop_stock_data.head())


# In[16]:


from bs4 import BeautifulSoup
import requests
import pandas as pd

# Define the URL for GameStop's revenue data
url = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"

# Adding headers to prevent request blocking
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

# Send request
response = requests.get(url, headers=headers)

# Check if request was successful
if response.status_code == 200:
    print("Page retrieved successfully!")
else:
    print(f"Error: {response.status_code}")
    exit()

# Parse HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Debugging: Check how many tables are found
tables = soup.find_all("table")
print(f"Found {len(tables)} tables.")

# If tables are found, proceed with extracting the data
if tables:
    gamestop_revenue = pd.read_html(str(tables[0]))[0]  # Convert first table to DataFrame
    print(gamestop_revenue.head())
else:
    print("No tables found. The page may use JavaScript to load data.")


# In[17]:


import matplotlib.pyplot as plt

def make_graph(stock_data, title):
    """
    Function to plot stock price trends.
    
    Parameters:
    stock_data (DataFrame): Stock data containing Date and Close price.
    title (str): Title for the graph.
    """
    plt.figure(figsize=(10, 5))
    plt.plot(stock_data["Date"], stock_data["Close"], label="Closing Price", color="blue", linewidth=2)
    plt.xlabel("Date")
    plt.ylabel("Stock Price (USD)")
    plt.title(title)
    plt.legend()
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()


# In[23]:


# Ensure Date is in proper format
gamestop_stock_data["Date"] = pd.to_datetime(gamestop_stock_data["Date"])

# Sort data by Date
gamestop_stock_data = gamestop_stock_data.sort_values("Date")

# Call function
make_graph(gamestop_stock_data, "GameStop Stock Price Over Time")


# In[22]:


# Ensure 'Date' is present before proceeding
if "Date" in tesla_stock_data.columns:
    tesla_stock_data["Date"] = pd.to_datetime(tesla_stock_data["Date"])
    tesla_stock_data = tesla_stock_data.sort_values("Date")

    # Plot the graph
    make_graph(tesla_stock_data, "Tesla Stock Price Over Time")
else:
    print("Error: 'Date' column not found in tesla_stock_data.")


# In[ ]:




