# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CERN.
# Copyright (C) 2020 Northwestern University.
#
# Invenio-Drafts-Resources is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Invenio Drafts Resources module to create REST APIs."""

from .drafts import DraftActionResource, DraftActionResourceConfig, \
    DraftLinksSchema, DraftResource, DraftResourceConfig, \
    DraftVersionResource, DraftVersionResourceConfig
from .records import RecordResource, RecordResourceConfig
from .userrecords import UserRecordsResource
from .userrecords_config import UserRecordsResourceConfig

__all__ = (
    "DraftActionResource",
    "DraftActionResourceConfig",
    "DraftLinksSchema",
    "DraftResource",
    "DraftResourceConfig",
    "DraftVersionResource",
    "DrafVersiontResourceConfig",
    "RecordResource",
    "RecordResourceConfig",
    "UserRecordsResource",
    "UserRecordsResourceConfig",
)
