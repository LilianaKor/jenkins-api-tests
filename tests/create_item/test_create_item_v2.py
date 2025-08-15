import requests
from tests.create_item.data import url, auth, headers, data


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
    #response = CreateItem.post_create_item()

    assert response.status_code == 200


def test_headers_server():

    print(response.headers)
    assert response.headers.keys().__contains__("Server")
    assert response.headers["Server"] == "Jetty(12.0.16)"


def test_headers_content_length_0():
    #response = CreateItem.post_create_item()
    assert response.headers.keys().__contains__("Content-Length")
    assert response.headers["Content-Length"] == "0"



def test_headers_content_type_if_present():
    if "Content-Length" in response.headers and response.headers["Content-Length"] != "0":
        assert "Content-Type" in response.headers
        assert response.headers["Content-Type"].startswith("text/html")
    else:
        print("No content, so Content-Type is not expected")
