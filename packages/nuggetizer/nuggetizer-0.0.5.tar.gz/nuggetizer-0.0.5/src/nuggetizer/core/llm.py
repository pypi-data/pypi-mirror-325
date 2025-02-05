import os
import time
from typing import Dict, List, Optional, Union, Tuple
import tiktoken
from openai import AzureOpenAI, OpenAI
from ..utils.api import get_azure_openai_args, get_openai_api_key

class LLMHandler:
    def __init__(
        self,
        model: str,
        api_keys: Optional[Union[str, List[str]]] = None,
        context_size: int = 8192,
        api_type: Optional[str] = None,
        api_base: Optional[str] = None,
        api_version: Optional[str] = None,
        use_azure_openai: bool = False,
    ):
        self.model = model
        self.context_size = context_size
        
        # Auto-configure API keys and Azure settings if not provided
        if (use_azure_openai and (api_keys is None or (api_type == "azure" or (api_type is None and "gpt" in model.lower())))):
            azure_args = get_azure_openai_args()
            api_type = "azure"
            api_base = azure_args.get("api_base")
            api_version = azure_args.get("api_version")
            api_keys = azure_args.get("api_key", api_keys) or get_openai_api_key()
        else:
            api_type = "openai"
            api_keys = api_keys or get_openai_api_key()
        self.api_keys = [api_keys] if isinstance(api_keys, str) else api_keys
        self.current_key_idx = 0
        self.client = self._initialize_client(api_type, api_base, api_version)
        
    def _initialize_client(self, api_type, api_base, api_version):
        if api_type == "azure" and all([api_base, api_version]):
            return AzureOpenAI(
                api_key=self.api_keys[0],
                api_version=api_version,
                azure_endpoint=api_base
            )
        elif api_type == "openai":
            return OpenAI(api_key=self.api_keys[0])
        else:
            raise ValueError(f"Invalid API type: {api_type}")

    def run(
        self, 
        messages: List[Dict[str, str]], 
        temperature: float = 0
    ) -> Tuple[str, int]:
        while True:
            if "o1" in self.model:
                # System message is not supported for o1 models
                new_messages = messages[1:]
                new_messages[0]["content"] = messages[0]["content"] + "\n" + messages[1]["content"]
                messages = new_messages[:]
                temperature = 1.0
            try:
                completion = self.client.chat.completions.create(
                    model=self.model,
                    messages=messages,
                    temperature=temperature,
                    max_completion_tokens=2048,
                    timeout=30
                )
                response = completion.choices[0].message.content
                try:
                    encoding = tiktoken.get_encoding(self.model)
                except:
                    encoding = tiktoken.get_encoding("cl100k_base")
                return response, len(encoding.encode(response))
            except Exception as e:
                print(f"Error: {str(e)}")
                self.current_key_idx = (self.current_key_idx + 1) % len(self.api_keys)
                self.client.api_key = self.api_keys[self.current_key_idx]
                time.sleep(0.1)
