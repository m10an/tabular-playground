import json
import pandas as pd
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split

from tblr.models import ConstantModel
from tblr.utils import AnnotatedArgumentParser


class Args:
    train: str
    test_size: int
    const: float
    seed: int
    output_scores: str


def main():
    parser = AnnotatedArgumentParser(Args)
    args: Args = parser.parse_args()

    # Load in the data
    x_full = pd.read_csv(args.train)
    y_full = x_full.pop('claim')
    x_train, x_test, y_train, y_test = train_test_split(x_full, y_full,
                                                        test_size=args.test_size,
                                                        random_state=args.seed)

    model = ConstantModel(constant=args.const)
    model.train(x_train, y_train)

    y_pred = model.predict(x_test)
    scores = {
        'roc_auc': roc_auc_score(y_test, y_pred)
    }
    with open(args.output_scores, 'w') as f:
        json.dump(scores, f)


if __name__ == 'main':
    main()
