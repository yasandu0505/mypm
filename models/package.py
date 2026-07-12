from dataclasses import dataclass, field

@dataclass
class Package:
    name : str
    link : str
    dependencies : list[str] = field(default_factory=list) 
    # we do not use [] as the default value, so we use default_factory=list , this ensures each instance gets its own separate list