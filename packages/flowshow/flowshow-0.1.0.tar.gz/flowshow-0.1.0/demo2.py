import marimo

__generated_with = "0.10.19"
app = marimo.App(width="medium")


@app.cell
def _():
    import time
    import random

    from flowshow import task

    # Turns a function into a Task, which tracks a bunch of stuff
    @task
    def my_function(x):
        time.sleep(0.5)
        return x * 2

    # Tasks can also be configured to handle retries
    @task(retry_on=ValueError, retry_attempts=10)
    def might_fail():
        time.sleep(0.5)
        if random.random() < 0.5:
            raise ValueError("oh no, error!")
        return "done"

    @task
    def main_job():
        print("This output will be captured by the task")
        for i in range(3):
            my_function(10)
            might_fail()
        return "done"

    # Run like you might run a normal function
    main_job()
    return main_job, might_fail, my_function, random, task, time


@app.cell
def _(main_job):
    main_job.to_dataframe()
    return


@app.cell
def _(main_job):
    main_job.runs
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
