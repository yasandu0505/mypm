from abc import ABC, abstractmethod
from repository.repository import Repository

class Command(ABC):
    def __init__(self,):
        self.repository = Repository()

    @abstractmethod
    def execute(self):
        pass


class FindPackage(Command):
    def execute(self, package_name):
        self.repository.find_package(package_name=package_name)
    
class PackageManeger(FindPackage):
    def __init__(self):
        pass

    def install_package(self):
        pass

    def uninstall_package(self):
        pass

    def list_packages(self):
        pass

    def find_package(self, package_name):
        find = FindPackage(self.repository)
        find.execute(package_name=package_name)