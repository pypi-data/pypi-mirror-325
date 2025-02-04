import argparse

from wah.train import main as train


def main():
    parser = argparse.ArgumentParser(
        prog="wah", description="Wah command-line interface."
    )
    subparsers = parser.add_subparsers(dest="command", help="Sub-commands")

    # 'train' command
    train_parser = subparsers.add_parser("train", help="Train a model")
    train_parser.add_argument(
        "--dataset",
        type=str,
        required=True,
        help="Dataset name",
    )
    train_parser.add_argument(
        "--dataset-root",
        type=str,
        required=False,
        default=".",
        help="Path to the dataset root",
    )
    train_parser.add_argument(
        "--model",
        type=str,
        required=True,
        help="Model name",
    )
    train_parser.add_argument(
        "--replace",
        type=str,
        required=False,
        default=None,
        help="Replace layer type",
    )
    train_parser.add_argument(
        "--version",
        type=str,
        required=False,
        default=None,
        help="Version name",
    )
    train_parser.add_argument(
        "--cfg-path",
        type=str,
        required=True,
        help="Path to the config file",
    )
    train_parser.add_argument(
        "--log-root",
        type=str,
        required=False,
        default="./logs",
        help="Path to the log root",
    )
    train_parser.add_argument(
        "--resume",
        action="store_true",
        default=False,
        help="Resume training",
    )

    args = parser.parse_args()

    if args.command == "train":
        train(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
