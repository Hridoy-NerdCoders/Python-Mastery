# import asyncio
# import aiohttp
# import os

# async def download_image(url, path):
#     print(f'Started Download for {path}')
    
#     # Ensure directory already exists:
#     os.makedirs(os.path.dirname(path), exist_ok=True)
    
#     # Download and save:
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             if response.status == 200:
#                 with open(path, 'wb') as file:
#                     file.write(await response.read())
#                 print(f'Successfully Downloaded {path}')
#             else:
#                 print(f'Failed to download {path}. Status code: {response.status}')

# async def download_python_img():
#     url = "https://shorturl.at/EFk1B"
#     filename = 'python.png'
#     path = f"download_imgs/{filename}"
#     await download_image(url, path)

# async def download_rajshahi_light_img():
#     url = "https://shorturl.at/DdfYe"
#     filename = 'raj_light.png'
#     path = f"download_imgs/{filename}"
#     await download_image(url, path)

# async def main():
#     await asyncio.gather(
#         download_python_img(),
#         download_rajshahi_light_img()
#     )

# asyncio.run(main())