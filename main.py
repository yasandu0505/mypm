import argparse
from services.package_manager import FindPackage, PackageManager, ListPackages


class Main:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description="Simple Package Manager"
        )
        self.package_manager = PackageManager()
        self.package_name = ""

        self.commands = {
            "install": "blabla",
            "uninstall": "blabla",
            "list": ListPackages(self.package_manager),
            "find": FindPackage(self.package_manager)
        }

    def run(self):
        self.parser.add_argument("command", help="Command to run")
        self.parser.add_argument("--package_name", help="Package name to proceed with")
        args = self.parser.parse_args()
        
        if args.package_name:
            self.package_name = args.package_name

        command = self.commands[args.command]
        if command:
            if self.package_name:
                command.execute(self.package_name)
            else:
                command.execute()

main = Main()
main.run()