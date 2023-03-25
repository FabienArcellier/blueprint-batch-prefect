"""
Runs a shell to run an environment and directly test flows.

Just run this module with pycharm in debug mode and set a breakpoint to be able to step through a flow.

>>> fn(main.my_favorite_function)(12)
"""
from IPython import embed

from app import main
from app.core.flow_test import fn

embed()
