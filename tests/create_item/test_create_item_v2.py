import requests
from tests.create_item.data import url, auth, headers, data
from tests.data import Auth


class CreateItem:
    @classmethod
    def post_create_item(cls):
        response = requests.post(
            url,
            auth=auth,
            headers=headers,
            data=data
        )
        return response


response = CreateItem.post_create_item()


def test_code_200():
    # response = CreateItem.post_create_item()

    assert response.status_code == 200


def test_headers_server():
    print(response.headers)
    assert response.headers.keys().__contains__("Server")
    assert response.headers["Server"] == "Jetty(12.0.16)"


def test_headers_content_length_0():
    # response = CreateItem.post_create_item()
    assert response.headers.keys().__contains__("Content-Length")
    assert response.headers["Content-Length"] == "0"


def test_headers_content_type_if_present():
    if "Content-Length" in response.headers and response.headers["Content-Length"] != "0":
        assert "Content-Type" in response.headers
        assert response.headers["Content-Type"].startswith("text/html")
    else:
        print("No content, so Content-Type is not expected")


def test_duplicate_item_creation_returns_error():
    # first_response = CreateItem.post_create_item()
    second_response = CreateItem.post_create_item()  # повторно

    assert second_response.status_code == 400
    assert "X-Error" in second_response.headers
    assert "already exists" in second_response.headers["X-Error"]


def test_get_job_info_happy1842():
    job_name = "happy1842"
    response = requests.get(
        f"{Auth.base_url}/job/{job_name}/api/json",
        auth=auth
    )

    assert response.status_code == 200

    data = response.json()
    assert data["name"] == job_name
    assert data["buildable"] is True
    assert "builds" in data


def test_trigger_build_happy1842():
    job_name = "happy1842"
    response = requests.post(
        f"{Auth.base_url}/job/{job_name}/build",
        auth=auth
    )
    assert response.status_code in [201, 302]  # Created или Redirect


def test_last_build_status():
    job_name = "happy1842"
    response = requests.get(
        f"{Auth.base_url}/job/{job_name}/lastBuild/api/json",
        auth=auth
    )
    assert response.status_code == 200
    data = response.json()
    assert "result" in data or data["building"] is True


def test_get_all_jobs():
    response = requests.get(f"{Auth.base_url}/api/json", auth=auth)
    assert response.status_code == 200
    data = response.json()
    assert "jobs" in data
    assert isinstance(data["jobs"], list)
