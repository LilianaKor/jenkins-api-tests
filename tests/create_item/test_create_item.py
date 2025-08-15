import requests
import random


base_url = "http://localhost:8080"
username = "Mo"
token = "110a2b2e109a674880aec07ab670247c49"

item_name = f"happy{random.randint(1000, 9999)}"
create_item = f"/createItem?name={item_name}"

freestyle_config_xml = """
<project>
<keepDependencies>false</keepDependencies>
<properties/>
<scm class="hudson.scm.NullSCM"/>
<canRoam>false</canRoam>
<disabled>false</disabled>
<blockBuildWhenDownstreamBuilding>false</blockBuildWhenDownstreamBuilding>
<blockBuildWhenUpstreamBuilding>false</blockBuildWhenUpstreamBuilding>
<triggers/>
<concurrentBuild>false</concurrentBuild>
<builders/>
<publishers/>
<buildWrappers/>
</project>
"""

url = f"{base_url}{create_item}"


def test_post_create_item_status_code_200():
    response = requests.post(
        url,
        auth=(username, token),
        headers={"Content-Type": "application/xml"},
        data=freestyle_config_xml.encode("utf-8"),
    )
    print(response.status_code)
    print(response.headers)

    assert response.status_code == 200


def test_post_create_item_headers_server():
    response = requests.post(
        url,
        auth=(username, token),
        headers={"Content-Type": "application/xml"},
        data=freestyle_config_xml.encode("utf-8"),
    )
    print(response.status_code)
    print(response.headers)
    assert response.headers.keys().__contains__("Server")
    assert response.headers["Server"] == "Jetty(12.0.16)"


