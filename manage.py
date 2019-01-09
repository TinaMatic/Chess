#!/usr/bin/env python
import os
import sys

from django.shortcuts import render
import webbrowser



def board(request):
    #Render the HTML template board.html
    return render(request, 'board.html')


if __name__ == '__main__':

    webbrowser.open_new_tab('C:/Users/matin/PycharmProjects/NewChess/templates/board.html')

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewChess.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
