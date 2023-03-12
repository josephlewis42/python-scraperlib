#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 nu

import base64
import pathlib

ROOT_DIR = pathlib.Path(__file__).parent
NAME = pathlib.Path(__file__).parent.name
with open(ROOT_DIR.joinpath("VERSION"), "r") as fh:
    VERSION = fh.read().strip()
SCRAPER = f"{NAME} {VERSION}"

UTF8 = "UTF-8"

# list of Image formats witout Alpha Channel support
ALPHA_NOT_SUPPORTED = ["JPEG", "BMP", "EPS", "PCX"]

# list of mimetypes we consider articles using it should default to FRONT_ARTICLE
FRONT_ARTICLE_MIMETYPES = ["text/html"]

# list of mandatory meta tags of the zim file.
MANDATORY_ZIM_METADATA_KEYS = [
    "Name",
    "Title",
    "Creator",
    "Publisher",
    "Date",
    "Description",
    "Language",
    "Illustration_48x48@1",
]

DEFAULT_DEV_ZIM_METADATA = {
    "Name": "Test Name",
    "Title": "Test Title",
    "Creator": "Test Creator",
    "Publisher": "Test Publisher",
    "Date": "2023-01-01",
    "Description": "Test Description",
    "Language": "fra",
    "Illustration_48x48_at_1": base64.b64decode(
        "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAAGXRFWHRTb2Z0d2FyZQBB"
        "ZG9iZSBJbWFnZVJlYWR5ccllPAAAAA9JREFUeNpi+P//P0CAAQAF/gL+Lc6J7gAAAABJ"
        "RU5ErkJggg=="
    ),
}
