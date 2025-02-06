"""Contains all the data models used in inputs/outputs"""

from .odoo_order_confirm_request import OdooOrderConfirmRequest
from .odoo_sync_product_request import OdooSyncProductRequest

__all__ = (
    "OdooOrderConfirmRequest",
    "OdooSyncProductRequest",
)
