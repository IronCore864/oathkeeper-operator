# Copyright 2024 Canonical Ltd.
# See LICENSE file for licensing details.

import pytest
from charm import OathkeeperCharm
from interface_tester import InterfaceTester
from scenario.state import State


@pytest.fixture
def interface_tester(interface_tester: InterfaceTester):
    interface_tester.configure(
        charm_type=OathkeeperCharm,
        state_template=State(
            leader=True,
            config={"dev": True},
        ),
    )
    yield interface_tester
