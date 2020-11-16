import pytest
import requests_mock

from src.data import download_data
from tests.mock_api import MockApi


@pytest.fixture
def requests_mocker() -> requests_mock.Mocker:
    """Enable request_mocker for a test session, yields the mock instance for interaction."""
    with requests_mock.Mocker(case_sensitive=True) as mocker:
        yield mocker


@pytest.fixture
def mock_api(requests_mocker):
    mock = MockApi(requests_mocker, hostname='http://fakeweather.com')
    return mock


def test_download_data(mock_api):
    # test conditions before
    assert len(mock_api.requests) == 0

    # download data
    data = download_data(hostname='http://fakeweather.com')

    # evaluate
    assert len(mock_api.requests) == 1
    assert len(data) > 0
    measurement = data[0]
    assert 'the_temp' in measurement
