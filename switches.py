# Script for formatting and printing switches with descriptions

class Switch():
    def __init__(self, modules, interfaces, ignored_modules=()):
        '''Initialize modules'''
        self.modules = int(modules)
        self.interfaces = int(interfaces)
        self.ignored_modules = ignored_modules
        self.format_interfaces(self.list_modules(), self.list_interfaces())

    def list_modules(self):
        '''Provides a list of modules, with ignored modules accounted for'''
        # Set Module Range to a list so ignored_modules can be removed
        module_list = list(range(1, self.modules+1))

        # Checks if a tuple is being supplied for ignoring
        # (multiple interfaces) and removes if it exists
        if type(self.ignored_modules) is tuple:
            # Iterate through provided tuple of ignored modules.
            for ignored_module in self.ignored_modules:
                # Removes ignored module from module list
                module_list.remove(ignored_module)

        # Checks if an integer is being supplied for ignoring (single interface)
        # and removes if it exists
        elif type(self.ignored_modules) is int:
            # Removes ignored module from module list
            module_list.remove(self.ignored_modules)
        return module_list


    def list_interfaces(self):
        # Simply return a list of 1 to # of provided interfaces
        return list(range(1, self.interfaces+1))

    def format_interfaces(self, module_list, interface_list):
        for module in module_list:
            for interface in interface_list:
                # Stringify the interface, and pad any numbers len <2 with a 0.
                interface = str(interface).zfill(2)
                print("gigabitEthernet {}/{}".format(module,interface))


def main():
    switch = Switch(modules=10,interfaces=48,ignored_modules=(5,6))


if __name__ == "__main__":
    main()
