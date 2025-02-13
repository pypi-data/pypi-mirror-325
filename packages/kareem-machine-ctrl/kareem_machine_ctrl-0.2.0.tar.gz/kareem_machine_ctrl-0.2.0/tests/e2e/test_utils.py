"""Test utilities for E2E tests."""
import time
from typing import List, Dict

class TestMetrics:
    """Class for tracking test performance metrics."""
    
    def __init__(self):
        """Initialize test metrics."""
        self.start_time = 0.0
        self.end_time = 0.0
        self.response_times: List[float] = []
        self.successes = 0
        self.failures = 0
        self.error_messages: List[str] = []
        
    def start(self):
        """Start timing the test."""
        self.start_time = time.time()
        
    def end(self):
        """End timing the test."""
        self.end_time = time.time()
        
    def add_response_time(self, response_time: float):
        """Add a response time measurement."""
        self.response_times.append(response_time)
        
    def add_success(self):
        """Increment success counter."""
        self.successes += 1
        
    def add_failure(self, error_msg: str):
        """Increment failure counter and store error message."""
        self.failures += 1
        self.error_messages.append(error_msg)
        
    def get_summary(self) -> Dict:
        """Get summary of test metrics."""
        total_time = self.end_time - self.start_time
        avg_response_time = sum(self.response_times) / len(self.response_times) if self.response_times else 0
        max_response_time = max(self.response_times) if self.response_times else 0
        
        return {
            "total_time": total_time,
            "average_response_time_ms": avg_response_time,
            "max_response_time_ms": max_response_time,
            "successes": self.successes,
            "failures": self.failures,
            "error_messages": self.error_messages,
            "total_requests": len(self.response_times)
        } 