import psutil
import time

for proc in psutil.process_iter(attrs=['pid','name']):
    if proc.name().lower() == "GTA5.exe".lower():
        proc.suspend()
        print("Suspend 8 sec")
        time.sleep(8)
        proc.resume()
        print("Resume")




