class DependencyResolver:
    def __init__(self, dependencies):
        self.dependencies = dependencies
    # TODO : modify this function to extract all the dependencies recursively for each package
    def resolve(self) -> list:
        print(f"Resolving dependencies -- {self.dependencies}")
        return self.dependencies
