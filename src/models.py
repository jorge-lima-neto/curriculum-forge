from dataclasses import dataclass, field
from typing import List

@dataclass
class Section:
    """
    Represents a section in the resume (e.g., Experience, Education).
    """
    title: str
    content: str  # HTML formatted content

@dataclass
class Resume:
    """
    Represents the complete resume data.
    """
    name: str = ""
    contacts: List[str] = field(default_factory=list)
    sections: List[Section] = field(default_factory=list)
