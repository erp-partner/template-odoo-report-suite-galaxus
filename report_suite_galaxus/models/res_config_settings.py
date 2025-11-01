from odoo import api, fields, models

class ResConfigSettings(models.TransientModel):
    """Settings toggles for the generic report suite (template)."""
    _inherit = "res.config.settings"

    # -------------------------------------------------------------------------
    # Fields
    # -------------------------------------------------------------------------
    report_suite_use_sale_report = fields.Boolean(
        string="Use custom Sale Reports",
        config_parameter="report_suite_galaxus.use_sale_report",
        help="Use the custom Sale Order report templates instead of the default ones.",
    )

    report_suite_use_purchase_reports = fields.Boolean(
        string="Use custom Purchase Reports",
        config_parameter="report_suite_galaxus.use_purchase_reports",
        help="Use the custom Purchase report templates instead of the default ones.",
    )

    report_suite_use_delivery_reports = fields.Boolean(
        string="Use custom Delivery Reports",
        config_parameter="report_suite_galaxus.use_delivery_reports",
        help="Use the custom Delivery report templates instead of the default ones.",
    )

    report_suite_use_invoice_reports = fields.Boolean(
        string="Use custom Invoice Reports",
        config_parameter="report_suite_galaxus.use_invoice_reports",
        help="Use the custom Invoice report templates instead of the default ones.",
    )

    report_suite_paperformat_id = fields.Many2one(
        comodel_name="report.paperformat",
        string="Paper Format",
        related="company_id.paperformat_id",
        readonly=False,
        help="Paper format to apply to the report templates for this company.",
    )