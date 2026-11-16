import argparse, sys
from .tokens import estimate_tokens, truncate_to_budget


def main(argv=None):
    p = argparse.ArgumentParser(prog="ptk", description="Prompt toolkit CLI")
    s = p.add_subparsers(dest="cmd", required=True)
    s.add_parser("count", help="Estimate tokens of stdin")
    t = s.add_parser("truncate", help="Truncate stdin to a token budget")
    t.add_argument("max_tokens", type=int)
    a = p.parse_args(argv)
    text = sys.stdin.read()
    print(estimate_tokens(text) if a.cmd == "count" else truncate_to_budget(text, a.max_tokens))


if __name__ == "__main__":
    main()
