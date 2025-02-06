from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.selveo_sale_shipment_webhook_data_type_0 import SelveoSaleShipmentWebhookDataType0


T = TypeVar("T", bound="SelveoWebhookEventDataOfSelveoSaleShipmentWebhookData")


@_attrs_define
class SelveoWebhookEventDataOfSelveoSaleShipmentWebhookData:
    """
    Attributes:
        updated (Union['SelveoSaleShipmentWebhookDataType0', None, Unset]):
        before (Union['SelveoSaleShipmentWebhookDataType0', None, Unset]):
    """

    updated: Union["SelveoSaleShipmentWebhookDataType0", None, Unset] = UNSET
    before: Union["SelveoSaleShipmentWebhookDataType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.selveo_sale_shipment_webhook_data_type_0 import SelveoSaleShipmentWebhookDataType0

        updated: Union[None, Unset, dict[str, Any]]
        if isinstance(self.updated, Unset):
            updated = UNSET
        elif isinstance(self.updated, SelveoSaleShipmentWebhookDataType0):
            updated = self.updated.to_dict()
        else:
            updated = self.updated

        before: Union[None, Unset, dict[str, Any]]
        if isinstance(self.before, Unset):
            before = UNSET
        elif isinstance(self.before, SelveoSaleShipmentWebhookDataType0):
            before = self.before.to_dict()
        else:
            before = self.before

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if updated is not UNSET:
            field_dict["updated"] = updated
        if before is not UNSET:
            field_dict["before"] = before

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.selveo_sale_shipment_webhook_data_type_0 import SelveoSaleShipmentWebhookDataType0

        d = src_dict.copy()

        def _parse_updated(data: object) -> Union["SelveoSaleShipmentWebhookDataType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_selveo_sale_shipment_webhook_data_type_0 = (
                    SelveoSaleShipmentWebhookDataType0.from_dict(data)
                )

                return componentsschemas_selveo_sale_shipment_webhook_data_type_0
            except:  # noqa: E722
                pass
            return cast(Union["SelveoSaleShipmentWebhookDataType0", None, Unset], data)

        updated = _parse_updated(d.pop("updated", UNSET))

        def _parse_before(data: object) -> Union["SelveoSaleShipmentWebhookDataType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_selveo_sale_shipment_webhook_data_type_0 = (
                    SelveoSaleShipmentWebhookDataType0.from_dict(data)
                )

                return componentsschemas_selveo_sale_shipment_webhook_data_type_0
            except:  # noqa: E722
                pass
            return cast(Union["SelveoSaleShipmentWebhookDataType0", None, Unset], data)

        before = _parse_before(d.pop("before", UNSET))

        selveo_webhook_event_data_of_selveo_sale_shipment_webhook_data = cls(
            updated=updated,
            before=before,
        )

        selveo_webhook_event_data_of_selveo_sale_shipment_webhook_data.additional_properties = d
        return selveo_webhook_event_data_of_selveo_sale_shipment_webhook_data

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
