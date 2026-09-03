
import pytest
import openai
from tenacity import retry, stop_after_attempt, wait_exponential

# Unit-simulated retry test (no real API call)
@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=0.5, max=4))
def flaky_fn(attempt=0):
    if attempt < 2:
        raise ConnectionError("simulated failure")
    return "ok"

def test_retry_eventually_succeeds():
    result = flaky_fn()
    assert result == "ok"

def test_retry_exhausted_raises():
    try:
        flaky_fn(attempt=3)  # force exhaustion
        assert False, "should have raised"
    except Exception:
        pytest.fail("unexpected")
