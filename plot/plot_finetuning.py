import json
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
import argparse
from collections import defaultdict


COLORS = [
    "#797979",
    "#e0736e",
    "#a31000",
    "#81312e",
    "#b6b6b6",
    "#b47744",
    "#daa87d",
    "#000000",
    "#aaaaaa",
]


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Plot evaluation results of a finetuning experiments"
    )
    parser.add_argument(
        "--title",
        default="Evaluation",
        type=str,
        help='Title for the plot (default: "Evaluation")',
    )
    parser.add_argument(
        "--xlabel",
        default="Epoch",
        type=str,
        help='Label for the x-axis (default: "Epochs")',
    )

    parser.add_argument(
        "--metrics",
        nargs="*",
        default=("SPICE", "CIDEr", "Bleu_4"),
        type=str,
        help="List of metrics for plot. The metrics need to match the terms used in the file specified with path (default: SPICE CIDEr Bleu_4)",
    )

    parser.add_argument(
        "--path",
        type=str,
        help="The path leading to the evaluate.txt in the finetuning output folder: ../LAVIS/output/BLIP/<SUBFOLDER>/evaluate.txt",
        required=True,
    )

    return parser.parse_args()


def read_raw_validation(path: Path) -> defaultdict:
    # initialize nested dictionary
    validations = defaultdict(lambda: defaultdict(dict))
    with open(path) as file:
        data = file.read()

    data_rows = data.split("\n")

    for idx, row in enumerate(data_rows[:-1]):
        raw_validation = json.loads(row)
        for key, epoch in raw_validation.items():
            for metric, metric_value in epoch.items():
                validations[key][metric][str(idx + 1)] = metric_value

    return validations


def plot_validation(
    metrics: list,
    path: Path,
    title: str,
    xlabel: str,
):
    validations = read_raw_validation(Path(path))

    validations = {k: v for k, v in validations["val"].items() if k in metrics}

    plt.rcParams["axes.prop_cycle"] = plt.cycler(color=COLORS)

    pd.DataFrame(validations).plot()
    plt.rcParams["axes.prop_cycle"] = plt.cycler(color=COLORS)

    plt.legend(loc="upper right", bbox_to_anchor=(1.27, 1.02))
    plt.title(title)
    plt.xlabel(xlabel)
    plt.grid(color=COLORS[8], linestyle="dotted", linewidth=0.75)
    plt.savefig(path.parent.name + ".png", bbox_inches="tight", transparent=True)


if __name__ == "__main__":
    args = parse_arguments()

    plot_validation(
        path=Path(args.path),
        metrics=list(args.metrics),
        title=args.title,
        xlabel=args.xlabel,
    )
