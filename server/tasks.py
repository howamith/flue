# PyPI modules.
from celery import Celery

# Standard library modules.
from os import environ
import random
import time
from typing import Dict

celery = Celery(
    "tasks",
    backend=environ.get("CELERY_BROKER_URL", "redis://localhost:6379/0"),
    broker=environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379/0"),
)


@celery.task(bind=True)
def long_task(self, name: str, duration: int) -> Dict[str, str]:
    """Background task that runs a long function with progress reports.

    Args:
        name: The task"s name.
        duration: The duration, in milliseconds, for the task to run.
    """

    # Words to be randomised in status messages.
    verb = ["Processing", "Optimising", "Repairing", "Loading", "Checking"]
    adjective = ["master", "radiant", "silent", "harmonic", "fast"]
    noun = ["solar array", "particle reshaper", "cosmic ray", "orbiter", "bit"]

    # Calculate how many iterations there'll be.
    iters = [250 / 1000] * int(duration / 250)
    rem = duration % 250
    if rem:
        iters.append((250 - rem) / 100)

    num_iters = len(iters)
    self.update_state(
        state="PROGRESS",
        meta={"current": 0, "total": num_iters, "status": "Starting..."},
    )

    for i in range(0, num_iters):
        time.sleep(iters[i])

        self.update_state(
            state="PROGRESS",
            meta={
                "current": i + 1,
                "total": num_iters,
                "status": "{0} {1} {2}...".format(
                    random.choice(verb),
                    random.choice(adjective),
                    random.choice(noun),
                ),
            },
        )

    # 80% chance of succes
    results = [False, True, True, True, True]
    return {
        "current": num_iters,
        "total": num_iters,
        "status": "success" if random.choice(results) else "failure",
        "result": 42,
    }
