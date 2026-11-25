# src/playbook/config/ml.yaml (ML domain)

MLflow tracking and model-serving configuration.

| Key | Model field | Meaning |
|---|---|---|
| `experiment_root` | `MlSettings.experiment_root` | Root path for experiments under the user workspace |
| `agent_experiment` | `MlSettings.agent_experiment` | Experiment path for agent development |
| `chat_endpoint` | `MlSettings.chat_endpoint` | Optional model serving endpoint for package extensions; empty until configured |
| `registry_schema` | `MlSettings.registry_schema` | UC schema holding registered models |

The YAML keys belong to the sample package configuration. The course notebooks choose their own experiment paths. Topic 05 takes a workspace-approved model endpoint from its `chat_endpoint` widget.
