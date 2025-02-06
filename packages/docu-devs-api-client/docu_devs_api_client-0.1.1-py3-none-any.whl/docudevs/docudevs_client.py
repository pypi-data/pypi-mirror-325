from docudevs.client import AuthenticatedClient
from docudevs.api.document import upload_files, upload_document, process_document
from docudevs.api.template import list_templates, metadata, delete_template, fill
from docudevs.api.job import result, status
from docudevs.models import UploadDocumentBody, UploadCommand
from docudevs.types import File
# New imports for concrete parameters:
from docudevs.models.upload_files_body import UploadFilesBody
from docudevs.models.template_fill_request import TemplateFillRequest

class DocuDevsClient:
    def __init__(self, api_url: str = "https://api.docudevs.ai", token: str = None):
        # Create the openapi-python-client AuthenticatedClient
        self._client = AuthenticatedClient(base_url=api_url, token=token)

    async def upload_files(self, body: UploadFilesBody):
        """Upload multiple files."""
        return await upload_files.asyncio_detailed(client=self._client, body=body)

    async def upload_document(self, body: UploadDocumentBody):
        """Upload a single document."""
        return await upload_document.asyncio_detailed(client=self._client, body=body)

    async def list_templates(self):
        """List all templates."""
        return await list_templates.asyncio_detailed(client=self._client)

    async def metadata(self, template_id: str):
        """Get metadata for a template."""
        return await metadata.asyncio_detailed(client=self._client, template_id=template_id)

    async def delete_template(self, template_id: str):
        """Delete template by ID."""
        return await delete_template.asyncio_detailed(client=self._client, template_id=template_id)

    async def process_document(self, guid: str, body: UploadCommand):
        """Process a document."""
        return await process_document.asyncio_detailed(client=self._client, guid=guid, body=body)

    async def result(self, uuid: str):
        """Get job result."""
        return await result.asyncio_detailed(client=self._client, uuid=uuid)

    async def status(self, guid: str):
        """Get job status."""
        return await status.asyncio_detailed(client=self._client, guid=guid)

    async def fill(self, name: str, body: TemplateFillRequest):
        """Fill a template."""
        return await fill.asyncio_detailed(client=self._client, name=name, body=body)

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

