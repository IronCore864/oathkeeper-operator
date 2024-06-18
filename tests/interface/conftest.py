# Copyright 2024 Canonical Ltd.
# See LICENSE file for licensing details.

import pytest
from unittest.mock import patch

from interface_tester import InterfaceTester
import ops
from scenario.state import Container, ExecOutput, State

from charm import OathkeeperCharm


@pytest.fixture
def interface_tester(interface_tester: InterfaceTester):
    with patch("charm.KubernetesServicePatch"):
        interface_tester.configure(
            charm_type=OathkeeperCharm,
            state_template=State(
                leader=True,
                config={"dev": True},
                containers=[
                    Container(
                        name="oathkeeper",
                        can_connect=True,
                        layers={
                            "foo": ops.pebble.Layer({
                                "summary": "foo",
                                "description": "bar",
                                "services": {
                                    "oathkeeper": {
                                        "startup": "enabled",
                                        "current": "active",
                                        "name": "oathkeeper",
                                    }
                                },
                                "checks": {},
                            })
                        },
                    )
                ],
            ),
        )
        yield interface_tester
