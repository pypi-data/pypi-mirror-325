from .core import ZeusCore, BASE_URL


class ZeusCourse(ZeusCore):
    async def get_course(self, protect=False) -> dict:
        url = f"{BASE_URL}/course"
        return await self.fetch_data(url, protect)

    async def get_course_by_id(self, id: int, protect=False) -> dict:
        url = f"{BASE_URL}/Course/{id}"
        return await self.fetch_data(url, protect)

    async def get_course_used_by(self, id: int, protect=False) -> dict:
        url = f"{BASE_URL}/course/{id}/usedby"
        return await self.fetch_data(url, protect)

    async def get_course_by_teacher(self, id: int, protect=False) -> dict:
        url = f"{BASE_URL}/Course/teacher/{id}"
        return await self.fetch_data(url, protect)
