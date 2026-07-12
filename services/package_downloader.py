from .package_manager import PackageManager
class PackageDownloader(PackageManager):
    def __init__(self, packages_to_download):
        self.packages_to_download = packages_to_download
        self.downloaded_packages = []
        super().__init__()
    
    def download(self) -> list:
        for package in self.packages_to_download:
            found_package = super().find_package(package_name=package)
            print(f"Downloading package {found_package}...")

            self.downloaded_packages.append(package)
        return self.downloaded_packages
