import re
import simple_utils


def test_get_uuid():
    assert simple_utils.random.get_uuid() != simple_utils.random.get_uuid()

def test_make_uuid_including_time():
    assert simple_utils.random.make_uuid_including_time() != simple_utils.random.make_uuid_including_time()
