# Hardcoded Email Vulnerability in Reset Password Page

## Overview

A **Security Misconfiguration** vulnerability was discovered on the `Reset Password` page, allowing attackers to bypass authentication mechanisms and retrieve sensitive information (the flag). This issue arises from improperly hardcoded values in the client-side HTML code, exposing sensitive implementation details.

## Methodology

1. **Initial Testing**

   - While testing the reset password functionality, different email inputs were submitted, but none successfully triggered a reset flow.
   - Inspection of the page source using browser developer tools revealed that the email field's value was hardcoded in the HTML.

2. **Crafting the Exploit**

   - By replacing the hardcoded email value with another email address within the HTML code, the server accepted the manipulated input.
   - The response included sensitive information: a flag indicating the vulnerability's successful exploitation.

3. **Reproduction Steps**

   - Open the reset password page in a browser.
   - Inspect the HTML using developer tools (e.g., right-click > Inspect).
   - Locate the hardcoded email value in the HTML.
   - Replace the email value with a different email address.
   - Submit the form.
   - Observe the server's response containing the flag.

## Flag

- **Flag**: 1d4855f7337c0c14b6f44946872c4eb33853f40b2d54393fbe94f49f1e19bbb0

---

## How to Prevent Data Recovery Exploit

1. **Secure Input Handling**

   - Validate and sanitize all inputs both on the client and server sides to prevent unauthorized manipulation.

2. **Server-Side Access Control**

   - Ensure that sensitive operations (e.g., password resets) are fully validated on the server side, independent of client-side data.

3. **Dynamic Value Management**

   - Use dynamic methods to populate sensitive fields instead of embedding static values in client-side code.

4. **Remove Unused Code**

   - Eliminate hardcoded values and dead code from production builds to minimize attack surfaces.

5. **Audit and Test Regularly**

   - Conduct regular security audits and penetration testing to identify and address potential vulnerabilities.
