from src.processing import process_data


def test_process_data():
    data = [
        {
            'the_temp': 20,
        },
        {
            'the_temp': 30,
        },
    ]

    output = process_data(data=data)

    # evaluate
    assert output == 25
