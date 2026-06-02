# Playwright Enterprise Automation

Enterprise-grade browser automation framework built with Playwright and Python for ERP invoice extraction, dynamic UI navigation, resilient synchronization, secure data processing, and structured JSON export.

---

## Overview

This project demonstrates a production-oriented automation workflow for interacting with dynamically rendered ERP systems.

The framework automates invoice discovery and extraction from an Odoo ERP environment while emphasizing:

* Dynamic UI handling
* Event-driven synchronization
* Resilient locator strategies
* Fault-tolerant automation
* PHI-safe logging
* Secure data processing
* Structured JSON export

---

## Business Scenario

Organizations often require automated extraction of invoice information from ERP systems for:

* Reporting
* Data migration
* Financial processing
* Auditing
* System integrations

This framework simulates a real-world enterprise workflow by locating a target invoice, extracting invoice line items, and exporting the results into a structured JSON format.

---

## Features

* Playwright-based browser automation
* Persistent browser sessions
* Dynamic ERP navigation
* Posted invoice filtering
* Invoice discovery workflow
* Invoice line extraction
* JSON export
* Retry mechanisms
* Event-driven synchronization
* Headless execution support
* Secure logging practices
* Memory sanitization

---

## Automation Workflow

```text
Launch Browser
        │
        ▼
Authenticate
        │
        ▼
Open Invoicing Module
        │
        ▼
Apply Posted Filter
        │
        ▼
Locate Target Invoice
        │
        ▼
Open Invoice Details
        │
        ▼
Extract Invoice Lines
        │
        ▼
Generate JSON Output
        │
        ▼
Sanitize Memory
        │
        ▼
Close Browser
```

## Project Structure

```text
playwright-enterprise-automation/
│
├── assets/
│
├── core/
│   ├── browser.py
│   ├── navigation.py
│   └── synchronization.py
│
├── extractors/
│   └── invoice_extractor.py
│
├── security/
│   ├── logger.py
│   └── sanitizer.py
│
├── output/
│
├── .env.example
├── requirements.txt
├── main.py
└── README.md
```

## Expected Output

```json
[
  {
    "product_name": "Desk Combination",
    "quantity": 2,
    "unit_price": 1500.00,
    "tax_amount": 300.00
  }
]
```

## Security Considerations

* No invoice details exposed in logs
* No customer information written to console output
* Secure handling of extracted data
* Temporary data cleared after export
* Environment-based credential management

## Technology Stack

| Component     | Technology        |
| ------------- | ----------------- |
| Language      | Python            |
| Automation    | Playwright        |
| Browser       | Chromium          |
| Serialization | JSON              |
| Logging       | Python Logging    |
| Execution     | Headless Chromium |

## Future Enhancements

* Multi-invoice extraction
* Session persistence
* API-assisted extraction
* Cloud execution support
* CI/CD integration
* Multi-ERP compatibility

## License

This project is licensed under the MIT License.
