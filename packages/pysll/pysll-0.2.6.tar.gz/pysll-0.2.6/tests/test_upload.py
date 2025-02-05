import logging
import pathlib

from pysll import Constellation
from pysll.models import Object, VariableUnitValue


def test_simple_upload(client: Constellation):
    data = client.upload("Object.Example.Data", None, {})

    assert data["new_object"]
    assert data["type"] == "Object.Example.Data"


def test_upload_public_object(client: Constellation):
    data = client.upload("Object.Example.Data", None, {}, allow_public_objects=True)

    object_id = data["id"]
    notebook = client.download(Object(object_id), "Notebook")

    assert notebook is None


def test_single_upload_cloud_file(client, sample_file):
    """Create a dummy file and upload it as a cloud file."""

    file_name, contents = sample_file
    assert contents

    logging.info(f"uploading file {file_name} to cloud...")
    logging.info(contents)

    response = client.upload_cloud_file(file_name, None)
    resolved_object = response["resolved_object"]

    download_response = client.download(
        Object(resolved_object["id"]), ["id", "FileSize", "FileName", "FileType", "type"]
    )
    assert download_response[0] == resolved_object["id"]
    assert download_response[1] == VariableUnitValue(len(contents), "Bytes")
    assert download_response[2] == pathlib.Path(file_name).stem
    assert download_response[3] == '"txt"'
    assert download_response[4] == "Object.EmeraldCloudFile"
    assert "Notebook" not in download_response


def test_single_upload_cloud_file_with_notebook(client: Constellation, sample_file: tuple[str, str]):
    """Create a dummy file and upload it as a cloud file."""

    file_name, contents = sample_file
    assert contents

    logging.info(f"uploading file {file_name} to cloud...")
    logging.info(contents)

    response = client.upload_cloud_file(file_name, None)
    resolved_object = response["resolved_object"]

    download_response = client.download(
        Object(resolved_object["id"]), ["id", "FileSize", "FileName", "FileType", "type"]
    )
    assert download_response[0] == resolved_object["id"]
    assert download_response[1] == VariableUnitValue(len(contents), "Bytes")
    assert download_response[2] == pathlib.Path(file_name).stem
    assert download_response[3] == '"txt"'
    assert download_response[4] == "Object.EmeraldCloudFile"
    assert "Notebook" not in download_response
