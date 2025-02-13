To use this module you need to:

#. Go to repair orders tree view.
#. Select multiple repair orders.
#. Go to *Action > Complete repair orders* to open a wizard.
#. Do not select the "Create Invoice" option if no invoice has to be created. In that case:
    
    * Repair orders without an Invoice Policy will be sent to "Repaired" state.
    * Repair orders with "Before Repair" Invoice Policy will be sent to "To Be Invoiced" state.
    * Repair orders with "After Repair" Invoice Policy will be sent to "To Be Invoiced" state.
#. Select the "Create Invoice" option if invoice have to be created. All the repair orders will be sent to "Repaired" states and invoices will be created.
#. Select the "Group Invoice" option along with "Create Invoice" option in order to group invoices created from repair orders when possible.
