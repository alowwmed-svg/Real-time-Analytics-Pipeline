import asyncpg


class Database: 
    def __init__(self, dns: str): 
        self.dns = dns 
        self.pool = None 
    
    async def __aenter__(self):
        await self.connect()
        return self
    
    async def __aexit__(self, exc_type, exc, tb):
        await self.disconnect()

    async def connect(self): 
        if self.pool is None: 
            self.pool = await asyncpg.create_pool(
                self.dns,
                max_size=10
            )

    async def disconnect(self):
        if self.pool: 
            await self.pool.close()
            self.poll = None 