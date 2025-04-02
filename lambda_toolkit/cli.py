
# Standard library imports
import argparse  # noqa: I001

# Local application imports
from lambda_toolkit.registry import lookup, list_definitions, expression_registry
from lambda_toolkit.examplegen import generate_example_trace
from lambda_toolkit.core import reduce_lambda_verbose, pretty_improved
from lambda_toolkit.multiapply import apply_operator
from lambda_toolkit.nodes import Var, Abs, App
from lambda_toolkit.registry import define
from lambda_toolkit.parser import parse_lambda

# Inject standard definitions
define("TRUE", Abs(Abs(Var(1))))
define("FALSE", Abs(Abs(Var(0))))
define("ID", Abs(Var(0)))
define("DIVERGING", Abs(App(Var(0), Var(0))))
define("ID_APP", Abs(App(Var(1), Var(0))))  # λx. (ID x)
define("IF", Abs(Abs(Abs(App(App(Var(2), Var(1)), Var(0))))), lazy_args=[False, True, True])  # noqa: E501

def setup_commands(subparsers):
    # parse
    prs = subparsers.add_parser("parse", help="Parse a lambda expression from string")
    prs.add_argument("source", type=str, help="Lambda expression in source form")
    prs.add_argument("--pretty", "-p", action="store_true", help="Pretty print the parsed AST")  # noqa: E501
    prs.set_defaults(func=run_parse)

    # generate-example
    gen = subparsers.add_parser("generate-example", help="Generate reduction trace and write to file")  # noqa: E501
    gen.add_argument("name", help="Registered combinator name")
    gen.add_argument("args", nargs="+", help="Argument names")
    gen.add_argument("--output", "-o", required=True, help="Output file for trace")
    gen.add_argument("--strategy", "-s", default="lazy", choices=["lazy", "eager"], help="Evaluation strategy")  # noqa: E501
    gen.add_argument("--eta", action="store_true", help="Enable eta-reduction")
    gen.set_defaults(func=run_generate_example)

    # list
    lst = subparsers.add_parser("list", help="List all registered expressions")
    lst.set_defaults(func=run_list)

    # show
    shw = subparsers.add_parser("show", help="Show a registered expression")
    shw.add_argument("name", help="Registered expression name")
    shw.set_defaults(func=show_expression)

    # evaluate
    evl = subparsers.add_parser("evaluate", help="Evaluate expression and print result")
    evl.add_argument("name", help="Combinator to apply")
    evl.add_argument("args", nargs="*", help="Argument names")
    evl.add_argument("--strategy", "-s", default="lazy", choices=["lazy", "eager"], help="Evaluation strategy")  # noqa: E501
    evl.add_argument("--eta", action="store_true", help="Enable eta-reduction")
    evl.add_argument("--trace", action="store_true", help="Show reduction steps")
    evl.set_defaults(func=run_evaluate)

    # eval (alias)
    eval_alias = subparsers.add_parser("eval", help="Alias for evaluate")
    eval_alias.add_argument("name", help="Combinator to apply")
    eval_alias.add_argument("args", nargs="*", help="Argument names")
    eval_alias.add_argument("--strategy", "-s", default="lazy", choices=["lazy", "eager"], help="Evaluation strategy")  # noqa: E501
    eval_alias.add_argument("--eta", action="store_true", help="Enable eta-reduction")
    eval_alias.add_argument("--trace", action="store_true", help="Show reduction steps")
    eval_alias.set_defaults(func=run_evaluate)

    # monday
    mnd = subparsers.add_parser("monday", help="Garfield's eternal suffering")
    mnd.set_defaults(func=lambda args: print(GARFIELD_ASCII))

    # crowbar
    cwb = subparsers.add_parser("crowbar", help="Trusty hardware")
    cwb.set_defaults(func=lambda args: print(CROWBAR_ASCII))

def run_parse(args):
    parsed = parse_lambda(args.source)
    if args.pretty:
        print(pretty_improved(parsed))
    else:
        print(parsed)

def run_generate_example(args):
    expr_args = [lookup(name) for name in args.args]
    generate_example_trace(
        args.name, expr_args,
        args.output,
        strategy=args.strategy,
        eta=args.eta
    )

def run_list(args):
    print("Registered expressions:")
    for name in list_definitions():
        entry = expression_registry[name]
        lazy_args = entry.get("lazy_args", [])
        print(f"- {name} (lazy_args={lazy_args})")

def show_expression(args):
    expr = lookup(args.name)
    print(f"Expression `{args.name}`:")
    print(pretty_improved(expr))

def run_evaluate(args):
    expr_args = [lookup(name) for name in args.args]
    result = apply_operator(args.name, expr_args, strategy=args.strategy)
    steps = reduce_lambda_verbose(
        result,
        max_steps=10,
        strategy=args.strategy,
        eta=args.eta
    )

    if args.trace:
        for i, (_info, state) in enumerate(steps):
            print(f"Step {i}: {pretty_improved(state)}")

    reduced = steps[-1][1]

    print("Final Result:")
    print(pretty_improved(reduced))

from lambda_toolkit.easter_egg import GARFIELD_ASCII  # noqa: E402, I001
def ihatemondays():
    print(GARFIELD_ASCII)

from lambda_toolkit.easter_egg import CROWBAR_ASCII  # noqa: E402, I001
def crowbar():
    print(CROWBAR_ASCII)

def main():
    parser = argparse.ArgumentParser(description="Lambda Toolkit CLI")
    subparsers = parser.add_subparsers(dest="command")
    setup_commands(subparsers)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()
    
    # Show subcommand help if no args were passed
    if not hasattr(args, "func"):
        parser.print_help()
        return
    
    if args.command == "help":
        parser.print_help()
        return

if __name__ == "__main__":
    main()