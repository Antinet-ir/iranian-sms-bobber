import json, os
from datetime import datetime

class Logger:
    def __init__(self):
        self.logs = []
        self.start_time = datetime.now().isoformat()

    def log(self, service, number, status, result, error=None):
        entry = {
            "time": datetime.now().isoformat(),
            "service": service,
            "number": number,
            "status": status,
            "result": result,
            "error": error
        }
        self.logs.append(entry)

    def save(self):
        folder = "logs"
        os.makedirs(folder, exist_ok=True)
        filename = os.path.join(folder, f"results_{datetime.now().date()}.json")
        with open(filename, "w") as f:
            json.dump(self.logs, f, indent=2)
