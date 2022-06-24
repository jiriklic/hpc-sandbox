from unicodedata import name
from projen.python import PythonProject
from projen.github import GitHubOptions
from projen import TomlFile, DependencyType, JsonFile


aws_pcluster_experiment: PythonProject = PythonProject(
    author_email="web@jiriklic.com",
    author_name="Jiri Klic",
    module_name="aws_pcluster_experiment",
    name="aws-pcluster-experiment",
    description="HPC experiment running on AWS ParallelCluster",
    license="MIT",
    version="0.1.0",
    deps=[
        "python@^3.8",
        "aws-parallelcluster@^3.1.4"
    ],
    dev_deps=[
        "jupyterlab@^3.4.3",
    ],
    clobber=False,
    github_options=GitHubOptions(
        pull_request_lint=False
    ),
    mergify=False,
    pip=False,
    poetry=True,
    setuptools=False,
    venv=False,
)

poetry_toml: TomlFile = aws_pcluster_experiment.try_find_object_file("poetry.toml")
poetry_toml.add_override("virtualenvs.in-project", True)
aws_pcluster_experiment.deps_manager.install_task.reset("# no install")
aws_pcluster_experiment.deps.remove_dependency("projen", DependencyType.DEVENV)

aws_pcluster_experiment.gitignore.remove_patterns("/poetry.toml")
aws_pcluster_experiment.add_git_ignore("*.swp")
aws_pcluster_experiment.add_git_ignore("package-lock.json")
aws_pcluster_experiment.add_git_ignore("*.egg-info")

aws_pcluster_experiment.synth()
