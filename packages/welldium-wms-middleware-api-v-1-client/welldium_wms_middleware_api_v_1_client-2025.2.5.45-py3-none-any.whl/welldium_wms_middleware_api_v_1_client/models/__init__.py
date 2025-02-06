"""Contains all the data models used in inputs/outputs"""

from .odoo_sync_product_request import OdooSyncProductRequest
from .request import Request
from .request_2 import Request2
from .selveo_sale_order_webhook_data_type_0 import SelveoSaleOrderWebhookDataType0
from .selveo_sale_shipment_webhook_data_type_0 import SelveoSaleShipmentWebhookDataType0
from .selveo_webhook_event_data_of_selveo_sale_order_webhook_data import (
    SelveoWebhookEventDataOfSelveoSaleOrderWebhookData,
)
from .selveo_webhook_event_data_of_selveo_sale_shipment_webhook_data import (
    SelveoWebhookEventDataOfSelveoSaleShipmentWebhookData,
)

__all__ = (
    "OdooSyncProductRequest",
    "Request",
    "Request2",
    "SelveoSaleOrderWebhookDataType0",
    "SelveoSaleShipmentWebhookDataType0",
    "SelveoWebhookEventDataOfSelveoSaleOrderWebhookData",
    "SelveoWebhookEventDataOfSelveoSaleShipmentWebhookData",
)
