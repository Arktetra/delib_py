from typing import Optional

ScalarLike = [float, int, "Scalar"]

_var_count = 0
    
class Scalar:
    data: float
    unique_id: int 
    name: str
    
    def __init__(
        self, 
        value: float,
        name: Optional[str] = None
    ):
        global _var_count
        _var_count += 1
        self.unique_id = _var_count
        self.data = float(value)
        
        if name is not None:
            self.name = name
        else:
            self.name = str(self.unique_id)
            
    def __repr__(self) -> str:
        return "Scalar(%f)" % self.data