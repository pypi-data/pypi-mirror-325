from bsscripts.commands import AppCommand, Command
from bsscripts.utils import TablePrinter


class HelpCommand(AppCommand):
    def __init__(self):
        super().__init__(["help"], "Show help")

    def show_generic_help(self):
        table = TablePrinter()
        table.add_column("command")
        table.add_column("arguments")
        table.add_column("description")

        for command in self.app.commands:
            positional_args = " ".join(
                f"<{arg.name}>" for arg in command.positional_args
            )
            flag_args = " ".join(f"[--{arg.name}]" for arg in command.flag_args)
            args = " ".join([positional_args, flag_args])

            table.add_row([" ".join(command.prefix), args, command.description])

        table.print()

        print("\nType 'help command' to see detailed help.")

    @staticmethod
    def show_command_help(command: Command):
        print(f'Help for command: {" ".join(command.prefix)}\n')
        # TODO: Some 'long' description?
        print(command.description)
        print("\nPositional arguments (required):")
        for arg in command.positional_args:
            print(f"  <{arg.name}> - {arg.help}")
        print("\nFlag arguments (optional):")
        for arg in command.flag_args:
            print(f"  --{arg.name} - {arg.help}")
        print()

    def execute(self):
        if not self.args:
            self.show_generic_help()
        else:
            for command in self.app.commands:
                if command.prefix == self.args:
                    self.show_command_help(command)
