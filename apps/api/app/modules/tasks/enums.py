from enum import StrEnum


class TaskStatus(StrEnum):
    """
    Status of a task.
    """

    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"


class TaskPriority(StrEnum):
    """
    Priority of a task.
    """

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
