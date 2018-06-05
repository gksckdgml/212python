# PYTHONIOENCODING=UTF-8
# -*- coding: utf-8 -*-

import requests
import pandas as pd
import matplotlib

res = requests.get(
"https://api.zigbang.com/v1/items?detail=true&item_ids=11743282&item_ids=11731416&item_ids=11696401&item_ids=11743287&item_ids=11696991"
)

res.json()

df = pd.DataFrame([item.get("item") for item in res.json().get("items")])

print(df)

df.to_csv("zigbang.csv")
df.to_excel("zigbang.xlsx")

%matplotlib inline
df.deposit.hist()
df.rent.hist()
