from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.selveo_webhook_event_data_of_selveo_sale_order_webhook_data import (
        SelveoWebhookEventDataOfSelveoSaleOrderWebhookData,
    )


T = TypeVar("T", bound="Request")


@_attrs_define
class Request:
    """
    Attributes:
        event_name (Union[Unset, str]):
        event_id (Union[Unset, str]):
        event_data (Union[Unset, SelveoWebhookEventDataOfSelveoSaleOrderWebhookData]):
    """

    event_name: Union[Unset, str] = UNSET
    event_id: Union[Unset, str] = UNSET
    event_data: Union[Unset, "SelveoWebhookEventDataOfSelveoSaleOrderWebhookData"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_name = self.event_name

        event_id = self.event_id

        event_data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.event_data, Unset):
            event_data = self.event_data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event_name is not UNSET:
            field_dict["eventName"] = event_name
        if event_id is not UNSET:
            field_dict["eventId"] = event_id
        if event_data is not UNSET:
            field_dict["eventData"] = event_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.selveo_webhook_event_data_of_selveo_sale_order_webhook_data import (
            SelveoWebhookEventDataOfSelveoSaleOrderWebhookData,
        )

        d = src_dict.copy()
        event_name = d.pop("eventName", UNSET)

        event_id = d.pop("eventId", UNSET)

        _event_data = d.pop("eventData", UNSET)
        event_data: Union[Unset, SelveoWebhookEventDataOfSelveoSaleOrderWebhookData]
        if isinstance(_event_data, Unset):
            event_data = UNSET
        else:
            event_data = SelveoWebhookEventDataOfSelveoSaleOrderWebhookData.from_dict(_event_data)

        request = cls(
            event_name=event_name,
            event_id=event_id,
            event_data=event_data,
        )

        request.additional_properties = d
        return request

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
