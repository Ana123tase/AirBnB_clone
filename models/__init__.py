#!/usr/bin/python3
"""The magic method of  models-__init__"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
