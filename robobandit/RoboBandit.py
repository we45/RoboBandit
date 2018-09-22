import docker
from robot.api import logger
from docker.types import Mount

class RoboBandit(object):

    def __init__(self):
        self.client = docker.from_env()
        self.bandit_docker = "abhaybhargav/robobandit"

    def run_bandit_against_python_source(self, code_path, results_path):
        self.source_path = code_path
        self.results_path = results_path
        source_mount = Mount("/src", self.source_path, type = "bind")
        results_mount = Mount("/results", self.results_path, type = "bind")
        self.client.containers.run(self.bandit_docker, "bandit", mounts = [source_mount, results_mount])

    def run_safety_against_python_source(self, code_path, results_path):
        '''
        You need to ensure that requirements.txt is in the root of the src directory

        '''
        self.source_path = code_path
        self.results_path = results_path
        source_mount = Mount("/src", self.source_path, type = "bind")
        results_mount = Mount("/results", self.results_path, type = "bind")
        self.client.containers.run(self.bandit_docker, "safety", mounts = [source_mount, results_mount])


