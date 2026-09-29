from fastapi import APIRouter
from pydantic import BaseModel
from ai_core.gemini_generator import GeminiDocumentGenerator

router = APIRouter()


class DocumentRequest(BaseModel):
    document_type: str
    parties: str
    terms: str
    dates: str


@router.post("/generate")
def generate_document(request: DocumentRequest):
    generator = GeminiDocumentGenerator()

    document = generator.generate_document(
        document_type=request.document_type,
        parties=request.parties,
        terms=request.terms,
        dates=request.dates
    )

    return {"generated_document": document}
