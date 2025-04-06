# WebEngage Automation Tool

## Overview

WebEngage Automation is an internal auditing tool designed for **Android applications**. It ensures that all data sent to WebEngage by customers adheres to the expected format. This is crucial for maintaining accuracy and consistency in event tracking and analytics.

## How It Works

- The tool captures **Android application logs** in real-time.
- It extracts logs related to event tracking and forwards them to a user-specified **endpoint**.
- Once the auditing session starts, logs are continuously sent until the auditor manually closes the session.
- These logs are later processed by the **internal WebEngage AI tools** to generate **data accuracy insights**.

## Installation

To install the package, run:

```sh
pip install webengage-automation-app
```

## Usage

Run the following command to start tracking logs:

```sh
track --webengage-android <YOUR_ENDPOINT_URL>
```

Replace `<YOUR_ENDPOINT_URL>` with the API endpoint where logs should be sent.

## Legal Notice

This tool is an **internal property** of **WebEngage** and is strictly for **auditing purposes**. It is owned by **Nipun Patel (Copyright)** and any misuse, unauthorized distribution, or external sharing will lead to **legal consequences**.

---

© WebEngage. All rights reserved.
