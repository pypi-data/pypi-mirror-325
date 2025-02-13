from abc import ABC, abstractmethod
from typing import List

from ..interface import (
    SettingsInterface,
    LoggerManagerInterface,
)
from ..model import Tenant, KnowledgeCreate, Knowledge, Task


class TaskEnginPluginInterface(ABC):
    settings: SettingsInterface
    logger: LoggerManagerInterface

    def __init__(
        self,
        logger: LoggerManagerInterface,
        settings: SettingsInterface,
    ):
        try:
            logger.info("TaskEngine plugin is initializing...")
            self.settings = settings
            self.logger = logger
            self.init()
            logger.info("TaskEngine plugin is initialized")
        except Exception as e:
            logger.error(f"TaskEngine plugin init error: {e}")

    @abstractmethod
    def init(self):
        pass

    @abstractmethod
    async def gen_knowledge_list(
        self, user_input: List[KnowledgeCreate], tenant: Tenant
    ) -> List[Task]:
        pass

    @abstractmethod
    async def init_task_from_knowledge(
        self, knowledge_list: List[Knowledge], tenant: Tenant
    ) -> List[Task]:
        pass

    @abstractmethod
    async def execute_task(self, task_id: str) -> List[Task]:
        pass

    @abstractmethod
    async def batch_execute_task(
        self, task_list: List[Task], knowledge_list: List[Knowledge]
    ) -> List[Task]:
        pass
