import aiohttp
import asyncio
import time

class DatasetService:
    current_offset: int = 0
    current_limit: int = 20000
    
    def __init__(self, api_url):
        print("""
            [!WARNING!] You are exectuing dataset retriever that uses API, 
            [!WARNING!] it has limitations and retrieving might take more than 1 hour
            [!WARNING!] Use ./bin/client instead, it fetches dataset from our team's server
            [!WARNING!] located in Europ.
        """)
        self.api_url = api_url

    def build_fetch_url(self) -> str:
        limit = "$limit=" + str(self.current_limit)
        offset = "$offset=" + str(self.current_offset)
        return self.api_url + "?" + limit + "&" + offset
    
    def pagination_next(self):
        self.current_offset += self.current_limit

    async def fetch(self, session: aiohttp.ClientSession, url: str) -> str:
        async with session.get(url) as response:
            return await response.text()

    def log(self, response: str):
        print(response)

    def log_iterations(self, response: str):
        print(f"Amount received: {self.current_offset}, chunk size: {self.current_limit}")
        
    def log_size(self, response: str):
        print(len(response))
        
    def continue_from(self, offset):
        self.current_offset = offset
    
    async def fetch_all_and_apply(self, processors, location):
        start = time.time()
        tasks = []
        responses = []

        async with aiohttp.ClientSession() as session:
            for i in range(0, 450):
                url = self.build_fetch_url()
                tasks.append(self.fetch(session, url))
                self.pagination_next()
                print(f"Sending promise: {i}")
                
                if (i % 100 == 0 and i != 0) or i == 449:
                    print(f"Start to await chunk {i} of promises")
                    _responses = await asyncio.gather(*tasks)
                    responses.extend(_responses)
                    tasks = []
                    print("Done waiting, sleep to wait for API limit..")
                    await asyncio.sleep(1)
        
        print("Writing dataset to file")
        start_write = time.time()
        with open(location, 'a+') as f:
            for response in responses:
                for callback in processors:
                    callback(response)
                f.write(response)
        end_write = time.time()
        print("Finished writing data in " + str(int(end_write - start_write)) + " ms.")
        
        end = time.time()
        print("Finished retrieving data in " + str(int(end - start)) + " s.")
