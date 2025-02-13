from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import Any, AsyncIterator, Dict, Optional, Union

from .versions import TRANSCRIPT_VERSION
from .types import Transcript, HTTPRequest, HTTPResponse

# Breaking this dependency on mitmproxy types, so common doesn't need this import
Request = Any
Response = Any

def transcript_from_message_pair(
    request: Request,
    response: Response,
) -> Transcript:
    """Extract transcript components from a request / response pair."""

    transcript = Transcript(
        transcript_version=TRANSCRIPT_VERSION,
        metadata={},
        url=str(request.url),
        request=request.content.decode("utf-8") if request.content else "",
        response=response.content.decode("utf-8") if response.content else "",
    )

    return transcript

def transcript_from_message_pair_commontypes(
    request: HTTPRequest,
    response: HTTPResponse,
) -> Transcript:
    """Extract transcript components from a request / response pair."""

    transcript = Transcript(
        transcript_version=TRANSCRIPT_VERSION,
        metadata={},
        url=request.url,
        request=request.body,
        response=response.body,
    )

    return transcript



class SigningError(Exception):
    """Base class for signing-related exceptions."""

    pass


class InvalidAPIKey(SigningError):
    """Raised when the Keystamp API key is invalid."""

    pass


class ProxyError(SigningError):
    """Raised when there's an error proxying the request."""

    pass


class SignatureError(SigningError):
    """Raised when there's an error signing or verifying a response."""

    pass


@dataclass
class ProxyRequest:
    """Represents an HTTP request to be proxied and signed."""

    method: str
    url: str
    headers: Dict[str, str]
    body: Optional[Union[bytes, AsyncIterator[bytes]]] = None


@dataclass
class ProxyResponse:
    """Represents a signed HTTP response."""

    status_code: int
    headers: Dict[str, str]
    body: Union[bytes, AsyncIterator[bytes]]
    signature: str
    timestamp: datetime


class SigningServer(ABC):
    """Abstract base class for a proxy-based signing server.

    This server acts as a proxy that:
    1. Receives HTTP requests from the local Keystamp proxy
    2. Validates the Keystamp API key in request headers
    3. Makes the actual request to the target API
    4. Signs the response
    5. Returns the signed response

    Raises:
        ProxySetupError: If there's an error starting or stopping the proxy
        ProxyError: If there's an error proxying the request
        InvalidAPIKey: If the Keystamp API key is invalid or missing
        SignatureError: If there's an error signing the response
    """

    @abstractmethod
    def start(self, port: int) -> None:
        """Start the signing server.

        The server will set os.environ["HTTPS_PROXY"] and os.environ["HTTP_PROXY"]
        to the signing server's URL.

        Args:
            port: The port to listen on for incoming requests

        Raises:
            ProxySetupError: If there's an error starting the proxy
        """
        pass

    @abstractmethod
    def stop(self) -> None:
        """Stop the signing server.

        The server will restore os.environ["HTTPS_PROXY"] and os.environ["HTTP_PROXY"]
        to their original values.

        Raises:
            ProxySetupError: If there's an error stopping the proxy
        """
        pass

    @abstractmethod
    async def proxy_request(self, request: ProxyRequest) -> ProxyResponse:
        """Proxy and sign an HTTP request.

        This method should:
        1. Validate the Keystamp API key in request headers
        2. Forward the request to its target
        3. Sign the response
        4. Return the signed response

        Args:
            request: The request to proxy and sign

        Returns:
            The signed response

        Raises:
            InvalidAPIKey: If the Keystamp API key is invalid or missing
            ProxyError: If there's an error proxying the request
            SignatureError: If there's an error signing the response
        """
        pass

    @abstractmethod
    async def verify_signature(self, signature: str, response: ProxyResponse) -> bool:
        """Verify a response signature.

        Args:
            signature: The signature to verify
            response: The response claiming to have been signed

        Returns:
            True if signature is valid, False otherwise

        Raises:
            SignatureError: If there's an error verifying the signature
        """
