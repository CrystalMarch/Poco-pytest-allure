# coding=utf-8

from pocopytest.testcase.utils.util import *


@pytest.fixture(autouse=True)
def fix_list_scroll(request):
    poco = request.cls.poco
    click_obj(poco, UI.MAIN_START)
    click_obj(poco, UI.MENU_LISTVIEW, sleep_time=1)
