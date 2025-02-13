"""Version information for Keystamp components

Uses integer versioning for internal protocol versions.
"""

# Version of the underlying data format (Transcript object)
TRANSCRIPT_VERSION = 1

# Version of signed data format (SignedTranscript object)
# If client is asked to verify a transcript with a greater version
# than this, it raises an error.
# (Also known as signing protocol version)
SIGNED_TRANSCRIPT_VERSION = 1

# Version of client-server API protocol
# Kept separate from client, server, and data format versions, as these can all
# change independently, and not all changes affect each other.
# Any changes to any API call should result in a version bump.
API_PROTOCOL_VERSION = 1

# When building in a dev environment, our package's __version__ won't be
# populated from pyproject.toml.
# We provide this fallback in case this is used for anything.
CLIENT_VERSION_DEV = "0.1.0-dev"  # Keep this as SemVer since it's for external use


