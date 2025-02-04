from dataclasses import dataclass
from logging import getLogger
from pathlib import Path
from typing import List

import yaml

from beamlit.common.settings import Settings

logger = getLogger(__name__)


@dataclass
class Credentials:
    apiKey: str = ""
    access_token: str = ""
    refresh_token: str = ""
    expires_in: int = 0
    device_code: str = ""
    client_credentials: str = ""


@dataclass
class WorkspaceConfig:
    name: str
    credentials: Credentials


@dataclass
class ContextConfig:
    workspace: str = ""
    environment: str = ""


@dataclass
class Config:
    workspaces: List[WorkspaceConfig] = None
    context: ContextConfig = None

    def __post_init__(self):
        if self.workspaces is None:
            self.workspaces = []
        if self.context is None:
            self.context = ContextConfig()

    def to_json(self) -> dict:
        return {
            "workspaces": [
                {
                    "name": ws.name,
                    "credentials": {
                        "apiKey": ws.credentials.apiKey,
                        "access_token": ws.credentials.access_token,
                        "refresh_token": ws.credentials.refresh_token,
                        "expires_in": ws.credentials.expires_in,
                        "device_code": ws.credentials.device_code,
                        "client_credentials": ws.credentials.client_credentials,
                    },
                }
                for ws in self.workspaces
            ],
            "context": {
                "workspace": self.context.workspace,
                "environment": self.context.environment,
            },
        }


def load_config() -> Config:
    config = Config()
    home_dir = Path.home()
    if home_dir:
        config_path = home_dir / ".beamlit" / "config.yaml"
        if config_path.exists():
            try:
                with open(config_path) as f:
                    data = yaml.safe_load(f)
                    if data:
                        workspaces = []
                        for ws in data.get("workspaces", []):
                            creds = Credentials(**ws.get("credentials", {}))
                            workspaces.append(WorkspaceConfig(name=ws["name"], credentials=creds))
                        config.workspaces = workspaces
                        if "context" in data:
                            config.context = ContextConfig(**data["context"])
            except yaml.YAMLError:
                # Invalid YAML, use empty config
                pass
    return config


def save_config(config: Config):
    home_dir = Path.home()
    if not home_dir:
        raise RuntimeError("Could not determine home directory")

    config_dir = home_dir / ".beamlit"
    config_file = config_dir / "config.yaml"

    config_dir.mkdir(mode=0o700, parents=True, exist_ok=True)
    with open(config_file, "w", encoding="utf-8") as f:
        yaml.dump(config.to_json(), f)


def list_workspaces() -> List[str]:
    config = load_config()
    return [workspace.name for workspace in config.workspaces]


def current_context() -> ContextConfig:
    config = load_config()
    return config.context


def set_current_workspace(workspace_name: str, environment: str):
    config = load_config()
    config.context.workspace = workspace_name
    config.context.environment = environment
    save_config(config)


def load_credentials(workspace_name: str) -> Credentials:
    config = load_config()
    for workspace in config.workspaces:
        if workspace.name == workspace_name:
            return workspace.credentials
    return Credentials()


def load_credentials_from_settings(settings: Settings) -> Credentials:
    return Credentials(
        apiKey=settings.authentication.apiKey,
        client_credentials=settings.authentication.client.credentials,
    )


def create_home_dir_if_missing():
    home_dir = Path.home()
    if not home_dir:
        logger.error("Error getting home directory")
        return

    credentials_dir = home_dir / ".beamlit"
    credentials_file = credentials_dir / "credentials.json"

    if credentials_file.exists():
        logger.warning("You are already logged in. Enter a new API key to overwrite it.")
    else:
        try:
            credentials_dir.mkdir(mode=0o700, parents=True, exist_ok=True)
        except Exception as e:
            logger.error(f"Error creating credentials directory: {e}")


def save_credentials(workspace_name: str, credentials: Credentials):
    create_home_dir_if_missing()
    if not credentials.access_token and not credentials.apiKey:
        logger.info("No credentials to save, error")
        return

    config = load_config()
    found = False

    for i, workspace in enumerate(config.workspaces):
        if workspace.name == workspace_name:
            config.workspaces[i].credentials = credentials
            found = True
            break

    if not found:
        config.workspaces.append(WorkspaceConfig(name=workspace_name, credentials=credentials))

    save_config(config)


def clear_credentials(workspace_name: str):
    config = load_config()
    config.workspaces = [ws for ws in config.workspaces if ws.name != workspace_name]

    if config.context.workspace == workspace_name:
        config.context.workspace = ""

    save_config(config)
