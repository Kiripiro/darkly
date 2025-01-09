# Cookie Poisoning Vulnerability

## Overview

A **Cookie Poisoning Vulnerability** was discovered, allowing attackers to manipulate cookie values and gain unauthorized privileges. This exploit demonstrates insufficient validation and protection of cookie data, exposing the application to privilege escalation.

## Methodology

1. **Initial Analysis**

   - Inspected HTTP requests and browser storage for sensitive cookies.
   - Identified a cookie named `I_am_admin` with a hashed value, which was not set as `HttpOnly=true`, meaning that we could change its value.

2. **Hash Analysis**

   - Extracted the value of the `I_am_admin` cookie.
   - Used the [dCode](https://www.dcode.fr/hash-md5) tool to analyze the hash and discovered it was an MD5 hash.
   - Determined that the hash represented a `false` value.

3. **Cookie Manipulation**

   - Modified the cookie value by replacing the hash for `false` with the hash for `true`.
   - Used the browser's developer console to execute:
     ```javascript
     document.cookie = "I_am_admin=b326b5062b2f0e69046810717534cb09";
     ```

4. **Privilege Escalation**
   - Reloaded the page, and the server recognized the modified cookie value, granting administrative privileges.
   - Retrieved the flag as a result of the successful privilege escalation.

## Flag

- **Flag**: df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3

---

## How to Prevent Security Misconfiguration Vulnerabilities

To secure applications against cookie poisoning vulnerabilities, implement the following measures:

1. **Use Secure Cookies**

   - Mark cookies with the `HttpOnly` and `Secure` flags to prevent client-side access and transmission over insecure channels.

2. **Strong Cookie Encryption**

   - Encrypt cookie values to prevent tampering. Ensure encryption keys are securely managed.

3. **Validate Cookie Data**

   - Implement server-side validation to verify the integrity and authenticity of cookie values.

4. **Avoid Sensitive Information in Cookies**

   - Do not store sensitive or security-related data directly in cookies.

5. **Implement Token-Based Authentication**

   - Use session tokens instead of cookies for critical operations requiring elevated privileges.

6. **Monitor and Log Cookie Usage**

   - Log and monitor unusual or suspicious cookie-related activities to detect potential attacks.

7. **Regularly Rotate Keys**
   - Periodically update and rotate keys used for cookie signing or encryption.

By following these best practices, developers can mitigate the risk of cookie poisoning attacks and ensure a secure application design.
