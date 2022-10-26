import argparse
from dataclasses import dataclass
@dataclass(init=True, repr=True)
class Arguments:
    parser = argparse.ArgumentParser(prog='PROG')
    parser.add_argument('--foo', nargs='?', help='foo help')
    parser.add_argument('bar',nargs='+', help='bar help')
    parser.print_help()

