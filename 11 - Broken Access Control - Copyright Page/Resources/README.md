# Spoofing Exploitation

## Overview

Spoofing involves impersonating a trusted entity to deceive a target system. In this case, the attack was conducted by spoofing the referer header and user agent string to bypass restrictions.

## Methodology

1. **Initial Discovery**

   - The attack was carried out using the `curl` command with the following options:
     - `-e`: Spoofed the referer header to appear as `https://www.nsa.gov/`.
     - `-A`: Replaced the user agent string to impersonate `ft_bornToSec` instead of a standard browser like Firefox.

2. **Vulnerability Exploitation**

   ```bash
   curl -e "https://www.nsa.gov/" -A "ft_bornToSec" http://192.168.122.121/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f
   ```

   - This successfully bypassed the web server's checks, revealing the flag.

## Flag

- **Flag**: f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188

---

## How to Prevent Spoofing Attacks

1. **Header Validation:**

   - Validate headers like `Referer` and `User-Agent` on the server side, ensuring they match expected patterns.
   - Avoid relying solely on these headers for authentication or access control.

2. **Use Secure Authentication:**

   - Implement robust authentication mechanisms (e.g., OAuth, API keys) instead of relying on easily spoofed headers.

3. **Rate Limiting:**

   - Apply rate limiting and monitoring to detect suspicious or repetitive requests.

4. **SSL/TLS Encryption:**
   - Enforce HTTPS to protect data in transit and prevent man-in-the-middle attacks.
