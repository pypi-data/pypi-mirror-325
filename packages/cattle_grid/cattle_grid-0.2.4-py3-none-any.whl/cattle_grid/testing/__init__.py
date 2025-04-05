from contextlib import contextmanager

from cattle_grid.dependencies.globals import global_container


@contextmanager
def mocked_config(config):
    old_config = global_container.config

    global_container.config = config

    yield

    global_container.config = old_config
