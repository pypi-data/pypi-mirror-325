# Copyright 2025 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Repair Order Mass Validate",
    "summary": "Repair Order Mass Validate",
    "version": "16.0.1.0.0",
    "license": "AGPL-3",
    "author": "Sygel,Odoo Community Association (OCA)",
    "website": "https://github.com/sygel-technology/sy-repair",
    "depends": [
        "repair",
    ],
    "data": [
        "security/ir.model.access.csv",
        "wizard/repair_order_mass_complete_wizard_views.xml",
    ],
}
