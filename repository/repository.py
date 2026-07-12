import json
from pathlib import Path

class Repository:

    def __init__(self):
        file_path = Path(__file__).parent / "package.json"
        with open(file=file_path ,mode="r", encoding="utf-8") as packages:
            self.packages = json.load(packages)

        
    def find_package(self,package_name):
        print("\n")
        package = self.packages[package_name]
        if package:
            for key, value in package.items():
                print(f"{key} - {value}")

