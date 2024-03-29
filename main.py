import psutil
import time


def suspend_gtav_process() -> None:
    """
    Suspend and resume GTA V online and RED DEAD ONLINE process for solo lobby

    :return: None
    """
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        if proc.name().lower() in ["GTA5.exe".lower(), "RDR2.exe".lower()]:
            proc.suspend()
            print("Suspend 8 sec")
            time.sleep(8)
            proc.resume()
            print("Resume")
            break


if __name__ == '__main__':
    suspend_gtav_process()
