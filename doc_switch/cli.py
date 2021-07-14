"""Console script for doc_switch."""
import sys
import click


@click.command()
@click.argument("files", type=click.Path(exists=True), nargs=-1)
def main(files):
    """Console script for doc_switch."""
    for file in files:
        with open(file) as f:
            print(f.read())
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
