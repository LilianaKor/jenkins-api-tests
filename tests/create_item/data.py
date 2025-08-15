import random
from tests.data import Auth


class Config:

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


item_name = f"happy{random.randint(1000, 9999)}"
create_item_endpoint = f"/createItem?name={item_name}"
url = f"{Auth.base_url}{create_item_endpoint}"
auth = (Auth.username, Auth.token)
headers = {"Content-Type": "application/xml"}
data = Config.freestyle_config_xml.encode("utf-8")
