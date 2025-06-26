# TME.eu API Client

```py
from tmeapi import TmeApi
import os

api = TmeApi(os.environ["TME_KEY"].strip(), os.environ["TME_APP_SECRET"].strip())

print(api.autocomplete("555"))
print(api.get_prices(["EL-MAKR04120PA-TC"]))
print(api.get_prices_and_stock(["EL-MAKR04120PA-TC"]))
```

NOTE: currently a limited api/typing surface, if you encounter any errors please submit an issue

[project.urls]
Homepage = "https://github.com/i404788/tme-api"
Repository = "https://github.com/i404788/tme-api"
