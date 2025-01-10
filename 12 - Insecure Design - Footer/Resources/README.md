# Bad Redirection Exploitation

## Overview

Bad redirection vulnerabilities occur when an application improperly handles user-controlled URLs during redirection, allowing attackers to redirect users to malicious sites.

## Methodology

1. **Initial Discovery**

   - The vulnerability was exploited by modifying the URL of a redirection. In this case, the footer contained a link to Facebook, which was manipulated to redirect users to an unintended destination.

2. **Exploit**
   - Find the HTML object for one of the social media icon in the footer.
   - Change the `site` variable inside the `href`.
   - Click on the modified icon on the page.

## Flag

- **Flag**: b9e775a0291fed784a2d9680fcfad7edd6b8cdf87648da647aaf4bba288bcab3

---

## How to Prevent Bad Redirection Vulnerabilities

1. **Validate Redirect URLs:**

   - Allow only pre-approved, trusted URLs for redirections.
   - Use a whitelist approach to ensure user-provided URLs match expected patterns.

2. **Avoid User-Controlled Input:**

   - Do not use user inputs directly in redirection logic.

3. **Implement Warning Pages:**

   - Display an intermediate warning page before completing the redirection, informing users about the target URL.

4. **Use URL Encoding:**
   - Properly encode URLs to prevent injection of malicious parameters.
