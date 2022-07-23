from query import run_query
from notification import Notification

result = run_query()
title = result["data"]["storefrontProductsById"][0]["title"]
status = result["data"]["storefrontProductsById"][0]["variants"][0]["status"]

if status != "SoldOut":
    Notification().notify("{} - EN STOCK".format(title))
