# Automation Workflow

## Objective

Automatically extract invoice line-item data from an Odoo ERP environment and export it into a structured JSON format.

---

## Workflow Stages

### Stage 1 — Authentication

The automation launches a browser session and authenticates into the target Odoo instance.

Expected Result:

* User reaches authenticated dashboard.

---

### Stage 2 — Module Navigation

The framework navigates to the Invoicing application.

Expected Result:

* Invoice list becomes available.

---

### Stage 3 — Filter Processing

Default filters are removed and the Posted invoice filter is applied.

Expected Result:

* Only posted invoices remain visible.

---

### Stage 4 — Invoice Discovery

The framework searches available invoices and locates the target customer invoice.

Target Customer:

Deco Addict

Expected Result:

* Invoice detail page opens successfully.

---

### Stage 5 — Data Extraction

The automation accesses the Invoice Lines section and extracts:

* Product Name
* Quantity
* Unit Price
* Tax Amount

Expected Result:

* All visible invoice lines are captured.

---

### Stage 6 — Data Export

Extracted data is converted into JSON format and written to a local output file.

Expected Result:

output/invoice_lines.json

---

### Stage 7 — Cleanup

Temporary memory structures are cleared.

Expected Result:

* No residual invoice data remains in memory.

---

## Success Criteria

* Login succeeds
* Invoice located successfully
* Invoice lines extracted
* JSON generated
* No sensitive data exposed in logs
* Execution remains stable in headless mode
