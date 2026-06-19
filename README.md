# Partner Code Search

![Odoo 19](https://img.shields.io/badge/Odoo-19.0-875A7B?style=flat-square)
![License](https://img.shields.io/badge/License-LGPL--3-blue?style=flat-square)
![Category](https://img.shields.io/badge/Category-Accounting-4ECDC4?style=flat-square)

Make `res.partner.business_partner_code` searchable in the standard accounting report partner selector in Odoo 19.

This lightweight addon extends the native `res.partner` relational search fields used by the standard partner selector. It is intended for report filters such as **Aged Payable**, **Aged Receivable**, **Partner Ledger**, and **General Ledger**, where Odoo uses `res.partner.name_search()` behind the selector.

## Highlights

- Keeps the native report filter flow unchanged.
- Extends `res.partner._rec_names_search` without modifying Odoo core.
- Adds `business_partner_code` to the existing standard search fields.
- Preserves standard partner display names and selection labels.
- Keeps existing searches by complete name, email, internal reference, VAT, and company registry.

## Search Fields

The addon keeps these standard search fields:

- `complete_name`
- `email`
- `ref`
- `vat`
- `company_registry`

It adds:

- `business_partner_code`

## What It Changes

- `models/res_partner.py`
  Inherits `res.partner` and extends `_rec_names_search`.

No report handler, JavaScript, display-name logic, or `name_get` override is added.

## Technical Notes

- The accounting report partner filter uses the standard relational selector path and calls `res.partner.name_search()`.
- This addon is intentionally minimal and upgrade-safe.
- The module assumes the field `business_partner_code` already exists on `res.partner` from another installed customization.

## Module Layout

```text
tha_partner_code_search/
|-- models/
|   |-- __init__.py
|   `-- res_partner.py
|-- README.md
|-- __init__.py
`-- __manifest__.py
```

## Dependencies

- `base`
- `account_reports`

## Installation

1. Place the module in your custom addons path.
2. Update the Apps list in Odoo.
3. Install **Partner Code Search**.

Example command:

```bash
docker exec odoo_19 odoo -c /etc/odoo/odoo.conf -d YOUR_DB_NAME -i tha_partner_code_search --stop-after-init
docker restart odoo_19
```

## Validation

Validated in this workspace by:

- Python syntax compilation
- Module installation
- Odoo container restart
- Live `res.partner.name_search()` check confirming business partner code lookup works for existing codes

## License

This module is licensed under `LGPL-3`.
