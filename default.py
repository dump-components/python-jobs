from repository.models.task_model import TaskModel
from .steps.open_browser import OpenBrowser
from services.browser.manipulation_browser import ServiceManipulationBrowser

class Default:
    
    def __init__(self, task: TaskModel) -> None:
        self.__task = task
    
    def run(self):
        print('reproduzindo a estrategia padrão')
        print(self.__task)
        print(OpenBrowser(ServiceManipulationBrowser()).open_google())