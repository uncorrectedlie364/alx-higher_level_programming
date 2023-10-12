#!/usr/bin/python3

import py_compile
import imp

if __name__ == "__main__":
    # Compile the module if not already compiled
    py_compile.compile('hidden_4.py')

    # Load the compiled module
    compiled_module = imp.load_compiled('hidden_4', 'hidden_4.pyc')

    # Get and print the names that don't start with '__'
    module_names = [name for name in dir(compiled_module) if not name.startswith('__')]
    for name in sorted(module_names):
        print(name)
