from services.package_maneger import FindPackage, PackageManeger, ListPackages

class Main:
    def __init__(self):
        package_maneger = PackageManeger()

        self.commands = {
            "install": "blabla",
            "uninstall": "blabla",
            "list": ListPackages(package_maneger),
            "find": FindPackage(package_maneger)
        }

    def run(self):
        package_name = str(input("Enter package name : "))
        command = str(input("Enter command : "))

        command = self.commands[command]
        if command:
            command.execute(package_name)


main = Main()
main.run()