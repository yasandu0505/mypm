class DependencyResolver:
    def __init__(self, package, repository):
        self.package = package
        self.repository = repository
        self.visited_dependencies = set()
        self.final_dependency_order = []
    
    def find_dependencies(self, package):
        print("\n")
        if package in self.visited_dependencies:
            return
        
        self.visited_dependencies.add(package)

        found_dependency = self.repository.find_package(package_name=package)

        for sub_dependency in found_dependency["dependencies"]:
            self.find_dependencies(package=sub_dependency)
        
        self.final_dependency_order.append(package)


    def resolve(self) -> list:
        print("\n")
        print(f"Resolving dependencies --------- {self.package}")
        self.find_dependencies(package=self.package)
        return self.final_dependency_order
