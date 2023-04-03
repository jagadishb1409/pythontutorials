
import argparse

parser = argparse.ArgumentParser(description='Example program for argparse')
parser.add_argument('num1', type=int, help='first number')
parser.add_argument('num2', type=int, help='second number')
args = parser.parse_args()

print(args.num1 + args.num2)



parser = argparse.ArgumentParser(description='Example program for argparse')
parser.add_argument('--verbose', '-v', action='store_true', help='enable verbose output')
args = parser.parse_args()

if args.verbose:
    print('Verbose output enabled')
