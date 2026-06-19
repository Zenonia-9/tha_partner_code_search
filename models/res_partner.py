from odoo import models


class ResPartner(models.Model):
    _inherit = "res.partner"

    _rec_names_search = [
        "complete_name",
        "email",
        "ref",
        "vat",
        "company_registry",
        "business_partner_code",
    ]
