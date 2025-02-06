import requests
import time 
from requests_toolbelt.multipart.encoder import MultipartEncoder

class EMFClient:
    def __init__(self, api_key):
        """
        Initialize the client.
        :param base_url: Base URL of the API.
        :param api_key: API key for authentication.
        """
        self.base_url = "https://api.sentech.ai"
        self.headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

    def add_memory(self, field_id, content, timestamp, relevance=1.0, decay_rate=0.01, salience=1.0 ):
        """
        Add a memory to the specified field, with optional salience.
        :param field_id: The ID of the field to add the memory to.
        :param content: The memory content.
        :param relevance: The relevance of the memory (default 1.0).
        :param decay_rate: The decay rate of the memory (default 0.01).
        :param salience: The salience of the memory (default None, initialized by API).
        :param timestamp: The timestamp for the memory (default None, uses current time).
        :return: API response.
        """
        if not content:
            raise ValueError("Content is required to add a memory.")
        print(f"Adding memory to field {field_id} with timestamp: {timestamp}")
        data = {
            "content": content,
            "relevance": relevance,
            "decay_rate": decay_rate,
            "salience": salience,
            "timestamp": timestamp,
        }
        try:
            response = requests.post(
                f"{self.base_url}/fields/{field_id}/memories", json=data, headers=self.headers
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error adding memory: {e}")
            raise

    def query_memory(self, field_id, query, top_k=50, depth_k=3):
        """
        Query memories from the field.
        :param field_id: The field ID to query.
        :param query: The query string.
        :param top_k: Number of top results to return.
        :return: Query results.
        """
        if not query:
            raise ValueError("Query text is required to perform a memory search.")
        data = {"query": query, "top_k": top_k, "depth_k": depth_k}
        try:
            response = requests.post(f"{self.base_url}/fields/{field_id}/memories/query", json=data, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error querying memory: {e}")
            raise

    def query_image(self, field_id, query=None, image_path=None, top_k=50):
        """
        Query memories using both text and an optional image.
        :param field_id: The field ID to query.
        :param query: The text query (optional).
        :param image_path: Path to the image file to query with (optional).
        :param top_k: Number of top results to return.
        :return: Combined query results.
        """
        if not query and not image_path:
            raise ValueError("Either a text query or an image is required to perform a combined query.")

        # Prepare multipart form data
        form_data = MultipartEncoder(fields={})
        if query:
            form_data = MultipartEncoder(fields={"query": query, "top_k": str(top_k)})
        if image_path:
            with open(image_path, "rb") as image_file:
                form_data = MultipartEncoder(
                    fields={
                        "query": query or "",
                        "top_k": str(top_k),
                        "image": ("image.jpg", image_file, "image/jpeg"),
                    }
                )

        try:
            response = requests.post(
                f"{self.base_url}/fields/{field_id}/memories/query_combined",
                headers={**self.headers, "Content-Type": form_data.content_type},
                data=form_data,
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error querying combined memories: {e}")
            raise