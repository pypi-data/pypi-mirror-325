from collections import defaultdict
import threading


class MetricsCollector:
    def __init__(self):
        self._metrics = defaultdict(int)
        self._response_times = []
        self._lock = threading.Lock()

    def increment(self, metric: str, value: int = 1):
        with self._lock:
            self._metrics[metric] += value

    def record_response_time(self, duration: float):
        with self._lock:
            self._response_times.append(duration)

    def get_metrics(self):
        with self._lock:
            avg_response_time = (
                sum(self._response_times) / len(self._response_times)
                if self._response_times
                else 0
            )
            return {
                "total_requests": self._metrics["requests"],
                "total_errors": self._metrics["errors"],
                "average_response_time": round(avg_response_time, 3),
                "requests_per_endpoint": dict(self._metrics["endpoints"]),
            }
