# src/playbook/config/settings.yaml (general domain)

Example values for code that consumes the package settings.

| Key | Model field | Meaning |
|---|---|---|
| `project_name` | `GeneralSettings.project_name` | Example logical project name |
| `catalog` | `GeneralSettings.catalog` | Example Unity Catalog catalog |
| `schema` | `GeneralSettings.schema_name` (also available as `.schema`) | Example schema inside `catalog` |
| `log_level` | `GeneralSettings.log_level` | Example log level for callers configuring Loguru |

The model defaults `log_level` to `INFO` and requires the other three fields. The bundle sets its resource names and destination in YAML. The wheel receives its catalog and schema as required arguments and configures logging at `INFO`.
