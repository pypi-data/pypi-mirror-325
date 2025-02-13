"""Gecko REQRM/RMREQ handlers"""

from __future__ import annotations

import logging
import struct
from enum import IntEnum

from ...config import GeckoConfig
from .packet import GeckoPacketProtocolHandler

REQRM_VERB = b"REQRM"
RMREQ_VERB = b"RMREQ"

RESPONSE_FORMAT = ">BBB"

_LOGGER = logging.getLogger(__name__)


class GeckoReminderType(IntEnum):
    INVALID = 0
    RINSE_FILTER = 1
    CLEAN_FILTER = 2
    CHANGE_WATER = 3
    CHECK_SPA = 4
    CHANGE_OZONATOR = 5
    CHANGE_VISION_CARTRIDGE = 6

    @staticmethod
    def to_string(type: GeckoReminderType) -> str:
        if type == GeckoReminderType.INVALID:
            return "Invalid"
        if type == GeckoReminderType.RINSE_FILTER:
            return "RinseFilter"
        if type == GeckoReminderType.CLEAN_FILTER:
            return "CleanFilter"
        if type == GeckoReminderType.CHANGE_WATER:
            return "ChangeWater"
        if type == GeckoReminderType.CHECK_SPA:
            return "CheckSpa"
        if type == GeckoReminderType.CHANGE_OZONATOR:
            return "ChangeOzonator"
        if type == GeckoReminderType.CHANGE_VISION_CARTRIDGE:
            return "ChangeVisionCartridge"
        # Technically unreachable code here
        return "Unhandled"


class GeckoRemindersProtocolHandler(GeckoPacketProtocolHandler):
    @staticmethod
    def request(seq, **kwargs):
        return GeckoRemindersProtocolHandler(
            content=b"".join([REQRM_VERB, struct.pack(">B", seq)]),
            timeout=GeckoConfig.PROTOCOL_TIMEOUT_IN_SECONDS,
            retry_count=GeckoConfig.PROTOCOL_RETRY_COUNT,
            on_retry_failed=GeckoPacketProtocolHandler._default_retry_failed_handler,
            **kwargs,
        )

    @staticmethod
    def response(reminders: list[tuple[GeckoReminderType, int]], **kwargs):
        return GeckoRemindersProtocolHandler(
            content=b"".join(
                [RMREQ_VERB]
                + [
                    struct.pack("<BhB", reminder[0], reminder[1], 1)
                    for reminder in reminders
                ]
            ),
            **kwargs,
        )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.reminders: list[tuple[GeckoReminderType, ...]] = []

    def can_handle(self, received_bytes: bytes, sender: tuple) -> bool:
        return received_bytes.startswith(REQRM_VERB) or received_bytes.startswith(
            RMREQ_VERB
        )

    def handle(self, received_bytes: bytes, sender: tuple):
        remainder = received_bytes[5:]
        if received_bytes.startswith(REQRM_VERB):
            self._sequence = struct.unpack(">B", remainder[0:1])[0]
            return  # Stay in the handler list

        # Otherwise must be RMREQ
        rest = remainder
        while len(rest) > 0:
            (t, days, _push, rest) = struct.unpack(f"<BhB{len(rest) - 4}s", rest)
            try:
                self.reminders.append(tuple((GeckoReminderType(t), days)))
            except ValueError:
                _LOGGER.warning("Cannot use %d as reminder type, ignored", t)

        self._should_remove_handler = True
