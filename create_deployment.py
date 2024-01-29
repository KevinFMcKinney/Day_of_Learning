from prefect import flow

if __name__ == "__main__":
    flow.from_source(
        source="https://github.com/KevinFMcKinney/Day_of_Learning_Prefect.git",
        entrypoint="days_till_my_birthday.py:days_till_my_birthday",
    ).deploy(
        name="birthay",
        work_pool_name="birthday_pool",
        cron="0 1 * * *",
    )