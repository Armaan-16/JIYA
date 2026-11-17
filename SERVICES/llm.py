"""
============================================================
JIYA AI Operating System
Module: LLM Service (Facade)
============================================================
"""
import time
from BRAIN.cortex_router import ProviderManager


class LLMService:

    def __init__(self):
        self.provider = ProviderManager()

    def generate(self, request):
        start = time.perf_counter()
        response = self.provider.generate(request)
        response.latency = time.perf_counter() - start
        return response

    def generate_stream(self, request):
        return self.provider.generate_stream(request)