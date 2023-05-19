# type: ignore

"""Tests for hls-tools

To create the test STAC items:

import json
from datetime import datetime

import rasterio.crs

import hls_tools

stac_items = hls_tools.query_hls_catalog(
    bbox=(98778, 2671477, 149203, 2704653),
    crs=rasterio.crs.CRS.from_epsg(5070),
    start_date=datetime(year=2022, month=7, day=1),
    end_date=datetime(year=2022, month=7, day=5),
)

with open("tests/test_item_collection.json", "w") as f:
    f.write(json.dumps(stac_items.to_dict(), indent=2))
"""
from datetime import datetime
from pathlib import Path

import pystac
import rasterio.crs
import xarray as xr

import hls_tools

BBOX = (98778, 2671477, 149203, 2704653)
CRS = rasterio.crs.CRS.from_epsg(5070)
START_DATE = datetime(year=2022, month=7, day=1)
END_DATE = datetime(year=2022, month=7, day=5)
TEST_ITEMS = pystac.ItemCollection.from_file(
    str(Path(__file__).parent / "test_item_collection.json")
)
RESOLUTION = 30


def test_query_hls_catalog():
    items = hls_tools.query_hls_catalog(
        bbox=BBOX,
        crs=CRS,
        start_date=START_DATE,
        end_date=END_DATE,
    )

    assert len(items) == len(TEST_ITEMS)


def test_translate_asset_keys():
    translated = hls_tools.translate_asset_keys(TEST_ITEMS)

    for item in translated:
        for key, asset in item.assets.items():
            if asset.href.endswith(".tif"):
                assert key in hls_tools.ALL_BANDS

    translated_again = hls_tools.translate_asset_keys(translated)
    assert translated_again == translated


def test_load_hls_stack():
    stack_all_bands = hls_tools.load_hls_stack(
        bbox=BBOX,
        crs=CRS,
        stac_items=hls_tools.translate_asset_keys(TEST_ITEMS),
        resolution=RESOLUTION,
    )

    assert isinstance(stack_all_bands, xr.DataArray)

    assert len(stack_all_bands.time.values) == 4

    stack_some_bands = hls_tools.load_hls_stack(
        bbox=BBOX,
        crs=CRS,
        stac_items=hls_tools.translate_asset_keys(TEST_ITEMS),
        bands=hls_tools.ALL_BANDS[:2],
        resolution=RESOLUTION,
    )

    assert len(stack_some_bands.band.values) == 2
