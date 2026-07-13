class PackageDownloader:
    def __init__(self, packages_to_download, repository):
        self.packages_to_download = packages_to_download
        self.downloaded_packages = []
        self.repository = repository
    
    def download(self) -> dict:
        for package in self.packages_to_download:
            found_package = self.repository.find_package(package_name=package)
            if found_package:
                print(f"Downloading package --------- {package}")
                self.downloaded_packages.append({
                    "name": package,
                    "download_location": found_package["link"]
                })
        return self.downloaded_packages
