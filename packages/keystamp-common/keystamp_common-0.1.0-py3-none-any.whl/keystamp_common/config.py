"""Configuration constants for Keystamp.

Configuration exposed via .env should:

- Receive default values here where possible
- Be accessed via these variables, instead of via os.getenv(),
  so that defaults are made use of.
"""

import os
from typing import Dict, Final, List, Set

# Whitelisted endpoint domains
PROD_WHITELISTED_DOMAINS: Final[Set[str]] = {
    "api.openai.com",  # OpenAI API
    "api.anthropic.com",  # Anthropic/Claude API
    "api.cohere.ai",  # Cohere API
    "api.ai21.com",  # AI21 API
    "api-inference.huggingface.co",  # HuggingFace API
    "generativelanguage.googleapis.com",  # Google API
    "api.aleph-alpha.com",  # Aleph Alpha API
}

# Endpoint domains for local development
DEV_ONLY_WHITELISTED_DOMAINS: Final[Set[str]] = {
    "localhost",
    "127.0.0.1",
    "172.17.0.1", # Docker localhost on Linux
    "host.docker.internal", # Docker localhost on Mac
}

COMBINED_WHITELISTED_DOMAINS: Final[Set[str]] = \
    PROD_WHITELISTED_DOMAINS | DEV_ONLY_WHITELISTED_DOMAINS

# All whitelisted domains, given the environment
def get_whitelisted_domains() -> Set[str]:
    """Get the set of whitelisted domains based on environment.
    
    Returns:
        Set of whitelisted domains including development domains if in Dev environment.
    """
    if os.getenv("KEYSTAMP_ENV", "Prod") == "Dev":
        return COMBINED_WHITELISTED_DOMAINS
    return PROD_WHITELISTED_DOMAINS

# Signing server path
def get_keystamp_sign_path() -> str:
    """Get the signing server path.

    Returns:
        The signing server path.
    """
    base_path = os.getenv("KEYSTAMP_BASE_PATH", "https://api.keystamp.net")
    return f"{base_path}/sign"

# Local signing keys
DEFAULT_LOCAL_KEY_FILENAME_PEM: Final[str] = "local_key.pem"
DEFAULT_LOCAL_KEY_FILENAME_PUB: Final[str] = "local_key.pub"



# Transcript directory configuration
DEFAULT_KEYSTAMP_DIR: Final[str] = ".keystamp"
DEFAULT_LOCAL_TS_DIR: Final[str] = os.path.join(DEFAULT_KEYSTAMP_DIR, "local_transcripts")
DEFAULT_OFFICIAL_TS_DIR: Final[str] = "transcripts"

def get_transcript_dir() -> str:
    """Get the default transcript directory.

    Can be overridden by KEYSTAMP_TRANSCRIPT_DIR environment variable.

    Returns:
        Path to the default transcript directory.
    """
    return os.getenv("KEYSTAMP_TRANSCRIPT_DIR", DEFAULT_OFFICIAL_TS_DIR)


# Proxy defaults
DEFAULT_PROXY_DIR: Final[str] = os.path.join(DEFAULT_KEYSTAMP_DIR, "proxy")
DEFAULT_PROXY_HOST: Final[str] = "localhost"
DEFAULT_PROXY_PORT: Final[int] = 8080
DEFAULT_PROXY_CA_CERT_FILENAME: Final[str] = "mitmproxy-ca.pem"
DEFAULT_PROXY_SETUP_TIMEOUT_SECS: Final[float] = 10.0

# Required for the case of Lambda warm starts
KS_RELAY_OFFICIAL_TIMEOUT_SECS: Final[float] = float(os.getenv("KS_RELAY_TIMEOUT_SECS", 30.0))
