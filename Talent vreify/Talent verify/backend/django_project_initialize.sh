#!/bin/bash

django-admin startproject talent_verify
cd talent_verify || exit
django-admin startapp company
django-admin startapp employee
