# XSS Exploitation via HTML Object Tag

## Overview

Cross-Site Scripting (XSS) allows attackers to inject malicious scripts into web pages viewed by other users. In this case, the vulnerability was exploited through an HTML object tag.

## Methodology

1. **Initial Discovery**

    - After analyzing the website endpoints, a media URL was identified:

    ```url
    http://192.168.122.121/?page=media&src=nsa
    ```

    - Testing the parameter with a value like `test` revealed an object HTML tag in use:

    ```url
    http://192.168.122.121/?page=media&src=test
    ```
2. **Vulnerability Exploitation**

    - An XSS attack was successfully injected using a base64-encoded payload directly in the URL:

    ```url
    http://192.168.122.121/?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgiU3VjY2VzcyIpOzwvc2NyaXB0Pg==
    ```

    - This worked because the object tag's `src` attribute processed the payload without proper validation. The malicious script executed successfully, triggering an alert.

### Flag

- **Flag**: 928d819fc19405ae09921a2b71227bd9aba106f9d2d37ac412e9e5a750f1506d

---

## How to Prevent XSS

1. **Input Validation and Sanitization:**
   - Rigorously validate and sanitize all user inputs, especially those used in HTML attributes.
   - Reject or escape dangerous characters such as `<`, `>`, and `"`.

2. **Content Security Policy (CSP):**
   - Implement a strict CSP to control which scripts can be executed on the page.
   - Block inline scripts and only allow trusted sources.

3. **Use of Encoding:**
   - Encode user inputs before inserting them into HTML attributes.
   - For URLs, ensure the parameters are URL-encoded properly.

4. **Avoid Dynamic Code Injection:**
   - Do not dynamically include untrusted data directly into HTML or JavaScript.
