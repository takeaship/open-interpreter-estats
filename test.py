import jpy_datareader.data as web
import os

api_key = os.environ.get("ESTATS_APP_ID")
df = web.DataReader("0003109558", "estat", api_key=api_key)
print(df)