# Path: invoke\api\api.py
from typing import Optional, List, Tuple, Any, Callable
from enum import Enum
import urllib.parse
import aiohttp
import json
import imghdr


QueryParams = List[Tuple[str, Optional[Any]]]

class ResponseType(Enum):
    JSON = "json",
    TEXT = "text",
    RAW = "raw"
    RESPONSE = "response"


class Api:
    host: str

    def __init__(self, client: aiohttp.ClientSession, host: str):
        self.host = host
        self.client = client


    async def get_async(self, api_path: str, version: int, prams: Optional[QueryParams] = None, type: ResponseType = ResponseType.JSON) -> Any:
        url = self.query_string(api_path, version, prams)
        async with self.client.get(url) as response:
            return await self.from_response_async(response, type)


    async def delete_async(self, api_path: str, version: int, prams: Optional[QueryParams] = None, type: ResponseType = ResponseType.JSON) -> Any:
        url = self.query_string(api_path, version, prams)
        async with self.client.delete(url) as response:
            return await self.from_response_async(response, type)


    async def upload_async(self, api_path: str, version: int, name: str, file_bytes: bytes, prams: Optional[QueryParams] = None, type: ResponseType = ResponseType.JSON) -> Any:
        url = self.query_string(api_path, version, prams)
        data = aiohttp.FormData()
        image_type = imghdr.what(None, h=file_bytes)
        content_type = f"image/{image_type}" if image_type else "application/octet-stream"
        data.add_field(name, file_bytes, filename=name, content_type=content_type)
        async with self.client.post(url, data=data) as response:
            return await self.from_response_async(response, type)


    async def post_async(self, api_path: str, version: int, data: Optional[Any] = None, prams: Optional[QueryParams] = None, type: ResponseType = ResponseType.JSON) -> Any:
        url = self.query_string(api_path, version, prams)
        async with self.client.post(url, json=self.prepare_data(data)) as response:
            return await self.from_response_async(response, type)


    async def put_async(self, api_path: str, version: int, data: Optional[Any] = None, prams: Optional[QueryParams] = None, type: ResponseType = ResponseType.JSON) -> Any:
        url = self.query_string(api_path, version, prams)
        async with self.client.put(url, json=self.prepare_data(data)) as response:
            return await self.from_response_async(response, type)


    async def patch_async(self, api_path: str, version: int, data: Optional[Any] = None, prams: Optional[QueryParams] = None, type: ResponseType = ResponseType.JSON) -> Any:
        url = self.query_string(api_path, version, prams)
        async with self.client.patch(url, json=self.prepare_data(data)) as response:
            return await self.from_response_async(response, type)


    def query_string(self, api_path: str, version: int, prams: Optional[QueryParams] = None) -> str:
        base_url = f"{self.host}/api/v{version}/{api_path}"
        if not prams:
            return base_url
        query_string = "&".join(f"{urllib.parse.quote(key)}={urllib.parse.quote(str(value))}" for key, value in prams if value is not None)
        return f"{base_url}?{query_string}"


    def prepare_data(self, data: Optional[Any]) -> Optional[Any]:
        if data is None:
            return {}
        if isinstance(data, str):
            return json.loads(data) 
        if isinstance(data, dict):
            return data
        try:
            return json.loads(json.dumps(data, default=lambda o: o.__dict__))
        except TypeError as e:
            raise ValueError(f"Cannot serialize data: {data}. Error: {e}")
        

    async def from_response_async(self, response: aiohttp.ClientResponse, type: ResponseType) -> Any:
        if type == ResponseType.RESPONSE:       
            return response
        
        if response.status >= 400:
            info = await response.text()
            raise Exception(f"Server status: {response.status}; Info: {info}")

        if type == ResponseType.JSON:
            try:
                return await response.json(content_type=None)
            except aiohttp.ContentTypeError:
                return {}
        if type == ResponseType.TEXT:   
            return await response.text()   
        if type == ResponseType.RAW:
            return await response.read()
        

    def add_params(self, prams: QueryParams, items: Optional[List[Any]], param_name: str, converter: Optional[Callable[[Any], str]] = None) -> None:
        if items is not None:
            for item in items:
                prams.append((param_name, converter(item) if converter else str(item)))