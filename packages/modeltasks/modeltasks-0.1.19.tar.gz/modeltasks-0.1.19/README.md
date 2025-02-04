# Model tasks

An opinionated and lightweight workflow management system and task graph. Born from the desire to have
a reusable code skeleton for geoprocessing and data pipelines projects this package offers:

- Write cleaner code code in separate tasks
- Formulate task dependencies and automatically resolve those as a direct acyclical graph (DAG)
- Display your models
- Parallelize concurrent tasks
- Task configuration
- Caching and invalidation of intermediate task results based on configuration
- Easily generate a task graph documentation


## Quickstart

A model consists of individual tasks which formulate their dependence on other tasks. Together they build one or more acyclical directed graphs, which do not allow loops or task repetition. Tasks are implement as subclasses of the ModelTask class. They can be either all defined within one file or within a folder of Python modules. The latter is more practical if the model grows and consists of many tasks.

### Create a one-file model

**model.py**

```
from modeltasks import Model, ModelTask


my_model = Model(title='My Model', model_tasks=__file__)


class TaskA(ModelTask):
    def run (self, logger, workspace):
        logger.info(f'Running an A task in {workspace}')
  
        
class TaskB(ModelTask):
    def run (self, logger, workspace):
        logger.info(f'Running a B task in {workspace}')
```

### Create a model with task modules

**Prepare project structure**

```
touch model.py
mkdir task_modules
touch task_modules/a_tasks.py
touch task_modules/b_tasks.py
```

**model.py**

```
from modeltasks import Model


my_model = Model(title='My Model', model_tasks='task_modules')
```

**a_tasks.py**

```
from modeltasks import ModelTask


class TaskA(ModelTask):
    def run (self, logger, workspace):
        logger.info(f'Running an A task in {workspace}')
```

**b_tasks.py**

```
from modeltasks import ModelTask


class TaskB(ModelTask):
    def run (self, logger, workspace):
        logger.info(f'Running a B task in {workspace}')
```

The above code creates a model with two simple tasks. But not a task graph yet because both tasks have not defined:
- inputs (dependencies)
- outputs (results)
- configuration

Putting tasks into a workflow graph is achieved by defining task inputs and outputs. Let's look at the two example tasks we just created and assume that `TaskB` requires `TaskA` to run first and then use its output.

**a_tasks.py (With output)**

```
from modeltasks import ModelTask
from modeltasks.data import VariableOutput


class TaskA(ModelTask):

    a_output: VariableOutput

    def run (self, logger, workspace):
        logger.info(f'Running an A task in {workspace}')
        self.a_output = 'First I ran task A.'
```

**b_tasks.py (With dependency and output)**

```
from modeltasks import ModelTask
from modeltasks.data import VariableInput, VariableOutput


class TaskB(ModelTask):

    a_input: VariableInput = 'a_tasks.TaskA'
    b_output: VariableOutput

    def run (self, logger, workspace):
        logger.info(f'Running an B task in {workspace}')
        self.b_output = f'{self.a_input} Then I ran task B.'
```

### Run a model

To run a model, we need to specify an entry task. This is the task that will be run at the end after all of its required task dependencies have been resolved and their output gathered.

```
python3 model.py --run --task b_tasks.TaskB
```

### Model visualization

Sometimes it is helpful to see a visual representation of all the task interdependencies. To render such a visual task graph call your model with:

```
python3 model.py --graph --output=mermaid.md (Mermaid file)
python3 model.py --graph --output=graph.png (Image file)
```

## Documentation

To learn more about supported input and output types, dependency definition, task schedulers, result caching, etc. head over to the [package documentation](https://gitlab.com/geotom/modeltasks/-/wikis/Modeltasks)

## Contribution

Please leave feedback, questions, suggestions on the [project's issue tracker](https://gitlab.com/geotom/modeltasks/-/issues).
