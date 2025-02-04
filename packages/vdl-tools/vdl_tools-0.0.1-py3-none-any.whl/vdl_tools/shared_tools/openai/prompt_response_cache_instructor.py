import json
import logging

import instructor
from openai import OpenAI

from vdl_tools.shared_tools.database_cache.models.prompt import PromptResponse
from vdl_tools.shared_tools.openai.prompt_response_cache_sql import PromptResponseCacheSQL
from vdl_tools.shared_tools.openai.openai_constants import MODEL_DATA
from vdl_tools.shared_tools.tools.logger import logger
from vdl_tools.shared_tools.openai.openai_api_utils import CLIENT

logger.setLevel(logging.DEBUG)
logging.getLogger("openai").setLevel(logging.DEBUG)
logging.getLogger("instructor").setLevel(logging.DEBUG)

CLIENT = instructor.patch(CLIENT, mode=instructor.Mode.JSON)

class InstructorPRC(PromptResponseCacheSQL):
    """Similar to the PromprtResponseCacheSQL but
    for queries that will use the Instructor API. This allows for
    using response model (Pydantic model) to validate the response
    """
    def __init__(
        self,
        session,
        prompt_str,
        response_model,
        prompt_name=None,
        model="gpt-4o-mini",
    ):
        # If None or "" is passed in
        prompt_str_w_schema = f"{prompt_str}\n{response_model.schema_json()}"
        super().__init__(
            session=session,
            prompt_str=prompt_str_w_schema,
            prompt_name=prompt_name,
        )
        self.prompt_text = prompt_str
        self.response_model = response_model
        self.model = model

    def get_completion(
        self,
        prompt_str,
        text,
        max_tokens=4096,
        **kwargs
    ):

        response = CLIENT.chat.completions.create(
            model=MODEL_DATA[self.model]["model_name"],
            response_model=self.response_model,
            max_tokens=max_tokens,
            max_retries=1,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": self.prompt_text,
                        },
                        {
                            "type": "text",
                            "text": text,
                        }
                    ],
                }
            ],
        )

        return response

    def store_item(
        self,
        given_id: str,
        text,
        response,
    ):
        prompt_response_obj = PromptResponse(
            prompt_id=self.prompt.id,
            given_id=given_id,
            input_text=text,
            response_full=response._raw_response.model_dump(),
            response_text=json.dumps(response.dict())
        )

        self.session.merge(prompt_response_obj)
        return prompt_response_obj
