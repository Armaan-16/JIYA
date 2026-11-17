"""
============================================================
JIYA AI Operating System
Module: Memory Service (ChromaDB + Qwen3-Embedding:4b on CPU)
Purpose: Long-term episodic and semantic vector memory for JIYA.
         Embeddings are pinned strictly to CPU (num_gpu: 0) to ensure
         100% of GPU VRAM is reserved for LLM generation.
Author: Armaan Mishra
============================================================
"""

import os
import json
import logging
import warnings
import uuid
import urllib.request
from typing import List, Union, Any, Sequence

# Suppress noisy library logs
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['TOKENIZERS_PARALLELISM'] = 'false'
os.environ['ONNXRUNTIME_EXECUTION_PROVIDERS'] = 'CPUExecutionProvider'

logging.getLogger('chromadb').setLevel(logging.ERROR)
warnings.filterwarnings('ignore')

try:
    import chromadb
    BaseEF = chromadb.EmbeddingFunction
    CHROMADB_AVAILABLE = True
except (ImportError, AttributeError):
    BaseEF = object  # type: ignore
    chromadb = None  # type: ignore
    CHROMADB_AVAILABLE = False


class CpuOllamaEmbeddingFunction(BaseEF):
    """
    Embedding function that queries Ollama's /api/embed endpoint with
    explicit CPU execution (num_gpu: 0).
    Guarantees that vector search never competes with the LLM for GPU VRAM.
    """

    def __init__(self, url: str = "http://localhost:11434/api/embed", model_name: str = "qwen3-embedding:4b"):
        self.url = url
        self.model_name = model_name

    def name(self) -> str:
        return "ollama"

    def __call__(self, input: Any) -> Any:
        texts = [input] if isinstance(input, str) else list(input)
        if not texts:
            return []

        try:
            req_data = json.dumps({
                "model": self.model_name,
                "input": texts,
                "options": {"num_gpu": 0}  # Pin to CPU!
            }).encode("utf-8")

            req = urllib.request.Request(
                self.url,
                data=req_data,
                headers={"Content-Type": "application/json"}
            )

            with urllib.request.urlopen(req, timeout=15) as response:
                result = json.loads(response.read().decode("utf-8"))
                return result.get("embeddings", [])
        except Exception as e:
            # Fallback to empty embeddings rather than crashing
            print(f"[MEMORY WARNING] CPU embedding call failed: {e}")
            return [[0.0] * 2560 for _ in texts]


class MemoryService:
    """Long-term vector memory service powered by ChromaDB and CPU-isolated Ollama embeddings."""

    def __init__(self, db_path: str = "./JIYA_MEMORY"):
        os.makedirs(db_path, exist_ok=True)
        self.db_path = db_path
        self.is_ready = False

        if not CHROMADB_AVAILABLE:
            print("[WARNING] ChromaDB not installed. Vector memory disabled.")
            return

        try:
            self.client = chromadb.PersistentClient(path=db_path)
            self.embedding_function = CpuOllamaEmbeddingFunction(
                url="http://localhost:11434/api/embed",
                model_name="qwen3-embedding:4b"
            )
            self.collection = self.client.get_or_create_collection(
                name="jiya_long_term_memory",
                embedding_function=self.embedding_function,  # type: ignore
                metadata={"hnsw:space": "cosine"}
            )
            self.is_ready = True
        except Exception as e:
            print(f"[WARNING] Could not initialize ChromaDB vector memory: {e}")
            self.client = None
            self.collection = None

    def save_memory(self, content: str, source: str = "conversation") -> str:
        """Stores a textual memory entry along with metadata into vector storage."""
        memory_id = str(uuid.uuid4())
        if not self.is_ready or not self.collection:
            return memory_id

        try:
            self.collection.add(
                documents=[content],
                metadatas=[{"source": source}],
                ids=[memory_id]
            )
        except Exception as e:
            print(f"[ERROR] Failed to save memory: {e}")
        return memory_id

    def recall(self, query: str, n_results: int = 3) -> List[str]:
        """Retrieves top semantically relevant memories matching the query."""
        if not self.is_ready or not self.collection:
            return []

        try:
            total = self.collection.count()
            if total == 0:
                return []

            results = self.collection.query(
                query_texts=[query],
                n_results=min(n_results, total)
            )

            if results and 'documents' in results and results['documents']:
                return results['documents'][0]
        except Exception as e:
            print(f"[ERROR] Failed to recall memories: {e}")

        return []

    def clear_all(self) -> None:
        """Wipes the entire vector memory collection."""
        if not self.is_ready or not self.client:
            print(">>> [SYSTEM] Memory service is not active. <<<")
            return

        try:
            self.client.delete_collection(name="jiya_long_term_memory")
            self.collection = self.client.get_or_create_collection(
                name="jiya_long_term_memory",
                embedding_function=self.embedding_function,  # type: ignore
                metadata={"hnsw:space": "cosine"}
            )
            print(">>> [SYSTEM] All ChromaDB memories wiped successfully. <<<")
        except Exception as e:
            print(f">>> [ERROR] Failed to wipe memory: {e} <<<")
