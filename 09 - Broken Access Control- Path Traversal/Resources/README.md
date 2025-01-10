# Path Traversal Vulnerability

## Overview

Path traversal is a web security vulnerability that allows an attacker to access directories and files stored outside the web root folder. By manipulating file paths, attackers can bypass access controls and potentially gain access to sensitive information or system files. This vulnerability often arises due to improper validation of user input.

## Methodology

1. **Initial Discovery**

   - The vulnerability was identified using techniques aligned with the OWASP Top 10 Broken Access Control, and focusing on "path traversal." Relevant documentation and testing guidelines were referenced from OWASP:

   - [OWASP Top 10 - Broken Access Control](https://owasp.org/Top10/A01_2021-Broken_Access_Control/)
   - [OWASP Testing Guide - Path Traversal](https://github.com/OWASP/wstg/blob/master/document/4-Web_Application_Security_Testing/05-Authorization_Testing/01-Testing_Directory_Traversal_File_Include.md)

2. **Vulnerability Exploitation**

   - The testing guide above sent us to this [Github](https://github.com/OWASP/wstg/blob/master/document/4-Web_Application_Security_Testing/05-Authorization_Testing/01-Testing_Directory_Traversal_File_Include.md) where we found the following tool.

   - To automate the testing, the tool `dotdotpwn` was employed. This command was executed:

   ```bash
   ./dotdotpwn.pl -m http -h 192.168.122.121/?page= -o "unix" -d 10
   ```

   - This tool generated potential exploit paths by leveraging common path traversal patterns. Each generated path was tested individually.

   - After testing multiple paths, a vulnerable endpoint was discovered:

   ```url
   http://192.168.122.121/?page=:80/../../../../../../../../../etc/passwd
   ```

   This endpoint allowed access to the `/etc/passwd` file, revealing sensitive system information. As a result, the following flag was retrieved:

## Flag

- **Flag**: b12c4b2cb8094750ae121a676269aa9e2872d07c06e429d25a63196ec1c8c1d0

---

## How to Prevent Path Traversal

1. **Input Validation:**

   - Rigorously filter and validate user inputs to block characters like `../`.
   - Use a whitelist approach to allow only predefined, safe paths.

2. **Filesystem Restrictions:**

   - Apply strict access controls to sensitive files.
   - Use chroot environments or containers to isolate the application from the rest of the system.

3. **Path Normalization:**
   - Convert user-supplied file paths into a standard format to prevent bypass techniques.
