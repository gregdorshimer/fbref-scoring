import pandas as pd

url = 'https://fbref.com/en/comps/Big5/shooting/players/Big-5-European-Leagues-Stats'

df_url = pd.read_html(url)

df_url[0].head()
