from http import HTTPStatus
from io import BytesIO

from docudevs.client import AuthenticatedClient
from docudevs.api.document import upload_files, upload_document, process_document
from docudevs.api.template import list_templates, metadata, delete_template, fill
from docudevs.api.job import result, status
from docudevs.models import UploadDocumentBody, UploadCommand, UploadResponse
from docudevs.types import File
# New imports for concrete parameters:
from docudevs.models.upload_files_body import UploadFilesBody
from docudevs.models.template_fill_request import TemplateFillRequest

class DocuDevsClient:
    def __init__(self, api_url: str = "https://api.docudevs.ai", token: str = None):
        self.api_url = api_url
        self.token = token

    def _create_client(self) -> AuthenticatedClient:
        return AuthenticatedClient(base_url=self.api_url, token=self.token)

    async def upload_files(self, body: UploadFilesBody):
        """Upload multiple files."""
        client = self._create_client()
        return await upload_files.asyncio_detailed(client=client, body=body)

    async def upload_document(self, body: UploadDocumentBody):
        """Upload a single document."""
        client = self._create_client()
        return await upload_document.asyncio_detailed(client=client, body=body)

    async def list_templates(self):
        """List all templates."""
        client = self._create_client()
        return await list_templates.asyncio_detailed(client=client)

    async def metadata(self, template_id: str):
        """Get metadata for a template."""
        client = self._create_client()
        return await metadata.asyncio_detailed(client=client, template_id=template_id)

    async def delete_template(self, template_id: str):
        """Delete template by ID."""
        client = self._create_client()
        return await delete_template.asyncio_detailed(client=client, template_id=template_id)

    async def process_document(self, guid: str, body: UploadCommand):
        """Process a document."""
        client = self._create_client()
        return await process_document.asyncio_detailed(client=client, guid=guid, body=body)

    async def result(self, uuid: str):
        """Get job result."""
        client = self._create_client()
        return await result.asyncio_detailed(client=client, uuid=uuid)

    async def status(self, guid: str):
        """Get job status."""
        client = self._create_client()
        return await status.asyncio_detailed(client=client, guid=guid)

    async def fill(self, name: str, body: TemplateFillRequest):
        """Fill a template."""
        client = self._create_client()
        return await fill.asyncio_detailed(client=client, name=name, body=body)

    async def submit_and_process_document(self, document: BytesIO,
                                          document_mime_type: str,
                                          prompt: str="",
                                          schema:str="",
                                          ocr: str = None,
                                          barcodes: bool = None,
                                          llm: str = None,
                                          extraction_mode = None
                                          ) -> str:
        # Check mimetype
        if not document_mime_type:
            raise ValueError("document_mime_type is required")
        if not document:
            raise ValueError("document is required")

        document_file = File(payload=document,
                             file_name="omitted",
                             mime_type=document_mime_type)
        # Create the upload document body
        upload_body = UploadDocumentBody(document=document_file)

        # Upload the document
        upload_response = await self.upload_document(body=upload_body)
        if upload_response.status_code != HTTPStatus.OK:
            raise Exception(f"Error uploading document: {upload_response.content}")
        # Process the uploaded document
        guid = upload_response.parsed.guid
        process_body = UploadCommand(prompt=prompt,
                                     schema=schema,
                                     mime_type=document_mime_type,
                                     ocr=ocr,
                                     barcodes=barcodes,
                                     llm=llm,
                                     extraction_mode=extraction_mode)
        process_resp = await self.process_document(guid=guid, body=process_body)
        if process_resp.status_code != HTTPStatus.OK:
            raise Exception(f"Error processing document: {upload_response.content}")
        return upload_response.parsed.guid

    async def wait_until_ready(self, guid: str):
        response = await self.result(uuid=guid)
        if response.status_code != HTTPStatus.OK:
            raise Exception(f"Error getting result: {response.content} (status code: {response.status_code})")
        return response.parsed

    # Re-export model classes for direct imports:
    UploadDocumentBody = UploadDocumentBody
    UploadCommand = UploadCommand
    File = File
    # New: re-export additional models:
    UploadFilesBody = UploadFilesBody
    TemplateFillRequest = TemplateFillRequest

# Module-level re-export for direct importing:
UploadFilesBody = UploadFilesBody
TemplateFillRequest = TemplateFillRequest

__all__ = [
    "DocuDevsClient",
    "UploadDocumentBody",
    "UploadCommand",
    "File",
    "UploadFilesBody",
    "TemplateFillRequest",
    # ... add other models if needed ...
]

