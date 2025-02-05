from typing import Any, Optional
from pathlib import Path
from io import IOBase
import PIL.Image

from ..types.schemas.generate import GenerateSchemaRequest
from ..types.schemas.object import Schema
from ..types.schemas.promptify import PromptifyRequest
from ..types.modalities import Modality
from .._resource import SyncAPIResource, AsyncAPIResource

from .._utils.json_schema import load_json_schema
from .._utils.mime import prepare_mime_document_list
from .._utils.ai_model import assert_valid_model_schema_generation

from typing import List



class Schemas(SyncAPIResource):

    def list(self, 
             schema_id: Optional[str] = None,
             data_id: Optional[str] = None) -> List[Schema]:
        """List all schemas.

        Returns:
            list[Schema]: The list of schemas
        """

        params = {}
        if schema_id:
            params["id"] = schema_id
        if data_id:
            params["data_id"] = data_id

        return [Schema.model_validate(schema) for schema in self._client._request("GET", "/v1/schemas", params=params)]

    def get(self, schema_id: str) -> Schema:
        """Retrieve a schema by ID.

        Args:
            schema_id: The ID of the schema to retrieve

        Returns:
            Schema: The retrieved schema object
        """
        return Schema.model_validate(self._client._request("GET", f"/v1/schemas/{schema_id}"))

    

    """Schemas API wrapper"""
    def promptify(self,
               raw_schema: dict[str, Any] | Path | str,
               documents: List[Path | str | bytes | IOBase | PIL.Image.Image],
               model: str = "gpt-4o-2024-08-06",
               temperature: float = 0,
               modality: Modality = "native") -> Schema:
        """
        Enrich an existing JSON schema with additional field suggestions based on document analysis. It can be beneficial to use a bigger model (more costly but more accurate) for this task.
        
        The generated schema includes X-Prompts for enhanced LLM interactions:
        - X-SystemPrompt: Defines high-level instructions and context for consistent LLM behavior
        - X-FieldPrompt: Enhances standard description fields with specific extraction guidance
        - X-ReasoningPrompt: Creates auxiliary reasoning fields for complex data processing
        
        Args:
            raw_schema: Base JSON schema to enrich
            documents: List of documents (as MIMEData) to analyze
        
        Returns:
            dict[str, Any]: Enhanced JSON schema with additional field suggestions and X-Prompts
            
        Raises:
            HTTPException if the request fails
        """

        assert_valid_model_schema_generation(model)

        raw_schema = load_json_schema(raw_schema)

        mime_documents = prepare_mime_document_list(documents)

        data = {
            "raw_schema": raw_schema,
            "documents": [doc.model_dump() for doc in mime_documents],
            "model": model,
            "temperature": temperature,
            "modality": modality
        }

        PromptifyRequest.model_validate(data)
        
        return Schema.model_validate(self._client._request("POST", "/v1/schemas/promptify", data=data))

    def generate(self,
                documents: List[Path | str | bytes | IOBase | PIL.Image.Image],
                model: str = "gpt-4o-2024-11-20",
                temperature: float = 0.0,
                modality: Modality = "native") -> Schema:
        """
        Generate a complete JSON schema by analyzing the provided documents.
        
        The generated schema includes X-Prompts for enhanced LLM interactions:
        - X-SystemPrompt: Defines high-level instructions and context for consistent LLM behavior
        - X-FieldPrompt: Enhances standard description fields with specific extraction guidance
        - X-ReasoningPrompt: Creates auxiliary reasoning fields for complex data processing
        
        Args:
            documents: List of documents (as MIMEData) to analyze
        
        Returns:
            dict[str, Any]: Generated JSON schema with X-Prompts based on document analysis
            
        Raises:
            HTTPException if the request fails
        """

        assert_valid_model_schema_generation(model)

        mime_documents = prepare_mime_document_list(documents)

        data = {
            "documents": [doc.model_dump() for doc in mime_documents],
            "model": model,
            "temperature": temperature,
            "modality": modality
        }
        
        GenerateSchemaRequest.model_validate(data)

        return Schema.model_validate(self._client._request("POST", "/v1/schemas/generate", data=data))
        


class AsyncSchemas(AsyncAPIResource):
    """Schemas Asyncronous API wrapper"""
    async def promptify(self,
                    raw_schema: dict[str, Any] | Path | str,
                    documents: list[Path | str | bytes | IOBase | PIL.Image.Image],
                    model: str = "gpt-4o-2024-08-06",
                    temperature: float = 0,
                    modality: Modality = "native") -> Schema:
        """
        Enrich an existing JSON schema with additional field suggestions based on document analysis. It can be beneficial to use a bigger model (more costly but more accurate) for this task.
        
        The generated schema includes X-Prompts for enhanced LLM interactions:
        - X-SystemPrompt: Defines high-level instructions and context for consistent LLM behavior
        - X-FieldPrompt: Enhances standard description fields with specific extraction guidance
        - X-ReasoningPrompt: Creates auxiliary reasoning fields for complex data processing
        
        Args:
            raw_schema: Base JSON schema to enrich
            documents: List of documents (as MIMEData) to analyze
        
        Returns:
            dict[str, Any]: Enhanced JSON schema with additional field suggestions and X-Prompts
            
        Raises:
            HTTPException if the request fails
        """

        assert_valid_model_schema_generation(model)

        raw_schema = load_json_schema(raw_schema)

        mime_documents = prepare_mime_document_list(documents)

        data = {
            "raw_schema": raw_schema,
            "documents": [doc.model_dump() for doc in mime_documents],
            "model": model,
            "temperature": temperature,
            "modality": modality
        }

        PromptifyRequest.model_validate(data)
        
        return Schema.model_validate(await self._client._request("POST", "/v1/schemas/promptify", data=data))

    async def generate(self,
                    documents: list[Path | str | bytes | IOBase | PIL.Image.Image],
                    model: str = "gpt-4o-2024-11-20",
                    temperature: float = 0.0,
                    modality: Modality = "native") -> Schema:
        """
        Generate a complete JSON schema by analyzing the provided documents.
        
        The generated schema includes X-Prompts for enhanced LLM interactions:
        - X-SystemPrompt: Defines high-level instructions and context for consistent LLM behavior
        - X-FieldPrompt: Enhances standard description fields with specific extraction guidance
        - X-ReasoningPrompt: Creates auxiliary reasoning fields for complex data processing
        
        Args:
            documents: List of documents (as MIMEData) to analyze
        
        Returns:
            dict[str, Any]: Generated JSON schema with X-Prompts based on document analysis
            
        Raises
            HTTPException if the request fails
        """

        assert_valid_model_schema_generation(model)

        mime_documents = prepare_mime_document_list(documents)

        data = {
            "documents": [doc.model_dump() for doc in mime_documents],
            "model": model,
            "temperature": temperature,
            "modality": modality
        }

        GenerateSchemaRequest.model_validate(data)

        return Schema.model_validate(await self._client._request("POST", "/v1/schemas/generate", data=data))
