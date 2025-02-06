
import pytest

from srbusapi.caching.redis_cache import RedisCache
from srbusapi.client.novi_sad import NoviSadClient


@pytest.fixture
def novi_sad_api():
    return NoviSadClient(cache=RedisCache(host="localhost", port=6379))


@pytest.mark.asyncio
async def test_get_stations(novi_sad_api):
    stations = await novi_sad_api.get_stations()
    assert stations, "Stations should not be empty"
    assert isinstance(stations, dict), "Stations should be a dictionary"
    assert "cities" in stations, "Stations should contain 'cities' key"
    assert "stations" in stations, "Stations should contain 'stations' key"
    assert isinstance(stations["cities"], list), "'cities' should be a list"
    assert isinstance(stations["stations"], list), "'stations' should be a list"
    assert len(stations["stations"]) > 0, "There should be at least one station"


@pytest.mark.asyncio
async def test_get_arrivals(novi_sad_api):
    station_id = "6853"
    arrivals = await novi_sad_api.get_arrivals(station_id)
    assert arrivals, "Arrivals should not be empty"
    assert isinstance(arrivals, list), "Arrivals should be a list"
    assert all(isinstance(arr, dict) for arr in arrivals), (
        "All elements in arrivals should be dictionaries"
    )


@pytest.mark.asyncio
async def test_get_route(novi_sad_api):
    actual_line_number = "761"
    route = await novi_sad_api.get_route(actual_line_number)
    assert route, "Route should not be empty"
    assert isinstance(route, dict), "Route should be a dictionary"
    # Check structure of route
    assert "line_route" in route, "Route should contain 'line_route'"
    assert isinstance(route["line_route"], list), "'line_route' should be a list"
    assert all(isinstance(point, str) for point in route["line_route"]), (
        "All elements in line_route should be strings"
    )


@pytest.mark.asyncio
async def test_get_route_version(novi_sad_api):
    actual_line_number = "761"
    route_version = await novi_sad_api.get_route_version(actual_line_number)
    assert route_version, "Route version should not be empty"
    assert isinstance(route_version, dict), "Route version should be a dictionary"
    # Check structure of route version
    assert "line_route_version" in route_version, (
        "Route version should contain 'line_route_version'"
    )
    assert isinstance(route_version["line_route_version"], int), (
        "'line_route_version' should be an integer"
    )
