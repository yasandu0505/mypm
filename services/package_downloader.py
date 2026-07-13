from .package_manager import PackageManager
class PackageDownloader(PackageManager):
    def __init__(self, packages_to_download):
        self.packages_to_download = packages_to_download
        self.downloaded_packages = []
        super().__init__()
    
    def download(self) -> dict:
        for package in self.packages_to_download:
            found_package = super().find_package(package_name=package)
            if found_package:
                print(f"Downloading package --------- {package}")
                self.downloaded_packages.append({
                    "name": package,
                    "download_location": found_package["link"]
                })
        return self.downloaded_packages
