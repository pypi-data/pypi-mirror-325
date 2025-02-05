import logging
from typing import IO, Any, Dict, List, Optional, Union

import requests

from .. import _storage, config
from ..enums import DataSourceLabel, FileType
from ..exceptions import ForecastFlowError
from ..training import TrainingSettings

logger = logging.getLogger(__name__)


def _get(id_token: str, endpoint: str, params: Dict[str, Any]) -> Any:
    response = requests.get(
        f"{config.forecastflow['api_base_url']}/{endpoint}",
        params=params,
        headers={"Authorization": f"Bearer {id_token}"},
    )
    try:
        response_json = response.json()
    except ValueError:
        raise ForecastFlowError(response.text)
    raise_error_from_response(response_json)
    return response_json


def _post(id_token: str, endpoint: str, data: Dict[str, Any]) -> Any:
    response = requests.post(
        f"{config.forecastflow['api_base_url']}/{endpoint}",
        json=data,
        headers={"Authorization": f"Bearer {id_token}"},
    )
    try:
        response_json = response.json()
    except ValueError:
        raise ForecastFlowError(response.text)
    raise_error_from_response(response_json)
    return response_json


def raise_error_from_response(response: Dict[str, Any]):
    if "error" in response:
        raise ForecastFlowError(
            f'{response["error"]["reason"]}: {response["error"]["message"]}'
        )


def create_data_source(
    id_token: str,
    team_id: Optional[str],
    pid: str,
    name: str,
    label: "DataSourceLabel",
    filetype: "FileType",
    num_files: int,
    description: "Optional[str]" = None,
) -> "Dict[str, Any]":
    """
    Create data source in project.
    NOTE: This function doesn't create profile.
    """
    response = _post(
        id_token,
        "v3/createdatasource",
        data={
            "idToken": id_token,
            "teamId": team_id,
            "pid": pid,
            "name": name,
            "desc": description or "",
            "label": label.value,
            "type": filetype.value,
            "numFiles": num_files,
        },
    )
    logger.info("Successfully created data source")
    return response["message"]


def profile(
    id_token: str,
    team_id: Optional[str],
    pid: str,
    did: str,
):
    _post(
        id_token,
        "v3/profile",
        data={"idToken": id_token, "teamId": team_id, "pid": pid, "did": did},
    )
    logger.info("ForecastFlow profiler is starting")


def create_data_source_from_files(
    id_token: str,
    team_id: Optional[str],
    pid: str,
    files: Union[List[str], List[IO]],
    filetype: "FileType",
    name: str,
    label: DataSourceLabel,
    description: Optional[str] = None,
) -> str:
    """
    Create data source and profile from file
    """
    if len(files) > 999:
        raise ValueError("Too many files to create datasource.")
    message = create_data_source(
        id_token=id_token,
        team_id=team_id,
        pid=pid,
        name=name,
        label=label,
        filetype=filetype,
        description=description,
        num_files=len(files),
    )
    did = message["did"]
    uris = [f["uri"] for f in message["files"]]
    for file, uri in zip(files, uris):
        _storage.upload(file=file, uri=uri, filetype=filetype, id_token=id_token)
    return did


def create_model(
    id_token: str,
    team_id: Optional[str],
    name: str,
    train_settings: Union[dict, "TrainingSettings"],
    train_pid: str,
    train_did: str,
    test_pid: Optional[str] = None,
    test_did: Optional[str] = None,
    test_frac: Optional[float] = None,
    description: Optional[str] = None,
) -> str:
    if isinstance(train_settings, TrainingSettings):
        train_settings = train_settings.to_dict()
    if not isinstance(train_settings, dict):
        raise TypeError("train_settings must be dict or TrainingSettings")

    data: Dict[str, Any] = {
        "idToken": id_token,
        "name": name,
        "desc": description or "",
        "trainData": {"pid": train_pid, "did": train_did},
        "trainSettings": train_settings,
    }
    if team_id is not None:
        data.update({"teamId": team_id})

    if isinstance(test_frac, float):
        data["percentTest"] = int(100 * test_frac)
    elif test_pid is not None and test_did is not None:
        data["testData"] = {"pid": test_pid, "did": test_did}
    else:
        raise ValueError("Lack of information for test data")

    response = _post(id_token, "v3/createmodel", data=data)
    return response["mid"]


def create_prediction(
    id_token: str,
    name: str,
    description: str,
    team_id: Optional[str],
    pid: str,
    did: str,
    mid: str,
    filetype: "FileType",
) -> str:
    response = _post(
        id_token,
        "v3/createpredict",
        data={
            "idToken": id_token,
            "name": name,
            "desc": description,
            "teamId": team_id,
            "did": did,
            "mid": mid,
            "pid": pid,
            "type": filetype.value,
        },
    )
    return response["rid"]


def get_data_source_info(
    id_token: str,
    team_id: Optional[str],
    pid: str,
    did: str,
) -> "Dict":
    """Get data-source info.

    Args:
        id_token: id token.
        pid: Project ID.
        did: DataSource ID.
    """
    response = _post(
        id_token,
        "v3/getdatasourceinfo",
        data={"idToken": id_token, "teamId": team_id, "pid": pid, "did": did},
    )
    return response


def get_model_info(
    id_token: str,
    team_id: Optional[str],
    pid: str,
    mid: str,
) -> "Dict":
    """Get model info.

    Args:
        id_token: id token.
        pid: Project ID.
        mid: Model ID.
    """
    response = _post(
        id_token,
        "v3/getmodelinfo",
        data={"idToken": id_token, "teamId": team_id, "pid": pid, "mid": mid},
    )
    return response


def get_model_importances(
    id_token: str,
    team_id: Optional[str],
    pid: str,
    mid: str,
) -> "Dict":
    """Get model importances info.

    Args:
        id_token: id token.
        pid: Project ID.
        mid: Model ID.
    """
    response = _post(
        id_token,
        "v3/getimportancesinfo",
        data={"idToken": id_token, "teamId": team_id, "pid": pid, "mid": mid},
    )
    return response


def get_prediction_info(
    id_token: str,
    team_id: Optional[str],
    pid: str,
    rid: str,
) -> "Dict":
    """Get prediction info.

    Args:
        id_token: id token.
        pid: Project ID.
        rid: Prediction ID.
    """
    response = _post(
        id_token,
        "v3/getpredictioninfo",
        data={"idToken": id_token, "teamId": team_id, "pid": pid, "rid": rid},
    )
    return response


def get_project_info(
    id_token: str,
    team_id: Optional[str],
    pid: str,
) -> "Dict":
    """Get project info.

    Args:
        id_token: id token.
        pid: Project ID.
    """
    response = _post(
        id_token,
        "v3/getprojectinfo",
        data={"idToken": id_token, "teamId": team_id, "pid": pid},
    )
    return response


def list_teams_info(id_token: str) -> List[dict]:
    """Fetch list of teams from server.

    Args:
        id_token (str): ID token used for authorization.

    Returns:
        List of teams belong to authorized user.
    """
    return _post(
        id_token=id_token, endpoint="v3/listteamsinfo", data={"idToken": id_token}
    )


def list_projects_info(
    id_token: str,
    team_id: Optional[str],
    current_page: int,
    items_per_page: int,
    order_type: str,
) -> dict:
    """Fetch list of projects from server.

    Args:
        id_token (str): id token used for authorization
        team_id (str, optional): ForecastFlow team ID
        current_page (int): Current page number
        items_per_page (int): Number of items per page
        order_type (str): asc or desc to order items by created date

    Returns:
        List of projects and pagination info.
    """
    return _post(
        id_token=id_token,
        endpoint="v3/listprojectsinfo",
        data={
            "idToken": id_token,
            "teamId": team_id,
            "currentPage": current_page,
            "itemsPerPage": items_per_page,
            "orderType": order_type,
        },
    )


def list_data_sources_info(
    id_token: str,
    team_id: Optional[str],
    pid: str,
    label_to_filter: Optional[DataSourceLabel],
    current_page: int,
    items_per_page: int,
    order_type: str,
) -> dict:
    """Fetch list of data sources from server.

    Args:
        id_token (str): id token used for authorization
        team_id (str, optional): ForecastFlow team ID
        pid (str): ForecastFlow project ID
        label_to_filter (DataSourceLabel, optional): Label type filtering data sources
        current_page (int): Current page number
        items_per_page (int): Number of items per page
        order_type (str): asc or desc to order items by created date

    Returns:
        List of data sources and pagination info.
    """

    # NOTE: Since DataSourceLabel is not JSON serializable,
    #       it needs to pass as enum's value here.
    if label_to_filter is not None:
        label_to_filter = label_to_filter.value

    return _post(
        id_token=id_token,
        endpoint="v3/listdatasourcesinfo",
        data={
            "idToken": id_token,
            "teamId": team_id,
            "pid": pid,
            "labelToFilter": label_to_filter,
            "currentPage": current_page,
            "itemsPerPage": items_per_page,
            "orderType": order_type,
        },
    )


def list_models_info(
    id_token: str,
    team_id: Optional[str],
    pid: str,
    current_page: int,
    items_per_page: int,
    order_type: str,
) -> dict:
    """Fetch list of models from server.

    Args:
        id_token (str): id token used for authorization
        team_id (str, optional): ForecastFlow team ID
        pid (str): ForecastFlow project ID
        current_page (int): Current page number
        items_per_page (int): Number of items per page
        order_type (str): asc or desc to order items by created date

    Returns:
        List of models and pagination info.
    """
    return _post(
        id_token=id_token,
        endpoint="v3/listmodelsinfo",
        data={
            "idToken": id_token,
            "teamId": team_id,
            "pid": pid,
            "currentPage": current_page,
            "itemsPerPage": items_per_page,
            "orderType": order_type,
        },
    )


def list_predictions_info(
    id_token: str,
    team_id: Optional[str],
    pid: str,
    mid: Optional[str],
    current_page: int,
    items_per_page: int,
    order_type: str,
):
    """Fetch list of predictions from server.

    Args:
        id_token (str): id token used for authorization
        team_id (str, optional): ForecastFlow team ID
        pid (str): ForecastFlow project ID
        mid (str, optional): ForecastFlow model ID
        current_page (int): Current page number
        items_per_page (int): Number of items per page
        order_type (str): asc or desc to order items by created date

    Returns:
        List of predictions and pagination info.
    """
    return _post(
        id_token=id_token,
        endpoint="v3/listpredictionsinfo",
        data={
            "idToken": id_token,
            "teamId": team_id,
            "pid": pid,
            "mid": mid,
            "currentPage": current_page,
            "itemsPerPage": items_per_page,
            "orderType": order_type,
        },
    )


def bulk_delete_data_sources(
    id_token: str, team_id: str, pid: str, dids: List[str], with_prediction: bool
) -> dict:
    return _post(
        id_token=id_token,
        endpoint="v3/bulkdeletedatasources",
        data={
            "idToken": id_token,
            "teamId": team_id,
            "pid": pid,
            "dids": dids,
            "withPrediction": with_prediction,
        },
    )


def delete_model(id_token: str, team_id: str, pid: str, mid: str):
    return _post(
        id_token=id_token,
        endpoint="v3/deletemodel",
        data={"idToken": id_token, "teamId": team_id, "pid": pid, "mid": mid},
    )


def delete_predict(id_token: str, team_id: str, pid: str, rid: str):
    return _post(
        id_token=id_token,
        endpoint="v3/deletepredict",
        data={"idToken": id_token, "teamId": team_id, "pid": pid, "rid": rid},
    )
