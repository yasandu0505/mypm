from abc import ABC, abstractmethod
from repository.repository import Repository
from .dependency_resolver import DependencyResolver
from .package_downloader import PackageDownloader
from .package_installer import PackageInstaller

class Command(ABC):
    def __init__(self, package_manager):
        self.package_manager = package_manager

    @abstractmethod
    def execute(self):
        pass


class FindPackage(Command):
    def execute(self, package_name):
        self.package_manager.find_package(package_name=package_name)


class ListPackages(Command):
    def execute(self):
        self.package_manager.list_packages()
    
class InstallPackage(Command):
    def execute(self, package_name):
        self.package_manager.install_package(package_name=package_name)


class PackageManager:

    def __init__(self):
        self.repository = Repository()

    def install_package(self, package_name):
        package = self.repository.find_package(package_name=package_name)
        dependency_resolver = DependencyResolver(dependencies=package["dependencies"])
        resolved_dependencies = dependency_resolver.resolve()
        resolved_dependencies.append(package_name)
        print(f"Resolved dependencies --------- {resolved_dependencies}")
        downloader = PackageDownloader(packages_to_download=resolved_dependencies, repository=self.repository)
        downloaded_packages = downloader.download()
        print(f"Downloaded packages --------- {downloaded_packages}")
        installer = PackageInstaller(downloaded_packages, package_name=package_name)
        installer.install()

    def uninstall_package(self):
        pass

    def list_packages(self):
        self.repository.list_packages()

    def find_package(self, package_name):
        found = self.repository.find_package(package_name=package_name)
        return found