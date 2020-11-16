from src.data import download_data


def test_download_data():
    data = download_data()

    # evaluate
    assert data == 'World'
