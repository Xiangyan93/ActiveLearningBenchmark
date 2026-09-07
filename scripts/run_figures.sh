#!/usr/bin/env bash
set -euo pipefail

repository_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repository_root/figures"

for notebook in \
  figure1.ipynb figure2.ipynb figure3.ipynb figure4.ipynb \
  sfigure1.ipynb sfigure2.ipynb sfigure3.ipynb sfigure4.ipynb \
  sfigure5.ipynb sfigure6.ipynb sfigure7-9.ipynb sfigure10.ipynb \
  sfigure11.ipynb sfigure12.ipynb sfigure13.ipynb; do
  jupyter nbconvert --to notebook --execute --inplace "$notebook"
done
