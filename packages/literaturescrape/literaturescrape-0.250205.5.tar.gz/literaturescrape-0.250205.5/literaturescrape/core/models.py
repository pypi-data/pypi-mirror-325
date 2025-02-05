from dataclasses import dataclass, asdict
from typing import Optional

@dataclass
class Literature:
    title: Optional[str] = None
    doi: Optional[str] = None
    IF: Optional[str] = None
    pmid: Optional[str] = None
    jour_name: Optional[str] = None
    jour_issn: Optional[str] = None
    
    openAccess: bool = False
    
    publish_date: Optional[str] = None
    year: Optional[str] = None
    volume: Optional[str] = None
    issue: Optional[str] = None
    page: Optional[str] = None
    
    author: Optional[str] = None
    abstract: Optional[str] = None
    
    def to_dict(self):
        return asdict(self)
    
    
@dataclass
class Response:
    source: str
    priority: int = 0
    
    fetch_flag: bool = False
    extract_flag: bool = False
    fetch_err_reason: Optional[str] = None
    extract_err_reason: Optional[str] = None
    
    finished: bool = False
    literature: Optional[Literature] = None

