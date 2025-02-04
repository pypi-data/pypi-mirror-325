from typing import Callable

from arraylake.repos.icechunk.utils import _raise_if_no_icechunk
from arraylake.types import S3Credentials


def get_icechunk_container_credentials(
    bucket_platform: str,
    s3_credentials: S3Credentials | None,
    credential_refresh_func: Callable | None,
):
    """Gets the icechunk virtual chunk container credentials
    from the given bucket config and credentials.

    Args:
        bucket_platform: The platform of the bucket. Supported platforms are "s3", "s3c", and "minio".
        s3_credentials: Optional S3Credentials to use for the virtual chunk container.
        credential_refresh_func (Callable[[], S3StaticCredentials]):
            Optional function to refresh S3 credentials. This function must
            be synchronous, cannot take in any args, and return a
            icechunk.S3StaticCredentials object.

    Returns:
        icechunk.Credentials.S3:
            The virtual chunk container credentials for the bucket.
    """
    _raise_if_no_icechunk()
    import icechunk

    # Check the if the bucket is an S3 or S3-compatible bucket
    if bucket_platform in ("s3", "s3c", "s3-compatible", "minio"):
        if credential_refresh_func and s3_credentials:
            raise ValueError("Cannot provide both static credentials and a credential refresh function.")
        if credential_refresh_func:
            return icechunk.s3_refreshable_credentials(credential_refresh_func)
        elif s3_credentials:
            return icechunk.s3_static_credentials(
                access_key_id=s3_credentials.aws_access_key_id,
                secret_access_key=s3_credentials.aws_secret_access_key,
                session_token=s3_credentials.aws_session_token,
                expires_after=s3_credentials.expiration,
            )
        else:
            return icechunk.s3_from_env_credentials()
    else:
        raise ValueError(f"Unsupported bucket platform for virtual chunk container credentials: {bucket_platform}")
