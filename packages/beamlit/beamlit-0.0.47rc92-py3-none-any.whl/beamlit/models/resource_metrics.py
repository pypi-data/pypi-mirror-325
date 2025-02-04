from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metric import Metric
    from ..models.qps import QPS


T = TypeVar("T", bound="ResourceMetrics")


@_attrs_define
class ResourceMetrics:
    """Metrics for a single resource (eg. model, function)

    Attributes:
        inference_global (Union[Unset, list['Metric']]): Array of metrics
        query_per_region (Union[Unset, QPS]): Query per second per element, can be per response status code (e.g. 200,
            400) or per location
    """

    inference_global: Union[Unset, list["Metric"]] = UNSET
    query_per_region: Union[Unset, "QPS"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        inference_global: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.inference_global, Unset):
            inference_global = []
            for componentsschemas_array_metric_item_data in self.inference_global:
                componentsschemas_array_metric_item = componentsschemas_array_metric_item_data.to_dict()
                inference_global.append(componentsschemas_array_metric_item)

        query_per_region: Union[Unset, dict[str, Any]] = UNSET
        if self.query_per_region and not isinstance(self.query_per_region, Unset):
            query_per_region = self.query_per_region.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if inference_global is not UNSET:
            field_dict["inferenceGlobal"] = inference_global
        if query_per_region is not UNSET:
            field_dict["queryPerRegion"] = query_per_region

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.metric import Metric
        from ..models.qps import QPS

        if not src_dict:
            return None
        d = src_dict.copy()
        inference_global = []
        _inference_global = d.pop("inferenceGlobal", UNSET)
        for componentsschemas_array_metric_item_data in _inference_global or []:
            componentsschemas_array_metric_item = Metric.from_dict(componentsschemas_array_metric_item_data)

            inference_global.append(componentsschemas_array_metric_item)

        _query_per_region = d.pop("queryPerRegion", UNSET)
        query_per_region: Union[Unset, QPS]
        if isinstance(_query_per_region, Unset):
            query_per_region = UNSET
        else:
            query_per_region = QPS.from_dict(_query_per_region)

        resource_metrics = cls(
            inference_global=inference_global,
            query_per_region=query_per_region,
        )

        resource_metrics.additional_properties = d
        return resource_metrics

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
