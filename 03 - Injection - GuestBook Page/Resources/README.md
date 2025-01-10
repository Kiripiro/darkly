# XSS Vulnerability in the GuestBook Page

## Overview

An **Injection** vulnerability was discovered on the `GuestBook` page, allowing attackers to inject malicious scripts into web pages viewed by other users. In this case, the vulnerability was exploited through an TextInput field.

## Methodology

1. **Initial Testing**

   - While testing the comment form, we've tried to inject malicious code in the `Name` field, as well as in the `Message` field.

2. **Payloads**
   - Classic JS
     ```javascript
     <script>alert("Test");</script>
     ```
     ```javascript
     <script>alert("Success");</script>
     ```
   - Base64 encoded
     ```javascript
     PHNjcmlwdD5hbGVydCgiVGVzdCIpOzwvc2NyaXB0Pg==
     ```
   - Escaped special characters
     ```javascript
     &lt;script&gt;alert(&#039;XSS&#039;)&lt;/script&gt;
     ```
     Many others...

To conclude, none of them worked, so we seeked help and found out that the solution was just to type a random `Name` and type `script` in the `Message` field.

## Flag

- **Flag**: 1d4855f7337c0c14b6f44946872c4eb33853f40b2d54393fbe94f49f1e19bbb0

---

## How to Prevent XSS Exploit

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
