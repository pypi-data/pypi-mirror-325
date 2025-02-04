from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    threema_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/contact-categories/{threema_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200
    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    threema_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, ErrorResponse]]:
    """Contact Categories: Show

     Show a contact category (Directory Feature required)

    Args:
        threema_id (str):  Example: B4UXXX11.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        threema_id=threema_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    threema_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, ErrorResponse]]:
    """Contact Categories: Show

     Show a contact category (Directory Feature required)

    Args:
        threema_id (str):  Example: B4UXXX11.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse]
    """

    return sync_detailed(
        threema_id=threema_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    threema_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, ErrorResponse]]:
    """Contact Categories: Show

     Show a contact category (Directory Feature required)

    Args:
        threema_id (str):  Example: B4UXXX11.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        threema_id=threema_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    threema_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, ErrorResponse]]:
    """Contact Categories: Show

     Show a contact category (Directory Feature required)

    Args:
        threema_id (str):  Example: B4UXXX11.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            threema_id=threema_id,
            client=client,
        )
    ).parsed
