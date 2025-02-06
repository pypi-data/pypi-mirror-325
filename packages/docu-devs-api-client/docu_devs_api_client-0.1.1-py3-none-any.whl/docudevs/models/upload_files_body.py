from io import BytesIO
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, File, FileJsonType, Unset

T = TypeVar("T", bound="UploadFilesBody")


@_attrs_define
class UploadFilesBody:
    """
    Attributes:
        document (File):
        metadata (Union[File, None, Unset]):
        prompt (Union[File, None, Unset]):
        schema (Union[File, None, Unset]):
    """

    document: File
    metadata: Union[File, None, Unset] = UNSET
    prompt: Union[File, None, Unset] = UNSET
    schema: Union[File, None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        document = self.document.to_tuple()

        metadata: Union[FileJsonType, None, Unset]
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, File):
            metadata = self.metadata.to_tuple()

        else:
            metadata = self.metadata

        prompt: Union[FileJsonType, None, Unset]
        if isinstance(self.prompt, Unset):
            prompt = UNSET
        elif isinstance(self.prompt, File):
            prompt = self.prompt.to_tuple()

        else:
            prompt = self.prompt

        schema: Union[FileJsonType, None, Unset]
        if isinstance(self.schema, Unset):
            schema = UNSET
        elif isinstance(self.schema, File):
            schema = self.schema.to_tuple()

        else:
            schema = self.schema

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "document": document,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if prompt is not UNSET:
            field_dict["prompt"] = prompt
        if schema is not UNSET:
            field_dict["schema"] = schema

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        document = self.document.to_tuple()

        metadata: Union[Tuple[None, bytes, str], Unset]

        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, File):
            metadata = self.metadata.to_tuple()
        else:
            metadata = (None, str(self.metadata).encode(), "text/plain")

        prompt: Union[Tuple[None, bytes, str], Unset]

        if isinstance(self.prompt, Unset):
            prompt = UNSET
        elif isinstance(self.prompt, File):
            prompt = self.prompt.to_tuple()
        else:
            prompt = (None, str(self.prompt).encode(), "text/plain")

        schema: Union[Tuple[None, bytes, str], Unset]

        if isinstance(self.schema, Unset):
            schema = UNSET
        elif isinstance(self.schema, File):
            schema = self.schema.to_tuple()
        else:
            schema = (None, str(self.schema).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "document": document,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if prompt is not UNSET:
            field_dict["prompt"] = prompt
        if schema is not UNSET:
            field_dict["schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        document = File(payload=BytesIO(d.pop("document")))

        def _parse_metadata(data: object) -> Union[File, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, bytes):
                    raise TypeError()
                metadata_type_0 = File(payload=BytesIO(data))

                return metadata_type_0
            except:  # noqa: E722
                pass
            return cast(Union[File, None, Unset], data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        def _parse_prompt(data: object) -> Union[File, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, bytes):
                    raise TypeError()
                prompt_type_0 = File(payload=BytesIO(data))

                return prompt_type_0
            except:  # noqa: E722
                pass
            return cast(Union[File, None, Unset], data)

        prompt = _parse_prompt(d.pop("prompt", UNSET))

        def _parse_schema(data: object) -> Union[File, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, bytes):
                    raise TypeError()
                schema_type_0 = File(payload=BytesIO(data))

                return schema_type_0
            except:  # noqa: E722
                pass
            return cast(Union[File, None, Unset], data)

        schema = _parse_schema(d.pop("schema", UNSET))

        upload_files_body = cls(
            document=document,
            metadata=metadata,
            prompt=prompt,
            schema=schema,
        )

        upload_files_body.additional_properties = d
        return upload_files_body

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
