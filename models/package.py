from dataclasses import dataclass, field

@dataclass
class Package:
    name : str
    link : str
    dependencies : list[str] = field(default_factory=list)