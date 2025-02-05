from modal import enable_output
from modalfold import app


def test_esmfold():
    from modalfold.esmfold import ESMFold

    with enable_output():
        with app.run():
            model = ESMFold()
            result = model.fold.remote("MALWMRLLPLLALLALWGPDPAAA")
            print(result)


if __name__ == "__main__":
    test_esmfold()
