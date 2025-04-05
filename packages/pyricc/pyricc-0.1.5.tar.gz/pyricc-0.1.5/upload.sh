#!/bin/bash

yellow "Try for verbsoity: python -m twine  upload dist/* --verbose"
python -m twine  upload dist/*
