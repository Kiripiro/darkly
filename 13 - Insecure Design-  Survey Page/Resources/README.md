# Permissive List of Allowed Inputs Vulnerability in a Survey Page

## Overview

A **Permissive List of Allowed Inputs** vulnerabilitywas found on the survey page that allows a user to choose a number between 1 and 10 using an input field. By modifying the value of this field directly through the browser’s element inspector, a user can send an incorrect value (greater than 10) to the server, which results in obtaining a flag.

## Methodology

1. **Access the Survey Page**

   - The page contains an input field where the user can select a number between 1 and 10.

2. **Modify the Value via the Element Inspector**

   - Open the browser's element inspector
   - Locate the `<input>` element where the value is defined (e.g., `value="5"`).
   - Modify this value in the inspector, for example, change `5` to `1000`.

3. **Submit the Form**
   After modifying the value, submit the form. The server will receive the falsified value and respond with a flag.

## Flag

- **Flag**: 03a944b434d5baff05f46c4bede5792551a2595574bcafc9a6e25f67c382ccaa

---

## How to prevent Permissive List of Allowed Inputs Vulnerability

1. **Server-side Validation**

   - Ensure that the server checks that the received value is within the allowed range (1 to 10).

2. **Client-side Validation**

   - Use JavaScript to verify that the value is between 1 and 10 before submitting the form.
   - Add HTML constraints like `min="1"` and `max="10"` on the input field to limit possible values.

3. **Hiding Sensitive Values**
   - If the input value is critical for server-side processing, consider not sending it directly from the client to the server, and handle it securely on the server side only.
