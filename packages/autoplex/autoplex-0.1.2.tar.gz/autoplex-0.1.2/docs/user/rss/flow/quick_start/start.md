(rss-quickstart)=

# Quick start

The `RssMaker` class in `autoplex` is the core interface for creating ML-RSS potential models from scratch. It accepts customizable parameters that control key aspects of the RSS process, including:

- **Randomized structure generation**  
  Generate diverse initial structures for broader configurational space exploration.

- **Sampling strategies**  
  Customize methods for selecting configurations based on energy and structure diversity.

- **DFT labeling**  
  Perform single-point DFT calculations to provide accurate energy and force labels for training.

- **Data preprocessing**  
  Include steps like data regularization and filtering to improve model performance.

- **Potential fitting**  
  Perform machine learning potential fitting with flexible hyperparameter tuning.

- **Iterative loop**  
  Continuously refine the potential model through iterative RSS cycles.

Parameters can be specified either through a YAML configuration file or as direct arguments in the `make` method.

## Running the workflow with a RSSConfig object

> **Recommendation**: This is currently our recommended approach for setting up and managing RSS workflows.

The RSSConfig object can be instantiated using a custom YAML configuration file, as illustrated in previous section. 
A comprehensive list of parameters, including default settings and modifiable options, is available in `autoplex.settings.RssConfig` pydantic model. 
To start a new workflow, create an `RssConfig` object using the YAML file and pass it to the `RSSMaker` class.
When initializing the RssConfig object with a YAML file, any specified keys will override the corresponding default values.

```python
from autoplex.settings import RssConfig
from autoplex.auto.rss.flows import RssMaker
from fireworks import LaunchPad
from jobflow.managers.fireworks import flow_to_workflow

rss_config = RssConfig.from_file('path/to/your/config.yaml')

rss_job = RssMaker(name="your workflow name", rss_config=rss_config).make()
wf = flow_to_workflow(rss_job) 
lpad = LaunchPad.auto_load()
lpad.add_wf(wf)
```

The above code is based on [`FireWorks`](https://materialsproject.github.io/fireworks/) for job submission and management. You could also use [`jobflow-remote`](https://matgenix.github.io/jobflow-remote/), in which case the code snippet would change as follows. 


```python
from autoplex.settings import RssConfig
from autoplex.auto.rss.flows import RssMaker
from jobflow_remote import submit_flow

rss_config = RssConfig.from_file('path/to/your/config.yaml')
rss_job = RssMaker(name="your workflow name", rss_config=rss_config).make()
resources = {"nodes": N, "partition": "name", "qos": "name", "time": "8:00:00", "mail_user": "your_email", "mail_type": "ALL", "account": "your account"}
print(submit_flow(rss_job, worker="your worker", resources=resources, project="your project name"))
```

For details on setting up `FireWorks`, see [FireWorks setup](../../../mongodb.md#fireworks-configuration) and for `jobflow-remote`, see [jobflow-remote setup](../../../jobflowremote.md).

## Running the workflow with direct parameter specification

As an alternative to using a RssConfig object, the RSS workflow can be initiated by directly specifying parameters in the `make` method. This approach is ideal for cases where only a few parameters need to be customized. 
You can override the default settings by passing them as keyword arguments, offering a more flexible and lightweight way to set up the workflow.

```python
rss_job = RssMaker(name="your workflow name").make(tag='Si',
                                                   buildcell_options=[{'NFORM': '{1,3,5}'},
                                                                      {'NFORM': '{2,4,6}'}],
                                                   hookean_repul=True, 
                                                   hookean_paras={'(14, 14)': (100, 1.2)})
```

If you choose to use the direct parameter specification method, at a minimum, you must provide the following arguments:

- `tag`: defines the system's elements and stoichiometry (only for compounds).  
- `buildcell_options`: controls the parameters for generating the initial randomized structures.
- `hookean_repul`: enables a strong repulsive force to avoid physically unrealistic structures.  
- `hookean_paras`: specifies the Hookean repulsion parameters.

> **Recommendation**: We strongly recommend enabling `hookean_repul`, as it applies a strong repulsive force when the distance between two atoms falls below a certain threshold. This ensures that the generated structures are physically reasonable.

> **Note**: If both a custom RssConfig object and direct parameter specifications are provided, any overlapping parameters will be overridden by the directly specified values.

## Building RSS models with various ML potentials

Currently, `RssMaker` supports GAP (Gaussian Approximation Potential), ACE (Atomic Cluster Expansion), and three graph-based network models including NequIP, M3GNet, and MACE. 
You can specify the desired model using the `mlip_type` argument and adjust relevant hyperparameters within the `make` method. 
Overview of default and adjustable hyperparameters for each model can be accessed using `MLIP_HYPERS` pydantic model of autoplex.

```python
from autoplex import MLIP_HYPERS
from autoplex.auto.rss.flows import RssMaker

print(MLIP_HYPERS.MACE) # Eg:- access MACE hyperparameters

# Intialize the workflow with the desired MLIP model
rss_job = RssMaker(name="your workflow name").make(tag='SiO2',
                                                   ... # Other parameters here
                                                   mlip_type='MACE',
                                                   {"MACE": "hidden_irreps":"128x0e + 128x1o","r_max":5.0},
                                                   )
```

> **Note**: We primarily recommend the GAP-RSS model for now, as GAP has demonstrated great stability with small datasets. Other models have not been thoroughly explored yet. However, we encourage users to experiment with and test other individual models or combinations for potentially interesting results.

## Resuming workflow from point of interruption

To resume an interrupted RSS workflow, use the `resume_from_previous_state` argument, which accepts a dictionary containing the necessary state information. Additionally, ensure that `train_from_scratch` is set to `False` to enable resuming from the previous state. This way, you are allowed to continue the workflow from any previously saved state.

```python
rss_job = RssMaker(name="your workflow name").make(tag='SiO2',
                                                   ... # Other parameters here
                                                   train_from_scratch=False,
                                                   resume_from_previous_state={'test_error': 0.24,
                                                   'pre_database_dir': 'path/to/pre-existing/database',
                                                   'mlip_path': 'path/to/previous/MLIP-model',
                                                   'isolated_atom_energies': {8: -0.16613333, 14: -0.16438578},
                                                   })
```
