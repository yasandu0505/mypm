class DependencyResolver:
    def __init__(self, dependencies, repository):
        self.dependencies = dependencies
        self.repository = repository
        self.final_dependency_list = []
    
    def find_dependencies(self, dependency):
        print("\n")
        found_dependency = self.repository.find_package(package_name=dependency)
        if not found_dependency["dependencies"]:
            if dependency not in self.final_dependency_list:
                self.final_dependency_list.append(dependency)
            print("no more sub dependencies.....")
            print("\n")
            return
        print(f"fouuuuuuuuunnndddd  ----  {found_dependency["dependencies"]}")
        for dependencyy in found_dependency["dependencies"]:
            if dependencyy not in self.final_dependency_list:
                self.final_dependency_list.insert(0,dependencyy)
            self.find_dependencies(dependency=dependencyy)

    def resolve(self) -> list:
        print("\n")
        print(f"Resolving dependencies --------- {self.dependencies}")
        for dependency in self.dependencies:
            self.find_dependencies(dependency=dependency)
            if dependency not in self.final_dependency_list:
                self.final_dependency_list.append(dependency)
        return self.final_dependency_list
