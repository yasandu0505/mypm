from .package_manager import PackageManager
class PackageInstaller(PackageManager):
    def __init__(self, packages_to_install):
        self.packages_to_install = packages_to_install
        self.installed_packages = []
        super().__init__()
    
    def install(self) -> list:
        for package in self.packages_to_install:
            print(f"Installing package --------- {package["name"]} -> {package["download_location"]}")
            self.installed_packages.append(package)
        return self.installed_packages
