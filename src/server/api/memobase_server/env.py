"""
Initialize logger, encoder, and config.
"""

import os
from rich.logging import RichHandler
from rich import print as pprint
import yaml
import logging
import tiktoken
import dataclasses
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass
class Config:
    buffer_flush_interval: int = 60 * 60  # 1 hour
    max_chat_blob_buffer_token_size: int = 1024

    # LLM
    openai_base_url: str = None
    openai_api_key: str = None
    best_llm_model: str = "gpt-4o"
    cheap_llm_model: str = "gpt-4o-mini"
    embedding_model: str = "text-embedding-3-small"
    embedding_dim: int = 1536
    embedding_max_token_size: int = 8192

    # azure_openai_base_url: str = ""
    # azure_openai_api_key: str = ""

    @classmethod
    def load_config(cls) -> "Config":
        if not os.path.exists("config.yaml"):
            LOG.warning("No config file found, using default config")
            return cls()
        with open("config.yaml") as f:
            overwrite_config = yaml.safe_load(f)
            LOG.info(f"Load ./config.yaml")
        overwrite_config = dataclasses.replace(cls(), **overwrite_config)
        return overwrite_config


# 1. Add logger
LOG = logging.getLogger("memobase_server")
LOG.setLevel(logging.INFO)
console_handler = RichHandler()
LOG.addHandler(console_handler)

# 2. Add encoder for tokenize strings
ENCODER = tiktoken.encoding_for_model("gpt-4o")


# 3. Load config
CONFIG = Config.load_config()
LOG.info(f"{CONFIG}")
