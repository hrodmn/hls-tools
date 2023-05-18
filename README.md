# hls-tools
Python package to help work with the Harmonized Landsat Sentinel 2 remote sensing dataset.

## Development

Create a virtual environment
```sh
python3 -m venv env
source env/bin/activate
```

```sh
git clone https://github.com/hrodmn/water_quality.git
cd water_quality
pip install -e .["test","dev"]
```

Linting and formatting are handled with [pre-commit](https://pre-commit.com/).
You will need to install pre-commit before committing any changes:
```sh
pre-commit install
```
