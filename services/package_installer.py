from .package_manager import PackageManager
class PackageInstaller(PackageManager):
    def __init__(self, packages_to_install):
        self.packages_to_install = packages_to_install
        self.installed_packages = []
        super().__init__()
    
    def install(self) -> list:
        for package in self.packages_to_install:
            found_package = super().find_package(package_name=package)
            print(f"Installing package {found_package}...")
            self.installed_packages.append(package)
        return self.installed_packages
