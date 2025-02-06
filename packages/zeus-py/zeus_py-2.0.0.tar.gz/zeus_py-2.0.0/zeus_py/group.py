from .core import ZeusCore, BASE_URL


class ZeusCourse(ZeusCore):
    async def getègroup(self, protect=False) -> dict:
        url = f"{BASE_URL}/group"
        return await self.fetch_data(url, protect)

    async def get_group_by_id(self, id: int, protect=False) -> dict:
        url = f"{BASE_URL}/group/{id}"
        return await self.fetch_data(url, protect)

    async def get_group_ics(self, id: int, protect=False) -> dict:
        url = f"{BASE_URL}/group/{id}/ics"
        return await self.fetch_data(url, protect)
