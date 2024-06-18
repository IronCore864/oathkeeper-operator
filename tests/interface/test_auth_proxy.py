# Copyright 2024 Canonical Ltd.
# See LICENSE file for licensing details.

from interface_tester import InterfaceTester


def test_auth_proxy_v0_interface(interface_tester: InterfaceTester):
    interface_tester.configure(
        interface_name="auth_proxy",
        interface_version=0,
    )
    interface_tester.run()
