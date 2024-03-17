import argparse
import time
import subprocess
import platform

def keep_alive(url):
    amount = 0
    param = '-n' if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", url]
    while amount < 10000:
        amount += 1
        time.sleep(5)
        subprocess.call(command)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Keeping machine alive, no big deal - constant PIIING")
    parser.add_argument("--url", "-u", type=str, nargs=1, help="Provide the url to the spwned machine.")
    args = parser.parse_args()

    keep_alive(args.url[0])   