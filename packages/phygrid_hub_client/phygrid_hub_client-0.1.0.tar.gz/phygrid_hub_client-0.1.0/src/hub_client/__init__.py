import asyncio
from hub_client import connect_phy_client

async def main():
    # Simple usage
    client = await connect_phy_client("my-module")
    
    # Or with explicit data residency
    client = await connect_phy_client("my-module", "US")

if __name__ == "__main__":
    asyncio.run(main())