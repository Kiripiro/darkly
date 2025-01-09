# Recursive Crawling in .hidden

## Overview

This project demonstrates a method for recursively crawling a website to locate hidden `.hidden` directories and extract flag information from `README` files. Using the ZAP crawling tool initially to identify hidden paths, we then created a Python script to crawl each folder and read the contents of every `README` file to find flags.

## Methodology

1. **Initial Step** 

    - Find `.hidden` directories using ZAP Crawling Tool
    We start by using the ZAP (Zed Attack Proxy) crawling tool to identify `.hidden` directories on the website. ZAP helps in discovering hidden paths that are not directly accessible via normal browsing.

2. **Recursively Crawl Folders with Python**

    - Once the `.hidden` directory is located, we use a Python script to crawl the directory recursively. The script identifies all subdirectories and searches for `README` files in each folder. It collects their contents and checks them for flags.

3. **Flag Extraction**

    - The `README` files often contain flags that are essential for completing challenges or capturing sensitive information. The script reads the content of each `README` file found and stores them in a file.

## Flag

- **Flag**: d5eec3ec36cf80dce44a896f961c1831a05526ec215693c8f2c39543497d4466

### How to Prevent Crawling
1. **Authentication and access control**
    - Add authentication to protect sensitive directories.

2. **Disable directory indexing**
    - Apply strict access to prevent discovery of hidden directories.

3. **Secure file handling**
    - File restrictions and avoid storing sensitive data in publicly accessible locations.
