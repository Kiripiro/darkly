# SQL Injection Vulnerability in Searchimg Page

## Overview

A **SQL Injection** vulnerability was discovered on the `searchimg` page, allowing unauthorized access to data from the `list_images` table. This issue stems from insufficient input validation, exposing sensitive information and demonstrating how attackers can manipulate parameters to gain unintended access.

## Methodology

1. **Initial Testing**

   - After successfully dumping values from the Members page, similar techniques were applied to the `searchimg` page.
   - The `id` parameter was tested by appending SQL logic (e.g., `AND 1=1` or `AND 1=2`) to observe the server’s responses.
   - The server returned additional data that should not normally be exposed, confirming the possibility of SQL Injection.

2. **Crafting the Payload**

   - **Payload**:
     ```sql
     1 AND 1=2 UNION SELECT title, comment FROM list_images --
     ```
   - By manipulating the `id` parameter with the above UNION-based injection, columns such as `title` and `comment` were successfully retrieved from the `list_images` table.

3. **Validation of Results**

   - The server returned sensitive data, including a **special message** (the Flag), confirming that the injection was successful.

4. **Exploited URL**
   - **Payload** (URL-encoded):
     ```
     http://192.168.122.121/?page=searchimg&id=1+AND+1%3D2+UNION+SELECT+title%2C+comment+FROM+list_images+--&Submit=Submit#
     ```
   - **Parameter**: `id`
   - **Injection point**: `1+AND+1%3D2+UNION+SELECT+title%2C+comment+FROM+list_images+--`

## Flag

- **Original**: 1928e8083cf461a51303633093573c46
- **Converted Flag**: albatroz
- **To sha256**: f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188

---

## How to Prevent SQL Injections

1. **Parameterized Queries / Prepared Statements**

   - Use parameterized queries to automatically sanitize user inputs instead of manually constructing SQL strings.

2. **Input Validation**

   - Validate and sanitize user inputs to allow only expected data formats (e.g., numeric values for IDs).

3. **Use of an ORM (Object-Relational Mapping)**

   - Rely on established frameworks (e.g., Hibernate, Entity Framework, Django ORM) that handle SQL queries safely.

4. **Least Privilege Principle**

   - Restrict database user privileges to the bare minimum needed.

5. **Regular Updates and Patches**
   - Keep your frameworks, libraries, and database software up to date to benefit from the latest security fixes.
