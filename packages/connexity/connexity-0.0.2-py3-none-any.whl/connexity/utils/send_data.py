from connexity.CONST import CONNEXITY_URL

import aiohttp


async def send_data(answer_dict, api_key):

    async with aiohttp.ClientSession() as session:
        async with session.post(CONNEXITY_URL, headers={"X-API-KEY": api_key}, json=answer_dict) as response:
            if response.status != 200:
                print(f"Coonexity SDK: Failed to send data: {response.status}")
                print(response, flush=True)
            else:
                print(f"Coonexity SDK: Data sent successfully: {response.status}", flush=True)
