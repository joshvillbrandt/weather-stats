from src.data import download_data


def test_download_data():
    data = download_data()

    # evaluate
    assert len(data) > 0
