from tmeapi import TmeApi
import os

api = TmeApi(os.environ["TME_KEY"].strip(), os.environ["TME_APP_SECRET"].strip())

print(api.autocomplete("555"))
print(api.get_prices(["EL-MAKR04120PA-TC"]))
print(api.get_prices_and_stock(["EL-MAKR04120PA-TC"]))

