# Copyright 2025 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class RepairOrderMassCompleteWizard(models.TransientModel):
    _name = "repair.order.mass.complete.wizard"
    _description = "Repair Order Mass Complete Wizard"

    create_invoice = fields.Boolean()
    group_invoice = fields.Boolean()
    repair_order_ids = fields.Many2many(
        comodel_name="repair.order",
        readonly=True,
        default=lambda self: self.env.context.get("active_ids"),
    )

    def complete_repair_orders(self):
        self.ensure_one()
        self.repair_order_ids.complete(self.create_invoice, self.group_invoice)
