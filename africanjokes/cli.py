import argparse
import africanjokes

VERSION = "1.0.0"  # Update as needed

def main():
    parser = argparse.ArgumentParser(
        description="Get a random African joke from the CLI!"
    )
    parser.add_argument(
        "--joke", "-j", action="store_true", help="Show a random African joke"
    )
    parser.add_argument(
        "--version", "-v", action="store_true", help="Show version info"
    )

    args = parser.parse_args()

    if args.joke:
        print(africanjokes.get_joke())
    elif args.version:
        print(f"africanjokes version {VERSION}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()