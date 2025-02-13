# Copyright 2025 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models


class RepairOrder(models.Model):
    _inherit = "repair.order"

    def _get_complete_repairs_to_validate(self):
        return self.filtered(lambda a: a.state == "draft")

    def _get_complete_repairs_to_start(self):
        return self.filtered(
            lambda a: (
                a.state == "confirmed" and a.invoice_method in ["none", "after_repair"]
            )
            or (a.state == "ready" and a.invoice_method == "b4repair")
        )

    def _get_complete_repairs_to_finish(self):
        return self.filtered(
            lambda a: (
                a.state == "under_repair"
                and a.invoice_method in ["none", "after_repair"]
            )
            or (a.invoice_method == "b4repair" and a.state == "under_repair")
        )

    def _get_complete_repairs_to_invoice(self):
        return self.filtered(lambda a: a.state == "2binvoiced")

    def complete_repair_validate(self):
        draft_repair_orders = self._get_complete_repairs_to_validate()
        for repair in draft_repair_orders:
            repair.action_validate()

    def complete_repair_start(self):
        self._get_complete_repairs_to_start().action_repair_start()

    def complete_repair_end(self):
        repair_orders_to_finish = self._get_complete_repairs_to_finish()
        repair_orders_to_finish.action_repair_end()

    def complete_repair_invoice(self, group):
        repairs_to_invoice = self._get_complete_repairs_to_invoice()
        repairs_to_invoice._create_invoices(group)
        # It is necessary to call action_repair_invoice_create after creating
        # the invoice so the state of the repairs change. It is dones with the
        # invoicing wizard in the same way.
        repairs_to_invoice.action_repair_invoice_create()

    def complete(self, invoice=False, group=False):

        # 1. Validate repairs in draft state
        self.complete_repair_validate()

        # 2. Start confirmed repairs with no invoice method or invoice method after repair
        self.complete_repair_start()

        # 3. Complete repairs with no invoice method or invoice method after repair
        self.complete_repair_end()

        # 4. Invoice repairs to be invoiced
        if invoice:
            self.complete_repair_invoice(group)

        # 5. action_repair_start is called again so the repairs with invoice method
        # before repair that has just been invoiced can be started
        self.complete_repair_start()

        # 6. complete_repair_end is called again so the repairs with invoice method
        # before repair that has just been invoiced can be finished
        self.complete_repair_end()
