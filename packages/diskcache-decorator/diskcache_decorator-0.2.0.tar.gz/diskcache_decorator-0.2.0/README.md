# diskcache-decorator

```py
from diskcache_decorator import cached

@cached() 
async def my_async_function(a, b):
    await asyncio.sleep(2)  # Simulate some work
    return a + b

await my_async_function(1, 2) # Takes 2 seconds
await my_async_function(1, 2) # Returns immediately
```
