#!/usr/bin/env python3
"""Get the song currently played on FIP."""
import argparse
import logging
import os
from enum import Enum
from typing import Any

import requests
from dotenv import load_dotenv

API_URL = "https://openapi.radiofrance.fr/v1/graphql"
load_dotenv()
TOKEN = os.getenv("RADIOFRANCE_API_TOKEN")
if not TOKEN:
    logging.error("RADIOFRANCE_API_TOKEN key not found in .env file.")
    TOKEN = "0000-0000"

DEFAULT_ARTIST = "not found"
DEFAULT_TITLE = "not found"


class FipStation(Enum):
    fip = "FIP"
    electro = "FIP_ELECTRO"
    groove = "FIP_GROOVE"
    hip_hop = "FIP_HIP_HOP"
    jazz = "FIP_JAZZ"
    metal = "FIP_METAL"
    nouveautes = "FIP_NOUVEAUTES"
    pop = "FIP_POP"
    reggae = "FIP_REGGAE"
    rock = "FIP_ROCK"
    # sacre_francais = "FIP_SACRE_FRANCAIS"
    world = "FIP_WORLD"

    @classmethod
    def _missing_(cls, value: Any):
        """Override default `_missing` to return classic FIP by default."""
        logging.warning("Resorting to default FIP.")
        return cls.fip


def _query(station: FipStation) -> str:
    """Format the query for given radio station."""
    my_query = (
        f"{{"
        f" live(station: {station.value}) {{"
        f"   song {{"
        f"     track {{"
        f"       title"
        f"       mainArtists"
        f"     }}"
        f"   }}"
        f" }}"
        f"}}"
    )
    logging.debug(f"Get title song with query:\n{my_query}")
    return my_query


def _set_headers(token: str = TOKEN) -> dict[str, str]:
    """Set the headers, including authentication."""
    my_headers = {
        "Content-Type": "application/json",
        "x-token": token,
    }
    logging.debug(f"Make query with header:\n{my_headers}")
    return my_headers


def _make_query(
    station: FipStation, token: str = TOKEN, url: str = API_URL
) -> requests.Response:
    """Get the data."""
    response = requests.post(
        url, json={"query": _query(station)}, headers=_set_headers(token)
    )
    logging.debug(f"Queried\n{response.request.body}")
    return response


def fetch_currently_playing(
    station: FipStation | str, verbose: bool = False
) -> tuple[str, str]:
    """Get title and artist of current song.

    Parameters
    ----------
    station : FipStation | str
        Name of the station, or directly a :class:`.FipStation` object.
    verbose : bool, optional
        If the script should output more information. The default is False.

    Returns
    -------
    tuple[str, str]
        Title and artist.

    """
    if verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    if isinstance(station, str):
        station = getattr(FipStation, station)
    assert isinstance(station, FipStation)
    response = _make_query(station)

    if response.status_code == 200:
        data = response.json()
        song = (
            data.get("data", {})
            .get("live", {})
            .get("song", {})
            .get("track", {})
        )
        title = song.get("title")
        artists = song.get("mainArtists", [])
        return title, ", ".join(artists)

    logging.error(
        f"Query failed with status code {response.status_code}: {response.text}"
    )
    return DEFAULT_TITLE, DEFAULT_ARTIST


def ui() -> tuple[str, str]:
    """Provide interface with the command line."""
    parser = argparse.ArgumentParser(
        "fip-fetch", description="Tell what is played on FIP right now."
    )
    parser.add_argument(
        "-s",
        "--station",
        help=(
            "Name of the radio to fetch. Must be one of: electro, groove,"
            " hip_hop, jazz, metal, nouveautes, pop, reggae, rock, world. "
            "If not provided, we take the 'standard' FIP."
        ),
        type=str,
        required=False,
        choices=[webradio.name for webradio in FipStation],
        default="fip",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        help="Print debug information.",
        action="store_true",
        required=False,
    )
    args = parser.parse_args()
    return fetch_currently_playing(station=args.station, verbose=args.verbose)


def main() -> None:
    """Test the query."""
    print(f"Currently playing on FIP: {fetch_currently_playing('fip')}")


if __name__ == "__main__":
    main()
