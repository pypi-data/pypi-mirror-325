from .core import ZeusCore, BASE_URL


class ZeusCourseType(ZeusCore):
    async def get_course_type(self, protect=False) -> dict:
        url = f"{BASE_URL}/coursetype"
        return await self.fetch_data(url, protect)

    async def get_course_type_by_id(self, id: int, protect=False) -> dict:
        url = f"{BASE_URL}/coursetype/{id}"
        return await self.fetch_data(url, protect)

    async def get_course_type_used_by(self, id: int, protect=False) -> dict:
        url = f"{BASE_URL}/coursetype/usedby/{id}"
        return await self.fetch_data(url, protect)
