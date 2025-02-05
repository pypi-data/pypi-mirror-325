import unittest
from src.DLMS_SPODES.types import cdt, cst, ut
from src.DLMS_SPODES.cosem_interface_classes import collection
from src.DLMS_SPODES.cosem_interface_classes import activity_calendar
from src.DLMS_SPODES.cosem_interface_classes.overview import ClassID, Version
from src.DLMS_SPODES import exceptions as exc
from src.DLMS_SPODES.cosem_interface_classes.special_days_table import SpecDayEntry
from datetime import date


class TestType(unittest.TestCase):

    def test_Sde(self):
        dt = date(2045, 1, 23)
        data = SpecDayEntry((None, cst.OctetStringDate(dt), None))
        print(data)