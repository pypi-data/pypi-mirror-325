"""Unit tests for the actual snapshots."""

import pathlib
from unittest import IsolatedAsyncioTestCase, main

from context import (
    GeckoAsyncFacade,
    GeckoAsyncStructure,
    GeckoAsyncTaskMan,
    GeckoSnapshot,
)


class GeckoAsyncSpa:
    """Mock spa for testing."""

    def __init__(self, snapshotfile):
        self.struct = GeckoAsyncStructure(None)

        cwd = pathlib.Path(__file__).parent.resolve()
        snapshots = GeckoSnapshot.parse_log_file(f"{cwd}/{snapshotfile}")
        assert len(snapshots) == 1

        snapshot = snapshots[0]
        self.struct.replace_status_block_segment(0, snapshot.bytes)

        # Attempt to get config and log classes
        self.plateform_key = snapshot.packtype.lower()
        self.config_version = snapshot.config_version
        self.log_version = snapshot.log_version

    @property
    def accessors(self):
        return self.struct.accessors

    async def async_init(self) -> None:
        """Init async."""
        await self.struct.load_pack_class(self.plateform_key)
        await self.struct.load_config_module(self.config_version)
        await self.struct.load_log_module(self.log_version)
        self.struct.build_accessors()


class TestSnapshots(IsolatedAsyncioTestCase):
    """Test all the snapshots."""

    def setUp(self) -> None:
        self.taskman = GeckoAsyncTaskMan()

    async def asyncSetUp(self) -> None:
        await self.taskman.__aenter__()

    async def asyncTearDown(self) -> None:
        await self.taskman.__aexit__(None)

    def tearDown(self) -> None:
        del self.taskman

    async def build_facade(self, snapshotfile) -> GeckoAsyncFacade:
        spa = GeckoAsyncSpa(snapshotfile)
        await spa.async_init()
        return GeckoAsyncFacade(spa, self.taskman)

    async def test_default(self) -> None:
        facade = await self.build_facade("snapshots/default.snapshot")
        self.assertListEqual(
            ["P1", "P2", "BL", "LI"],
            [device["device"] for device in facade.actual_user_devices],
        )
        self.assertFalse(facade.pumps[0].is_on)
        self.assertFalse(facade.pumps[1].is_on)
        self.assertFalse(facade.blowers[0].is_on)
        self.assertFalse(facade.lights[0].is_on)
        self.assertEqual(39.0, facade.water_heater.current_temperature)
        self.assertEqual("°C", facade.water_heater.temperature_unit)

    async def test_inYT_Pump1Low(self) -> None:  # noqa: N802
        facade = await self.build_facade(
            "snapshots/inYT-Pump1Lo-2020-12-13 11_19_35.snapshot"
        )
        self.assertListEqual(
            ["P1", "P2", "LI"],
            [device["device"] for device in facade.actual_user_devices],
        )
        self.assertEqual("LOW", facade.pumps[0].mode)
        self.assertEqual("OFF", facade.pumps[1].mode)
        self.assertTrue(facade.pumps[0].is_on)
        self.assertFalse(facade.pumps[1].is_on)
        self.assertTrue(facade.lights[0].is_on)
        self.assertEqual(70.0, facade.water_heater.current_temperature)
        self.assertEqual("°F", facade.water_heater.temperature_unit)

    async def test_inYT_Pump1High(self) -> None:  # noqa: N802
        facade = await self.build_facade(
            "snapshots/inYT-Pump1Hi-2020-12-13 11_19_35.snapshot"
        )
        self.assertListEqual(
            ["P1", "P2", "LI"],
            [device["device"] for device in facade.actual_user_devices],
        )
        self.assertEqual("HIGH", facade.pumps[0].mode)
        self.assertEqual("OFF", facade.pumps[1].mode)
        self.assertTrue(facade.pumps[0].is_on)
        self.assertFalse(facade.pumps[1].is_on)
        self.assertTrue(facade.lights[0].is_on)
        self.assertEqual(70.0, facade.water_heater.current_temperature)
        self.assertEqual("°F", facade.water_heater.temperature_unit)

    async def test_inYT_WaterFall_On(self) -> None:  # noqa: N802
        facade = await self.build_facade(
            "snapshots/inYT-waterfall on-2020-10-23 18_01_30.snapshot"
        )
        self.assertListEqual(
            ["P1", "P2", "Waterfall", "LI"],
            [device["device"] for device in facade.actual_user_devices],
        )
        self.assertEqual("OFF", facade.pumps[0].mode)
        self.assertEqual("OFF", facade.pumps[1].mode)
        self.assertEqual("ON", facade.pumps[2].mode)
        self.assertFalse(facade.pumps[0].is_on)
        self.assertFalse(facade.pumps[1].is_on)
        self.assertFalse(facade.lights[0].is_on)
        self.assertEqual(37.0, facade.water_heater.current_temperature)
        self.assertEqual("°C", facade.water_heater.temperature_unit)

    async def test_inYJ_All_Off(self) -> None:  # noqa: N802
        facade = await self.build_facade(
            "snapshots/inYJ-All off-2020-12-18 11_24_09.snapshot"
        )
        self.assertListEqual(
            ["P1", "LI"],
            [device["device"] for device in facade.actual_user_devices],
        )
        self.assertEqual("OFF", facade.pumps[0].mode)
        self.assertFalse(facade.pumps[0].is_on)
        self.assertFalse(facade.lights[0].is_on)
        self.assertEqual(37.0, facade.water_heater.current_temperature)
        self.assertEqual("°C", facade.water_heater.temperature_unit)
        print(facade.all_user_devices)


if __name__ == "__main__":
    main()
