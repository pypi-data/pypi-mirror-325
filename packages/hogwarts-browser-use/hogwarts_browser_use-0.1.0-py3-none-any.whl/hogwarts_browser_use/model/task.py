from typing import Optional, Any, Union
from pydantic import BaseModel


class Task(BaseModel):
    task: Union[str, tuple]
    model: Optional[str] = None
    key: Optional[str] = None
    base_url: Optional[str] = None
    reuse_browser: bool = False
    temperature: float = 0

    def model_post_init(self, __context: Any) -> None:
        if isinstance(self.task, tuple):
            self.task = ' '.join(self.task)
