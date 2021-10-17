import time
from plyer import notification


if __name__ == "__main__":
    while True:
        notification.notify(title = "Alert!", message = "Hello, there!, this is my first notification.", timeout = 10)

        time.sleep(30)