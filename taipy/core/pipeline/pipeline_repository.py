import pathlib
from collections import defaultdict

from taipy.core.common import utils
from taipy.core.common.alias import Dag
from taipy.core.config.config import Config
from taipy.core.exceptions.pipeline import NonExistingPipeline
from taipy.core.exceptions.task import NonExistingTask
from taipy.core.pipeline.pipeline import Pipeline
from taipy.core.pipeline.pipeline_model import PipelineModel
from taipy.core.repository import FileSystemRepository
from taipy.core.task.task_manager import TaskManager


class PipelineRepository(FileSystemRepository[PipelineModel, Pipeline]):
    def __init__(self):
        super().__init__(model=PipelineModel, dir_name="pipelines")

    def to_model(self, pipeline: Pipeline) -> PipelineModel:
        return PipelineModel(
            pipeline.id,
            pipeline._parent_id,
            pipeline._config_id,
            pipeline._properties.data,
            [task.id for task in pipeline._tasks.values()],
            utils.fcts_to_dict(pipeline._subscribers),
        )

    def from_model(self, model: PipelineModel) -> Pipeline:
        try:
            tasks = self.__to_tasks(model.tasks)
            pipeline = Pipeline(
                model.name,
                model.properties,
                tasks,
                model.id,
                model.parent_id,
                {utils.load_fct(it["fct_module"], it["fct_name"]) for it in model.subscribers},
            )
            return pipeline
        except NonExistingTask as err:
            raise err
        except KeyError:
            pipeline_err = NonExistingPipeline(model.id)
            raise pipeline_err

    @property
    def storage_folder(self) -> pathlib.Path:
        return pathlib.Path(Config.global_config.storage_folder)  # type: ignore

    @staticmethod
    def __to_tasks(task_ids):
        tasks = []
        for _id in task_ids:
            if task := TaskManager.get(_id):
                tasks.append(task)
            else:
                raise NonExistingTask(_id)
        return tasks
