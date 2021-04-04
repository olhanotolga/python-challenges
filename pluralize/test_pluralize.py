__doc__

import pluralize


def test_answer():
    assert (
        pluralize.pluralize(
            [
                "matrix",
                "ox",
                "salmon",
                "mouse",
                "buzz",
                "buzz",
                "matrix",
                "ox",
                "salmon",
                "mouse",
            ]
        )
        == {"matrices", "oxen", "buzzes", "salmon", "mice"}
    )
    assert pluralize.pluralize(["cow", "pig", "cow", "cow"]) == {"cows", "pig"}
    assert pluralize.pluralize(["table", "table", "table"]) == {"tables"}
    assert pluralize.pluralize(["chair", "pencil", "arm"]) == {"chair", "pencil", "arm"}
