""" URI handling module"""

from __future__ import annotations

import urllib.parse

from zimscraperlib import logger
from zimscraperlib.misc import first


def rebuild_uri(
    uri: urllib.parse.ParseResult,
    scheme: str | None = None,
    username: str | None = None,
    password: str | None = None,
    hostname: str | None = None,
    port: str | int | None = None,
    path: str | None = None,
    params: str | None = None,
    query: str | None = None,
    fragment: str | None = None,
    *,
    failsafe: bool = False,
) -> urllib.parse.ParseResult:
    """new ParseResult named tuple from uri with requested part updated"""
    try:
        username = first(username, uri.username)
        password = first(password, uri.password)
        hostname = first(hostname, uri.hostname)
        port = first(port, uri.port)
        netloc = (
            f"{username}{':' if password else ''}{password}"
            f"{'@' if username or password else ''}{hostname}"
            f"{':' if port else ''}{port}"
        )
        return urllib.parse.urlparse(
            urllib.parse.urlunparse(
                (
                    first(scheme, uri.scheme),
                    netloc,
                    first(path, uri.path),
                    first(params, uri.params),
                    first(query, uri.query),
                    first(fragment, uri.fragment),
                )
            )
        )
    except Exception as exc:
        if failsafe:
            logger.error(
                f"Failed to rebuild "  # lgtm [py/clear-text-logging-sensitive-data]
                f"URI {uri} with scheme={scheme} username={username} "
                f"password={password} hostname={hostname} port={port} path={path} "
                f"params={params} query={query} fragment={fragment} - {exc}"
            )
            return uri
        raise exc
