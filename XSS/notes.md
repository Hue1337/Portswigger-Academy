# XSS - notes
- Author: [Mateusz Głuchowski](https://github.com/hue1337)
- Based on [PortSwigger Academy](https://portswigger.net)

## DOM-XSS
- What sinks can lead to `DOM-XSS` vulnerability:

    ```js
    document.write()
    document.writeln()
    document.domain
    element.innerHTML
    element.outerHTML
    element.insertAdjacentHTML
    element.onevent
    ```

- What `jQuery` functions can also lead to `DOM-XSS` vulnerablity:
    ```js
    add()
    after()
    append()
    animate()
    insertAfter()
    insertBefore()
    before()
    html()
    prepend()
    replaceAll()
    replaceWith()
    wrap()
    wrapInner()
    wrapAll()
    has()
    constructor()
    init()
    index()
    jQuery.parseHTML()
    $.parseHTML()
    ```


# ?
```
https://portswigger.net/users?returnurl=%2facademy%2flabs%2flaunch%2fb73aad4efa87dfe5458720e5a4713f2b416825e550dc9d161f58635db7a48dcd%3freferrer%3d%252fweb-security%252fcross-site-scripting%252fdom-based%252flab-jquery-selector-hash-change-event

https://portswigger.net/users?returnurl=
```
