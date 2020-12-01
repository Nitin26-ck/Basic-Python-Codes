import pandas as pd
import wikipedia as wp
html=wp.page("list of world no 1 badminton players").html().encode("UTF-8")
df=pd.read_html(html)[0]
df.to_csv('beautifulsoup_pandas.csv',header=0,index=False)
print(df)