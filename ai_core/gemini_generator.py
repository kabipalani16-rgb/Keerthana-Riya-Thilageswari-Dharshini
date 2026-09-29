import os
import google.generativeai as genai


class GeminiDocumentGenerator:

    def _init_(self):
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("GEMINI_API_KEY is not set")

        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-1.5-pro")

    def generate_document(self, document_type, parties, terms, dates):

        prompt = f"""
        Generate a professional {document_type}.

        Parties:
        {parties}

        Terms:
        {terms}

        Dates:
        {dates}

        Create a clear and well-structured legal document.
        """

        response = self.model.generate_content(prompt)

        return response.text
