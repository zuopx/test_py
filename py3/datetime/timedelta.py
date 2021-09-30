import datetime
import time
import pytest


if __name__ == "__main__":
    prefix = __file__ + "::"
    case = "test_total_second"
    pytest.main([prefix + case + "-s"])
