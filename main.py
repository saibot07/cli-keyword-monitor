import argparse

def main():
    parser = argparse.ArgumentParser(description="CLI Keyword Monitor")
    parser.add_argument("keywords", nargs="+", help="List of keywords to monitor")
    parser.add_argument("--frequency", type=int, default=5, help="Frequency in seconds (default: 5 seconds)")

    args = parser.parse_args()

    if not args.keywords:
        parser.error("The following arguments are required: keywords")

    print(f"Monitoring keywords: {args.keywords} with a frequency of {args.frequency} seconds")

if __name__ == "__main__":
    main()
