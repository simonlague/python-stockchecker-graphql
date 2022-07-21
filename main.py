from query import run_query
from pushover import initialize, notify

result = run_query()
title = result["data"]["storefrontProductsById"][0]["title"]
status = result["data"]["storefrontProductsById"][0]["variants"][0]["status"]

if status == "SoldOut":
    utilisateur = initialize()
    notify(utilisateur, "{} - EN STOCK".format(title))
