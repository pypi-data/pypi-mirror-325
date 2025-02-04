import json
import requests
from pydantic import BaseModel
from typing import Optional
from valyu.types.context import SearchResponse, SearchType

class ErrorResponse(BaseModel):
    success: bool
    error: str

class Context:
    BASE_API_URL = "https://api.valyu.network/v1"

    def __init__(self, api_key=None):
        self.api_endpoint = f"{self.BASE_API_URL}/knowledge"
        self.api_key = api_key

    def fetch_context(
        self, 
        query: str, 
        search_type: SearchType, 
        num_query: int = 10,
        num_results: int = 10,
        max_price: int = 1
    ) -> Optional[SearchResponse]:
        try:
            payload = {
                "query": query,
                "search_type": search_type,
                "num_query": num_query,
                "num_results": num_results,
                "max_price": max_price
            }
            print(f"Payload being sent: {json.dumps(payload, indent=2)}")
            headers = {
                "Content-Type": "application/json",
                "x-api-key": self.api_key
            }
            response = requests.post(
                self.api_endpoint, 
                json=payload,
                headers=headers
            )

            data = response.json()
            if not response.ok:
                error_resp = ErrorResponse(**data)
                return None
                
            return SearchResponse(**data)
        except Exception as e:
            print(f"Error details: {str(e)}")
            return None
