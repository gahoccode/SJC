"""
rate_limiter.py
Implements API rate limiting logic and monitoring.
"""
import time
import streamlit as st
class RateLimiter:
    def __init__(self, delay: float = 1.0, batch_size: int = 1, enabled: bool = True):
        self.delay = delay
        self.batch_size = batch_size
        self.enabled = enabled
        self.request_count = 0

    def request(self):
        if not self.enabled:
            return
        self.request_count += 1
        if self.request_count % self.batch_size == 0:
            time.sleep(self.delay)

    def reset(self):
        self.request_count = 0

    def set_params(self, delay: float, batch_size: int, enabled: bool):
        self.delay = delay
        self.batch_size = batch_size
        self.enabled = enabled

    def monitor(self):
        st.progress(self.request_count % self.batch_size / self.batch_size)
        if self.request_count % self.batch_size == 0:
            st.warning("Approaching API rate limit!")
