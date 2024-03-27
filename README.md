# hls-tools
Python package with convenience functions for accessing and loading the Harmonized Landsat Sentinel 2 remote sensing dataset into `xarray.DataArray` format.

## Installation
You can install the package from pypi using pip:
```sh 
pip install hls_tools
```

## Development

```sh
git clone https://github.com/hrodmn/hls-tools.git
cd hls-tools
```

Create a virtual environment
```sh
python3 -m venv env
source env/bin/activate
```

Install test/dev dependencies
```sh
pip install -e .["test","dev"]
```

Linting and formatting are handled with [pre-commit](https://pre-commit.com/).
You will need to install pre-commit before committing any changes:
```sh
pre-commit install
```
