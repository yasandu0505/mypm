from services.package_maneger import FindPackage

class Main:
    def __init__(self):

        self.commands = {
            "install": "blabla",
            "uninstall": "blabla",
            "list": "blabla",
            "find": FindPackage()
        }

    def run(self):
        package_name = str(input("Enter package name : "))
        command = str(input("Enter command : "))

        command = self.commands[command]
        if command:
            command.execute(package_name)


main = Main()
main.run()