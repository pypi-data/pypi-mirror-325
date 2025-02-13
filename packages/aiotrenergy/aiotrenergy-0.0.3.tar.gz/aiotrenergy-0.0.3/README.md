# Aiotrenergy
Asyncio library for interacting with the [Trenergy](https://tr.energy/) API.


## Installation
`pip install aiotrenergy`


## Usage
```python
from aiotrenergy import TrenergyClient
from aiotrenergy.enums import ConsumptionType


client = TrenergyClient("your_api_key", "https://nile-core.tr.energy/api/consumers")  # default url is https://core.tr.energy/api/

# Show account information
account = await client.account.show()
print(account)

# Transit wallets usage (https://tr.energy/ru/consumers/faq//#faq10)
consumer_create_response = await client.consumers.create(
    15,
    "TY3dRk4eQ75dCrW7tUcCzggU9rnz4V111",
    False,
    ConsumptionType.STATIC,
    200000,
    "test"
)
await client.consumers.activate(consumer_create_response.data.id)
```

## To do
### Fixes
client.consumers.toggle_auto_renewal returns 422 with no error message... (on params -> True, [54])
### Tests
### Docs
