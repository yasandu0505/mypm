class PackageInstaller:
    def __init__(self, packages_to_install, package_name):
        self.packages_to_install = packages_to_install
        self.package_name = package_name
        self.installed_packages = []
    
    def install(self) -> list:
        for package in self.packages_to_install:
            print(f"Installing package --------- {package["name"]} -> {package["download_location"]}")
            self.installed_packages.append(package)
        
        if self.installed_packages:
            for package in self.installed_packages:
                if package["name"] == self.package_name:
                    print(f"------- {package["name"]} was installed successfully")
                else:
                    print(f"------- {package["name"]} was installed")
