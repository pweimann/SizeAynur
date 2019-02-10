#!/usr/bin/env python
import os
import sys
import socket

if __name__ == "__main__":
    if socket.gethostname() == "iPhone":
        os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                              "portfolio.settings.dev")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                              "portfolio.settings.production")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
