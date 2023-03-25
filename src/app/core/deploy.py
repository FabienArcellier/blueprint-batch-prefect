"""
This module provides a library to plan a deployment for Prefect.
The developer saves these flows in a deployment book.

>>> deploy_book = deploy.create_deploy_book()
>>> deploy.register(deploy_book, flow1)
>>> deploy.register(deploy_book, flow2)
>>> deploy.deploy(deploy_book)
"""
import dataclasses
import os
from typing import List, Optional, Union

from prefect import Flow
from prefect.deployments import Deployment
from prefect.server.schemas.schedules import IntervalSchedule, CronSchedule


@dataclasses.dataclass
class DeployFlow:
    """
    defines a flow to deploy
    """
    flow: Flow
    name: Optional[str] = None
    interval: Optional[int] = None
    cron: Optional[str] = None

    @property
    def schedule(self) -> Optional[Union[IntervalSchedule, CronSchedule]]:
        if self.interval is None and self.cron is None:
            return None
        elif self.interval is not None:
            return IntervalSchedule(interval=self.interval)
        elif self.cron is not None:
            return CronSchedule(cron=self.cron)

        return None


@dataclasses.dataclass
class DeployBook:
    deploy_flows: List[DeployFlow] = dataclasses.field(default_factory=list)


def create_deploy_book() -> DeployBook:
    return DeployBook()


def register(deploy_book: DeployBook, flow: Flow, name: Optional[str] = None, interval: Optional[int] = None, cron: Optional[str] = None) -> None:
    if interval is not None and cron is not None:
        raise ValueError(f"Cannot define both interval and cron for the flow {flow.name=} - {interval=} - {cron=}")

    deploy_book.deploy_flows.append(DeployFlow(flow=flow, name=name, interval=interval, cron=cron))


def deploy(book: DeployBook) -> None:
    """
    The url of the prefect instance to deploy to is retrieved
    from the PREFECT_API_URL environment variable

    Inject a specific PREFECT_API_URL variable of the endpoint the deploy script will use.
    """
    root_dir = os.path.join(os.path.dirname(__file__), '..', '..', '..')
    for deploy_flow in book.deploy_flows:
        deployment = Deployment.build_from_flow(
            flow=deploy_flow.flow,
            name="main" if deploy_flow.name is None else deploy_flow.name,
            path=root_dir,
            schedule=deploy_flow.schedule,
        )

        deployment.apply()
