class TimeMap:

    def __init__(self):
        self.mapp = {}

        

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.mapp:
            self.mapp[key] = []

        self.mapp[key].append((timestamp,value))
        

        

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.mapp:
            return ""

        pair = self.mapp[key]

        val = ""
 
        for t, k in pair:
            if t <= timestamp:
                val = k
            else:
                break
        
        return val

        

        
