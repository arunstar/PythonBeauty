import time


# async function or coroutines
async def get_server_status(url):
    time.sleep(3)
    return await "Done"

start = time.time()
get_server_status("google")
get_server_status("yahoo")
end = time.time()

print(end-start)