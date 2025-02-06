"""Test that an artist and title can be fetched from every radio."""

from unittest.mock import patch

import pytest

from fip_radiod.fip_fetch import (
    DEFAULT_ARTIST,
    DEFAULT_TITLE,
    FipStation,
    fetch_currently_playing,
)

MOCK_RESPONSE = {
    "data": {
        "live": {
            "song": {
                "track": {
                    "title": "Song Title",
                    "mainArtists": ["Artist Name"],
                }
            }
        }
    }
}


@pytest.mark.parametrize("station", [station.name for station in FipStation])
@pytest.mark.radiofranceapikey
def test_fetch_currently_playing(station: str) -> None:
    """Test that the fetching function works."""
    with patch("fip_fetch._make_query") as mock_query:
        mock_query.return_value.status_code = 200
        mock_query.return_value.json.return_value = MOCK_RESPONSE
        title, artist = fetch_currently_playing(station)

        assert (title != DEFAULT_TITLE) or (
            artist != DEFAULT_ARTIST
        ), f"Title and artist are empty for station {station}"
