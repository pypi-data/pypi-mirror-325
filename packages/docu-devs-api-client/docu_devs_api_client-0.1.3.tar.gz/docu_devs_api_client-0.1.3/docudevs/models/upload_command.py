from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UploadCommand")


@_attrs_define
class UploadCommand:
    """
    Attributes:
        ocr (Union[None, Unset, str]):
        llm (Union[None, Unset, str]):
        extraction_mode (Union[None, Unset, str]):
        schema (Union[None, Unset, str]):
        prompt (Union[None, Unset, str]):
        barcodes (Union[None, Unset, bool]):
        mime_type (Union[None, Unset, str]):
    """

    ocr: Union[None, Unset, str] = UNSET
    llm: Union[None, Unset, str] = UNSET
    extraction_mode: Union[None, Unset, str] = UNSET
    schema: Union[None, Unset, str] = UNSET
    prompt: Union[None, Unset, str] = UNSET
    barcodes: Union[None, Unset, bool] = UNSET
    mime_type: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ocr: Union[None, Unset, str]
        if isinstance(self.ocr, Unset):
            ocr = UNSET
        else:
            ocr = self.ocr

        llm: Union[None, Unset, str]
        if isinstance(self.llm, Unset):
            llm = UNSET
        else:
            llm = self.llm

        extraction_mode: Union[None, Unset, str]
        if isinstance(self.extraction_mode, Unset):
            extraction_mode = UNSET
        else:
            extraction_mode = self.extraction_mode

        schema: Union[None, Unset, str]
        if isinstance(self.schema, Unset):
            schema = UNSET
        else:
            schema = self.schema

        prompt: Union[None, Unset, str]
        if isinstance(self.prompt, Unset):
            prompt = UNSET
        else:
            prompt = self.prompt

        barcodes: Union[None, Unset, bool]
        if isinstance(self.barcodes, Unset):
            barcodes = UNSET
        else:
            barcodes = self.barcodes

        mime_type: Union[None, Unset, str]
        if isinstance(self.mime_type, Unset):
            mime_type = UNSET
        else:
            mime_type = self.mime_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ocr is not UNSET:
            field_dict["ocr"] = ocr
        if llm is not UNSET:
            field_dict["llm"] = llm
        if extraction_mode is not UNSET:
            field_dict["extractionMode"] = extraction_mode
        if schema is not UNSET:
            field_dict["schema"] = schema
        if prompt is not UNSET:
            field_dict["prompt"] = prompt
        if barcodes is not UNSET:
            field_dict["barcodes"] = barcodes
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_ocr(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        ocr = _parse_ocr(d.pop("ocr", UNSET))

        def _parse_llm(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        llm = _parse_llm(d.pop("llm", UNSET))

        def _parse_extraction_mode(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        extraction_mode = _parse_extraction_mode(d.pop("extractionMode", UNSET))

        def _parse_schema(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        schema = _parse_schema(d.pop("schema", UNSET))

        def _parse_prompt(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        prompt = _parse_prompt(d.pop("prompt", UNSET))

        def _parse_barcodes(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        barcodes = _parse_barcodes(d.pop("barcodes", UNSET))

        def _parse_mime_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        mime_type = _parse_mime_type(d.pop("mimeType", UNSET))

        upload_command = cls(
            ocr=ocr,
            llm=llm,
            extraction_mode=extraction_mode,
            schema=schema,
            prompt=prompt,
            barcodes=barcodes,
            mime_type=mime_type,
        )

        upload_command.additional_properties = d
        return upload_command

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
