import requests
from tests.create_item.data import Auth


class JobsAPI:

    @classmethod
    def get_all_jobs(cls):
        return requests.get(f"{Auth.base_url}/api/json", auth=(Auth.username, Auth.token))

    @classmethod
    def get_job_info(cls, job_name):
        return requests.get(f"{Auth.base_url}/job/{job_name}/api/json", auth=(Auth.username, Auth.token))

    @classmethod
    def trigger_build(cls, job_name):
        return requests.post(f"{Auth.base_url}/job/{job_name}/build", auth=(Auth.username, Auth.token))

    @classmethod
    def get_last_build_info(cls, job_name):
        return requests.get(f"{Auth.base_url}/job/{job_name}/lastBuild/api/json", auth=(Auth.username, Auth.token))

    @classmethod
    def disable_job(cls, job_name):
        return requests.post(
            f"{Auth.base_url}/job/{job_name}/disable",
            auth=(Auth.username, Auth.token)
        )

    @classmethod
    def enable_job(cls, job_name):
        return requests.post(
            f"{Auth.base_url}/job/{job_name}/enable",
            auth=(Auth.username, Auth.token)
        )

    @classmethod
    def delete_job(cls, job_name):
        return requests.post(
            f"{Auth.base_url}/job/{job_name}/doDelete",
            auth=(Auth.username, Auth.token)
        )
