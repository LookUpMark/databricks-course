"""Pydantic models for project configuration.

One model per configuration domain; ``Settings`` aggregates them all.
Every model validates its YAML source, so loading fails fast on bad config.
"""

from pydantic import BaseModel, ConfigDict, Field


class GeneralSettings(BaseModel):
    """Example project settings for consumers of the package configuration.

    Attributes:
        project_name: Logical project name.
        catalog: Example Unity Catalog catalog.
        schema_name: Example schema inside the configured catalog.
        log_level: Logging level for callers configuring Loguru.
    """

    model_config = ConfigDict(serialize_by_alias=True)

    project_name: str
    catalog: str
    schema_name: str = Field(alias="schema")
    log_level: str = Field(default="INFO")

    @property
    def schema(self) -> str:
        """Return the schema under its existing Python attribute name."""
        return self.schema_name


class MlSettings(BaseModel):
    """MLflow and model-serving settings.

    Attributes:
        experiment_root: Root path for experiments under the user workspace.
        agent_experiment: Experiment path for agent development.
        chat_endpoint: Serving endpoint of the chat model used by agents.
        registry_schema: Unity Catalog schema holding registered models.
    """

    experiment_root: str
    agent_experiment: str
    chat_endpoint: str
    registry_schema: str


class EtlSettings(BaseModel):
    """Medallion ETL settings.

    Attributes:
        scratch_schema: Schema holding the medallion tables.
        bronze_table: Raw events table name.
        silver_table: Cleaned events table name.
        gold_table: Customer totals aggregate table name.
        checkpoint_template: Path template for Auto Loader checkpoints, with
            ``{catalog}``, ``{scratch_schema}`` and ``{table}`` placeholders.
    """

    scratch_schema: str
    bronze_table: str
    silver_table: str
    gold_table: str
    checkpoint_template: str


class Settings(BaseModel):
    """Aggregate of all configuration domains.

    Attributes:
        general: Project identity and defaults.
        ml: MLflow and model serving.
        etl: Medallion pipeline settings.
    """

    general: GeneralSettings
    ml: MlSettings
    etl: EtlSettings
