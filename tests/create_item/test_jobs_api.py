from tests.create_item.jobs_api import JobsAPI
from tests.create_item.test_create_item_v2 import CreateItem


def test_get_job_info():
    job_name = "happy1842"
    response = JobsAPI.get_job_info(job_name)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == job_name


def test_trigger_build():
    job_name = "happy1842"
    response = JobsAPI.trigger_build(job_name)
    assert response.status_code in [201, 302]


def test_last_build_info():
    job_name = "happy1842"
    response = JobsAPI.get_last_build_info(job_name)
    assert response.status_code == 200
    data = response.json()
    assert "building" in data or "result" in data


def test_get_all_jobs():
    response = JobsAPI.get_all_jobs()
    assert response.status_code == 200


def test_disable_enable_job():
    job_name = "happy1842"
    print(f"Testing disable/enable for job: {job_name}")
    disable_response = JobsAPI.disable_job(job_name)
    print(f"Disabled: status code = {disable_response.status_code}")
    assert disable_response.status_code in [200, 302]

    # Проверим, что теперь job не buildable
    info = JobsAPI.get_job_info(job_name).json()

    assert info["buildable"] is False

    enable_response = JobsAPI.enable_job(job_name)
    assert enable_response.status_code in [200, 302]

    info = JobsAPI.get_job_info(job_name).json()
    print(f"After enabling: buildable = {info['buildable']}")
    assert info["buildable"] is True


def test_delete_job():
    job_name = "job_to_delete"
    # 1. Создаём job
    CreateItem.post_create_item()
    # 2. Удаляем
    response = JobsAPI.delete_job(job_name)
    assert response.status_code in [200, 302]

    # 3. Проверяем, что он не существует
    response_check = JobsAPI.get_job_info(job_name)
    assert response_check.status_code == 404
