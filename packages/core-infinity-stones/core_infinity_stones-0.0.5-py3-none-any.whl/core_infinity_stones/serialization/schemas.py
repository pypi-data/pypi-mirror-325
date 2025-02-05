from abc import ABC, abstractmethod
from typing import Any, Callable, Sequence
import xml.etree.ElementTree as ET
from pydantic import BaseModel


class XmlEncodableModel(BaseModel, ABC):
    @property
    @abstractmethod
    def xml_tag_name(self) -> str:
        raise NotImplementedError
