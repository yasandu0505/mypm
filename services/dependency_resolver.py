class DependencyResolver:
    def __init__(self, dependencies):
        self.dependencies = dependencies

    def resolve(self) -> list:
        print(f"Resolving dependencies -- {self.dependencies}")
        return self.dependencies
