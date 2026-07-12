from abc import ABC, abstractmethod
from repository.repository import Repository

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


class PackageManager:

    def __init__(self):
        self.repository = Repository()

    def install_package(self):
        pass

    def uninstall_package(self):
        pass

    def list_packages(self):
        self.repository.list_packages()

    def find_package(self, package_name):
        self.repository.find_package(package_name=package_name)