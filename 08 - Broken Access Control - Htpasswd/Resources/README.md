# Htpasswd Vulnerability

## Overview

A **Broken Access Control Vulnerability** was discovered, allowing attackers to bypass restrictions and gain unauthorized access to sensitive files and directories. This exploit demonstrates weak access control measures and poor configuration practices.

## Methodology

1. **Initial Discovery**

   - Ran a crawler Python script to find all the website's pages.
   - Accessed the `robots.txt` file at `http://192.168.122.121/robots.txt`.
   - Identified restricted paths listed in `robots.txt` that were not adequately protected.

2. **File Enumeration**

   - Navigated to one of the restricted paths (`/whatever/`) and retrieved a file named `htpasswd.txt`.
   - The file contained credentials, including a username (`root`) and a md5 encoded password (`437394baff5aa33daa618be47b75cb49`).

3. **Password Decoding**

   - Decoded the password using [dCode](https://www.dcode.fr/hash-md5).

4. **Login Attempt**

   - Attempted to sign in with the `root` credentials but found they did not provide access.

5. **Hidden Admin Page Discovery**

   - Using [GoBuster](https://github.com/OJ/gobuster) found on [OWASP](https://owasp.org/www-project-web-security-testing-guide/latest/6-Appendix/C-Fuzzing)

   - Used `gobuster` to enumerate hidden directories:

   ```bash
   gobuster dir -u http://192.168.122.121/ -w actions-lowercase.txt -k --exclude-length 975
   ```

   - Found a hidden admin page.

6. **Exploitation**
   - Accessed the hidden admin page using the credentials, successfully retrieving the flag.

## Flag

- **Flag**: d19b4823e0d5600ceed56d5e896ef328d7a2b9e7ac7e80f4fcdb9b10bcb3e7ff

---

## How to Prevent Access Control Vulnerabilities

1. **Restrict Sensitive File Access**

   - Avoid exposing sensitive files such as `robots.txt` or `htpasswd.txt` in publicly accessible directories.

2. **Enforce Strong Access Controls**

   - Implement robust access control mechanisms to restrict unauthorized access to sensitive paths and files.

3. **Use Secure Authentication Practices**

   - Store passwords securely using strong hashing algorithms and salts.
   - Periodically audit and rotate credentials.

4. **Disable Directory Indexing**

   - Prevent attackers from discovering sensitive files by disabling directory listing.

5. **Conduct Regular Security Audits**

   - Periodically audit server configurations and access control policies to ensure compliance with best practices.

6. **Penetration Testing**
   - Perform regular penetration testing to identify and patch potential access control weaknesses.
