import argparse
from pixel_lab_viewer.core import build_snapshot


def main() -> None:
    parser = argparse.ArgumentParser(description="Desktop image inspection utilities for microscopy-like frames and manual annotation drills.")
    parser.add_argument("--summary", action="store_true")
    args = parser.parse_args()
    if args.summary:
        print(build_snapshot())


if __name__ == "__main__":
    main()
