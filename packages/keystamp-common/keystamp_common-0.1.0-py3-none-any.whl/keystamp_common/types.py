import json
from dataclasses import asdict, dataclass
from hashlib import sha256
from typing import Dict, List, Literal, Union, Self
from urllib.parse import urlparse

JSONSerializable = Union[
    str, int, float, bool, None, List["JSONSerializable"], Dict[str, "JSONSerializable"]
]

SigningMethod = Literal["local", "official", "disabled"]

# Header policy can be:
# - "exclude" to remove all headers
# - "include" to keep all headers
# - {"include": [...], "exclude": [...]} to specify exact headers
HeaderPolicy = Union[
    Literal["exclude", "include"], Dict[Literal["include", "exclude"], List[str]]
]


@dataclass
class Transcript:
    """Transcripts reflect a single HTTP request and response.
    
    Args:
        transcript_version: The version of the transcript format (integer).
        metadata: User-supplied annotations.
        url: The URL of the request.
        request: The request as a JSON string.
        response: The response as a JSON string.
    """

    transcript_version: int
    metadata: Dict[str, JSONSerializable]
    url: str
    request: str
    response: str

    def hash_sha256(self) -> str:
        """Hash using version, metadata, and request, but not response

        The aim is to allow repeat requests to be identified by their transcript hash.
        """
        transcript_dict = self.to_dict()
        transcript_dict.pop("response")
        return sha256(json.dumps(transcript_dict, sort_keys=True).encode()).hexdigest()

    def to_dict(self) -> Dict[str, JSONSerializable]:
        return asdict(self)

@dataclass
class Signature:
    """A keystamp signature.
    
    Associated with a specific Transcript in SignedTranscript, but kept separate
    to match the underlying file format, in which signatures are stored separately
    from transcripts.

    These get passed wholesale in server response headers, so keep the keys short,
    and make sure values can be str()'ed.
    
    Args:
        version: Signing protocol version (integer).
        keypair_id: Unique ID for the keypair used to sign the transcript.
        timestamp: When the transcript was signed. ISO format with UTC timezone.
        signature: The Ed25519 signature of the transcript.
        algorithm: The algorithm used to sign the transcript.
    """
    version: int
    keypair_id: str
    timestamp: str
    signature: str
    algorithm: str

    def to_dict(self) -> Dict[str, JSONSerializable]:
        return asdict(self)

@dataclass
class SignedTranscript:
    """A transcript and a signature.

    The signature is kept separate from the underlying transcript for ease of
    verification.

    Args:
        transcript: The transcript that was signed.
        signature: The signature of the transcript.
    """
    transcript: Transcript
    signature: Signature

    def to_dict(self) -> Dict[str, JSONSerializable]:
        return asdict(self)


@dataclass
class HTTPRequest:
    url: str
    method: str
    headers: dict
    body: str # We don't parse the body

    def __post_init__(self) -> Self:
        """Quick validation of the request"""
        # Validate URL has correct scheme and domain
        assert self.url.startswith("http://") or self.url.startswith("https://"), \
            "URL must start with http:// or https://"
        parsed_url = urlparse(self.url)
        assert parsed_url.netloc, "URL must have a domain"
        
        # Validate method
        assert self.method in ["GET", "POST", "PUT", "DELETE"]
        return self


@dataclass
class HTTPResponse:
    status_code: int
    headers: dict
    body: str # We don't parse the body

    def __post_init__(self) -> Self:
        """Quick validation of the response"""
        assert isinstance(self.status_code, int)
        assert 100 <= self.status_code <= 599  # Valid HTTP status codes range
        return self

