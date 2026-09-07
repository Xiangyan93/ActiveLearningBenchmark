#!/usr/bin/env python3
"""Verify that all processed tables required by the figure notebooks exist."""

from pathlib import Path


REQUIRED_FILES = (
    'results_summary_classification_exploitive.csv',
    'results_summary_classification_explorative.csv',
    'results_summary_regression_exploitive.csv',
    'results_summary_regression_explorative.csv',
    'al.csv',
    'cv.csv',
    'yol.csv',
    'al_cv_corr.csv',
    'al_se_corr.csv',
)


def main() -> int:
    processed_dir = Path(__file__).resolve().parents[1] / 'data' / 'processed'
    missing = [name for name in REQUIRED_FILES if not (processed_dir / name).is_file()]
    if missing:
        print('Missing processed source-data files:')
        for name in missing:
            print(f'  - {name}')
        print('Download the companion Zenodo archive and unpack it into data/processed/.')
        return 1
    print(f'All {len(REQUIRED_FILES)} processed source-data files are present.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
