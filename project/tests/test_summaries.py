# project/tests/test_summaries.py


import json


def test_create_summary(test_app_with_db):
    response = test_app_with_db.post(
        "/summaries/",
        data=json.dumps(
            {"url": "http://foo.bar"}
        )
    )

    assert response.status_code == 201
    assert response.json()["url"] == "http://foo.bar"


def test_create_summary_invalid_json(test_app_with_db):
    response = test_app_with_db.post("/summaries/", data=json.dumps({}))

    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "url"],
                "msg": "field required",
                "type": "value_error.missing"
            }
        ]
    }
