from at_common_workflow.core.workflow import Workflow
from at_common_workflow.core.task import Task
from at_common_workflow.builders.task import TaskBuilder
import logging
from pathlib import Path
from typing import Optional
from at_common_workflow.utils.logging import setup_logging

class WorkflowBuilder:
    def __init__(self, logger: Optional[logging.Logger] = None):
        self.workflow = Workflow(logger=logger)
    
    def add_task(self, name: str) -> 'TaskBuilder':
        """Add a task to the workflow and return a TaskBuilder for configuring it."""
        return TaskBuilder(self, name=name)

    def build(self) -> Workflow:
        """
        Build and return the workflow.
        
        Returns:
            Workflow: The built and validated workflow
        """
        return self.workflow

    @classmethod
    def with_logging(cls, 
        level: int = logging.INFO,
        log_file: Optional[Path] = None,
        format_string: Optional[str] = None
    ) -> 'WorkflowBuilder':
        """
        Create a WorkflowBuilder with configured logging.
        
        Args:
            level: Logging level
            log_file: Optional path to log file
            format_string: Optional custom format string for log messages
            
        Returns:
            WorkflowBuilder: Configured builder instance
        """
        logger = setup_logging(level, log_file, format_string)
        return cls(logger=logger)