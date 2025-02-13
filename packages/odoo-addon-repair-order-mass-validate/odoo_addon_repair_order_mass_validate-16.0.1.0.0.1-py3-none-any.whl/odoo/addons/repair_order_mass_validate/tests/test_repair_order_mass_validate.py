# Copyright 2025 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo.addons.repair.tests.test_repair import TestRepair


class TestRepairOrderMassValidate(TestRepair):
    def setUp(self):
        super().setUp()
        self.wizard = (
            self.env["repair.order.mass.complete.wizard"]
            .with_context(
                active_ids=[
                    self.repair0.id,
                    self.repair1.id,
                    self.repair2.id,
                ]
            )
            .create({})
        )

    def test_respair_order_mass_validate_no_invoice(self):
        """
        repair0     Invoice Policy: After Repair
        repair1     Invoice Policy: None
        repair2     Invoice Policy: Before Repair
        """
        self.wizard.create_invoice = False
        self.wizard.group_invoice = False
        self.wizard.complete_repair_orders()
        self.assertEqual(self.repair0.state, "2binvoiced")
        self.assertEqual(self.repair1.state, "done")
        self.assertEqual(self.repair2.state, "2binvoiced")
        self.assertFalse(self.repair0.invoice_id)
        self.assertFalse(self.repair1.invoice_id)
        self.assertFalse(self.repair2.invoice_id)

    def test_respair_order_mass_validate_invoice_no_group(self):
        """
        repair0     Invoice Policy: After Repair
        repair1     Invoice Policy: None
        repair2     Invoice Policy: Before Repair
        """
        self.wizard.create_invoice = True
        self.wizard.group_invoice = False
        self.wizard.complete_repair_orders()
        self.assertEqual(self.repair0.state, "done")
        self.assertEqual(self.repair1.state, "done")
        self.assertEqual(self.repair2.state, "done")
        self.assertTrue(self.repair0.invoice_id)
        self.assertFalse(self.repair1.invoice_id)
        self.assertTrue(self.repair2.invoice_id)
        self.assertNotEqual(self.repair0.invoice_id, self.repair2.invoice_id)

    def test_respair_order_mass_validate_invoice_group(self):
        """
        repair0     Invoice Policy: After Repair
        repair1     Invoice Policy: None
        repair2     Invoice Policy: Before Repair
        """
        self.wizard.create_invoice = True
        self.wizard.group_invoice = True
        self.wizard.complete_repair_orders()
        self.assertEqual(self.repair0.state, "done")
        self.assertEqual(self.repair1.state, "done")
        self.assertEqual(self.repair2.state, "done")
        self.assertTrue(self.repair0.invoice_id)
        self.assertFalse(self.repair1.invoice_id)
        self.assertTrue(self.repair2.invoice_id)
        self.assertEqual(self.repair0.invoice_id, self.repair2.invoice_id)
