from .src.magic import UNUSED  # this performs some magic to hide controlflow warning
from .src.agents import Agent
# from .src.memory import AsyncMemory, AsyncPostgresMemoryProvider, Memory, PostgresMemoryProvider
from .src.memory import Memory
from .src.workflow import Workflow, run_agents
from .src.agent_methods.data_models.datamodels import PersonaConfig
from .src.handlers import AsyncLoggingHandler, LoggingHandler
from .client import client


__all__ = [
    "Agent",
    # "AsyncMemory",
    # "AsyncPostgresMemoryProvider",
    "Memory",
    # "PostgresMemoryProvider",
    "Workflow",
    "run_agents",
    "PersonaConfig",
    "AsyncLoggingHandler",
    "LoggingHandler",
    "client"
]


__version__="1.1.0"