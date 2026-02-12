import os
import json
import docker
import uuid

from .load_query import LoadQuery
from .execution_result import ExecutionResult


class ExecutionModel:

    def __init__(self, image: str, result_root: str = "./results"):
        self.image = image
        self.result_root = result_root
        self.client = docker.from_env()

        os.makedirs(self.result_root, exist_ok=True)

    def execute(self, query: LoadQuery) -> ExecutionResult:

        task_id = str(uuid.uuid4())
        result_dir = os.path.join(self.result_root, task_id)
        os.makedirs(result_dir, exist_ok=True)

        container = self._run_container(query, result_dir)

        container.wait()

        result = self._collect_result(result_dir)

        container.remove()

        return result

    def _run_container(self, query: LoadQuery, result_dir: str):

        command = self._build_command(query)

        container = self.client.containers.run(
            self.image,
            command=command,
            volumes={
                os.path.abspath(result_dir): {
                    "bind": "/app/output",
                    "mode": "rw"
                }
            },
            detach=True
        )

        return container

    def _build_command(self, query: LoadQuery) -> str:
        """
        根据 LoadQuery 构造容器内执行命令
        """
        return f"python run.py --size {query.size} --type {query.type}"

    def _collect_result(self, result_dir: str) -> ExecutionResult:

        result_file = os.path.join(result_dir, "result.json")

        if not os.path.exists(result_file):
            raise RuntimeError("Execution failed: result.json not found")

        with open(result_file, "r") as f:
            data = json.load(f)

        return ExecutionResult(**data)
