# Copyright 2024 Canonical Ltd.
# See LICENSE file for licensing details.

import pytest
from unittest.mock import patch

from interface_tester import InterfaceTester
from scenario.state import State

from charm import OathkeeperCharm


@pytest.fixture
def interface_tester(interface_tester: InterfaceTester):
    with patch("charm.KubernetesServicePatch", lambda x, y: None):
        interface_tester.configure(
            charm_type=OathkeeperCharm,
            state_template=State(
                leader=True,
                config={"dev": True},
            ),
        )
        yield interface_tester
