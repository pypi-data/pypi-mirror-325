import asyncio
from datetime import timedelta
from typing import Any, Dict, Optional, Sequence, Union

from airflow.exceptions import AirflowException
from airflow.providers.google.cloud.hooks.bigquery import BigQueryHook
from airflow.sensors.base import BaseSensorOperator
from airflow.triggers.base import TriggerEvent
from airflow.utils.context import Context


class BigQueryAsyncSensor(BaseSensorOperator):
    def __init__(
        self,
        template_path: str,
        dag_folder_path: str,
        labels: dict[str, str],
        project_id: str,
        gcp_conn_id: Optional[str] = "google_cloud_default",
        impersonation_chain: Union[str, Sequence[str], None] = None,
        retry_delay: timedelta = timedelta(seconds=60),
        *args,
        **kwargs,
    ) -> None:
        super().__init__(*args, **kwargs)
        self.template_path = template_path
        self.dag_folder_path = dag_folder_path
        self.labels = labels
        self.project_id = project_id
        self.gcp_conn_id = gcp_conn_id
        self.impersonation_chain = impersonation_chain
        self.retry_delay = retry_delay

    def execute(self, context: Context) -> None:
        self.defer(
            trigger=self,
            method_name="execute_complete",
            timeout=timedelta(seconds=self.timeout),
        )

    async def run(self) -> TriggerEvent:
        while True:
            result = self._execute_query()
            if result is True:
                return TriggerEvent({"status": "success"})
            await asyncio.sleep(self.retry_delay.seconds)

    def _execute_query(self) -> bool:
        hook = BigQueryHook(
            gcp_conn_id=self.gcp_conn_id,
            use_legacy_sql=False,
            impersonation_chain=self.impersonation_chain,
            labels=self.labels,
        )
        client = hook.get_client(project_id=self.project_id)
        with open(f"{self.dag_folder_path}/{self.template_path}", "r") as file:
            sql = file.read()
        results = list(client.query_and_wait(sql))
        return results[-1][0] if len(results) > 0 else False

    def execute_complete(
        self, context: Dict[str, Any], event: Dict[str, Any] | None = None
    ) -> None:
        if event:
            if event["status"] == "success":
                self.log.info("Deferred task completed successfully.")
                return
            raise AirflowException(event["message"])

        raise AirflowException("No event received in trigger callback")

    def serialize(self) -> tuple[str, dict[str, Any]]:
        return (
            f"{self.__class__.__module__}.{self.__class__.__name__}",
            {
                "template_path": self.template_path,
                "retry_delay": self.retry_delay,
                "dag_folder_path": self.dag_folder_path,
                "labels": self.labels,
                "project_id": self.project_id,
                "gcp_conn_id": self.gcp_conn_id,
                "impersonation_chain": self.impersonation_chain,
            },
        )