import multiprocessing
import requests

def download_file(url,name):
    print(f"Started Downloading {name}")
    response = requests.get(url)
    with open(f"images/img{name}.jpg","wb") as file:
        file.write(response.content)
    print(f"Finished Downloading {name}")



url = "https://picsum.photos/3000/3000"

processes = []

for i in range(20):
    process = multiprocessing.Process(target=download_file,args=[url,i])
    processes.append(process)
    process.start()


for process in processes:
    process.join()
    
print("All Download Completed!")


