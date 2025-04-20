"""
test_rate_limiter.py
Unit tests for rate_limiter.py
"""
from app.rate_limiter import RateLimiter
import time

def test_rate_limiter_basic():
    rl = RateLimiter(delay=0.01, batch_size=2, enabled=True)
    start = time.time()
    for _ in range(4):
        rl.request()
    elapsed = time.time() - start
    assert elapsed >= 0.01
    rl.reset()
    assert rl.request_count == 0

def test_rate_limiter_disable():
    rl = RateLimiter(delay=0.01, batch_size=2, enabled=False)
    start = time.time()
    for _ in range(4):
        rl.request()
    elapsed = time.time() - start
    assert elapsed < 0.01
