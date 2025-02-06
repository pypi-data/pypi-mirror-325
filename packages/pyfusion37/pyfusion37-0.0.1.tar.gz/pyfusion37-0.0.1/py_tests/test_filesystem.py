import io
import json
from pathlib import Path
from typing import Any, Dict
from unittest import mock
from unittest.mock import MagicMock, patch

import asynctest
import fsspec
import pytest
from aiohttp import ClientResponse
from pytest_mock import MockerFixture

from fusion.credentials import FusionCredentials
from fusion.fusion_filesystem import FusionHTTPFileSystem


@pytest.fixture
def http_fs_instance(credentials_examples: Path) -> FusionHTTPFileSystem:
    """Fixture to create a new instance for each test."""
    creds = FusionCredentials.from_file(credentials_examples)
    return FusionHTTPFileSystem(credentials=creds)


def test_filesystem(
    example_creds_dict: Dict[str, Any], example_creds_dict_https_pxy: Dict[str, Any], tmp_path: Path
) -> None:
    credentials_file = tmp_path / "client_credentials.json"
    with Path(credentials_file).open("w") as f:
        json.dump(example_creds_dict, f)
    creds = FusionCredentials.from_file(credentials_file)
    assert FusionHTTPFileSystem(creds)

    credentials_file = tmp_path / "client_credentials.json"
    with Path(credentials_file).open("w") as f:
        json.dump(example_creds_dict_https_pxy, f)
    creds = FusionCredentials.from_file(credentials_file)
    assert FusionHTTPFileSystem(creds)

    kwargs = {"client_kwargs": {"credentials": creds}}

    assert FusionHTTPFileSystem(None, **kwargs)

    kwargs = {"client_kwargs": {"credentials": 3.14}}  # type: ignore
    with pytest.raises(ValueError, match="Credentials not provided"):
        FusionHTTPFileSystem(None, **kwargs)


@pytest.mark.asyncio
async def test_not_found_status(http_fs_instance: FusionHTTPFileSystem) -> None:
    response = asynctest.MagicMock(spec=ClientResponse)
    response.status = 404
    response.text = asynctest.CoroutineMock(return_value="404 NotFound")

    with pytest.raises(FileNotFoundError):
        await http_fs_instance._async_raise_not_found_for_status(response, "http://example.com")

@pytest.mark.asyncio
async def test_other_error_status(credentials: FusionCredentials) -> None:
    response = mock.MagicMock(spec=ClientResponse)
    response.status = 500
    response.text = asynctest.CoroutineMock(return_value="Internal server error")

    instance = FusionHTTPFileSystem(credentials)

    with mock.patch.object(instance, "_raise_not_found_for_status", side_effect=Exception("Custom error")):
        with pytest.raises(Exception, match="Custom error"):
            await instance._async_raise_not_found_for_status(response, "http://example.com")

        response.text.assert_awaited_once()
        assert response.reason == "Internal server error", "The reason should be updated to the response text"


@pytest.mark.asyncio
async def test_successful_status(http_fs_instance: FusionHTTPFileSystem) -> None:
    response = mock.MagicMock(spec=ClientResponse)
    response.status = 200
    response.text = asynctest.CoroutineMock(return_value="Success response body")

    try:
        await http_fs_instance._async_raise_not_found_for_status(response, "http://example.com")
    except FileNotFoundError as e:
        pytest.fail(f"No exception should be raised for a successful response, but got: {e}")


@pytest.mark.asyncio
async def test_decorate_url_with_http_async(http_fs_instance: FusionHTTPFileSystem) -> None:
    url = "resource/path"
    exp_res = f"{http_fs_instance.client_kwargs['root_url']}catalogs/{url}"
    result = await http_fs_instance._decorate_url_a(url)
    assert result == exp_res


@pytest.mark.asyncio
async def test_isdir_true(http_fs_instance: FusionHTTPFileSystem) -> None:
    http_fs_instance._decorate_url = asynctest.CoroutineMock(return_value="decorated_path_dir")  # type: ignore
    http_fs_instance._info = asynctest.CoroutineMock(return_value={"type": "directory"})
    result = await http_fs_instance._isdir("path_dir")
    assert result


@pytest.mark.asyncio
async def test_isdir_false(http_fs_instance: FusionHTTPFileSystem) -> None:
    http_fs_instance._decorate_url = asynctest.CoroutineMock(return_value="decorated_path_file")  # type: ignore
    http_fs_instance._info = asynctest.CoroutineMock(return_value={"type": "file"})
    result = await http_fs_instance._isdir("path_file")
    assert not result

@patch("requests.Session")
def test_stream_single_file(mock_session_class: MagicMock, example_creds_dict: Dict[str, Any], tmp_path: Path) -> None:
    url = "http://example.com/data"
    output_file = MagicMock(spec=fsspec.spec.AbstractBufferedFile)
    output_file.path = "./output_file_path/file.txt"
    output_file.name = "file.txt"

    credentials_file = tmp_path / "client_credentials.json"
    with Path(credentials_file).open("w") as f:
        json.dump(example_creds_dict, f)
    creds = FusionCredentials.from_file(credentials_file)

    # Create a mock response object with the necessary context manager methods
    mock_response = MagicMock()
    mock_response.raise_for_status = MagicMock()
    mock_response.iter_content = MagicMock(return_value=[b"0123456789", b""])
    # Mock the __enter__ method to return the mock response itself
    mock_response.__enter__.return_value = mock_response
    # Mock the __exit__ method to do nothing
    mock_response.__exit__.return_value = None

    # Set up the mock session to return the mock response
    mock_session = MagicMock()
    mock_session.get.return_value = mock_response
    mock_session_class.return_value = mock_session

    # Create an instance of FusionHTTPFileSystem
    http_fs_instance = FusionHTTPFileSystem(credentials=creds)
    http_fs_instance.sync_session = mock_session

    # Run the function
    results = http_fs_instance.stream_single_file(url, output_file)

    # Assertions to verify the behavior
    output_file.write.assert_any_call(b"0123456789")
    assert results == (True, output_file.path, None)


@patch("requests.Session")
def test_stream_single_file_exception(
    mock_session_class: MagicMock, example_creds_dict: Dict[str, Any], tmp_path: Path
) -> None:
    url = "http://example.com/data"
    output_file = MagicMock(spec=fsspec.spec.AbstractBufferedFile)
    output_file.path = "./output_file_path/file.txt"
    output_file.name = "file.txt"

    # Create a mock response object with the necessary context manager methods
    mock_response = MagicMock()
    mock_response.raise_for_status = MagicMock()
    mock_response.iter_content = MagicMock(side_effect=Exception("Test exception"))
    # Mock the __enter__ method to return the mock response itself
    mock_response.__enter__.return_value = mock_response
    # Mock the __exit__ method to do nothing
    mock_response.__exit__.return_value = None

    # Set up the mock session to return the mock response
    mock_session = MagicMock()
    mock_session.get.return_value = mock_response
    mock_session_class.return_value = mock_session

    credentials_file = tmp_path / "client_credentials.json"
    with Path(credentials_file).open("w") as f:
        json.dump(example_creds_dict, f)
    creds = FusionCredentials.from_file(credentials_file)

    # Create an instance of FusionHTTPFileSystem
    http_fs_instance = FusionHTTPFileSystem(credentials=creds)
    http_fs_instance.sync_session = mock_session

    # Run the function and catch the exception
    results = http_fs_instance.stream_single_file(url, output_file)

    # Assertions to verify the behavior
    output_file.close.assert_called_once()
    assert results == (False, output_file.path, "Test exception")

@pytest.mark.asyncio
async def test_download_single_file_async(
    mocker: MockerFixture,  # Add type annotation for mocker
    example_creds_dict: Dict[str, Any], 
    tmp_path: Path
) -> None:
    # Patching the function _run_coros_in_chunks with a mock
    mock_run_coros_in_chunks = mocker.patch("fsspec.asyn._run_coros_in_chunks", new_callable=mocker.AsyncMock)
    
    mock_run_coros_in_chunks.return_value = [True, True, True]

    url = "http://example.com/data"
    output_file = MagicMock(spec=io.IOBase)
    output_file.path = "./output_file_path/file.txt"
    file_size = 20
    chunk_size = 10
    n_threads = 3

    # Mock credentials file
    credentials_file = tmp_path / "client_credentials.json"
    with Path(credentials_file).open("w") as f:
        json.dump(example_creds_dict, f)
    creds = FusionCredentials.from_file(credentials_file)

    # Create the FusionHTTPFileSystem instance
    http_fs_instance = FusionHTTPFileSystem(credentials=creds)
    http_fs_instance.set_session = mocker.AsyncMock(return_value=mocker.AsyncMock())
    http_fs_instance._fetch_range = mocker.AsyncMock()

    # Run the download function
    result = await http_fs_instance._download_single_file_async(url, output_file, file_size, chunk_size, n_threads)

    # Assertions for successful download
    assert result == (True, output_file.path, None)
    output_file.close.assert_called_once()

    # Simulate an exception during the function call
    mock_run_coros_in_chunks.return_value = [Exception("Test exception")]
    result = await http_fs_instance._download_single_file_async(url, output_file, file_size, chunk_size, n_threads)

    # Assertions for failed download
    assert result == (False, output_file.path, "Test exception")
    output_file.close.assert_called()

@pytest.mark.asyncio
async def test_fetch_range_exception(
    mocker: MockerFixture,  # Add type annotation for mocker
    example_creds_dict: Dict[str, Any], 
    tmp_path: Path
) -> None:
    # Mock output file
    output_file = MagicMock(spec=io.IOBase)
    output_file.path = "./output_file_path/file.txt"
    output_file.seek = MagicMock()
    output_file.write = MagicMock()

    # Mock the response with an exception on read
    mock_response = mocker.MagicMock()
    mock_response.raise_for_status = mocker.MagicMock()
    mock_response.read = mocker.MagicMock(side_effect=Exception("Test exception"))
    mock_response.status = 500
    mock_response.__aenter__.return_value = mock_response
    mock_response.__aexit__.return_value = None

    # Mock the ClientSession
    mock_client_session = mocker.MagicMock()
    mock_client_session.get.return_value = mock_response
    mocker.patch("aiohttp.ClientSession", return_value=mock_client_session)

    # Mock credentials file
    credentials_file = tmp_path / "client_credentials.json"
    with Path(credentials_file).open("w") as f:
        json.dump(example_creds_dict, f)
    creds = FusionCredentials.from_file(credentials_file)

    # Create the FusionHTTPFileSystem instance
    http_fs_instance = FusionHTTPFileSystem(credentials=creds)
    http_fs_instance.kwargs = {}

    # Run the function (assuming you're testing a method that handles this exception)
    # You should assert what the function would do in the case of an exception
    await http_fs_instance._fetch_range(mock_client_session, "http://example.com/data", 0, 10, output_file)

    # Assertions
    output_file.seek.assert_not_called()
    output_file.write.assert_not_called()

@pytest.mark.asyncio
async def test_fetch_range_success(
    mocker: MockerFixture,  # Add type annotation for mocker
    example_creds_dict: Dict[str, Any], 
    tmp_path: Path
) -> None:
    url = "http://example.com/data"
    output_file = MagicMock(spec=io.IOBase)
    output_file.path = "./output_file_path/file.txt"
    output_file.seek = MagicMock()
    output_file.write = MagicMock()
    start = 0
    end = 10

    # Mocking the response
    mock_response = mocker.MagicMock()
    mock_response.raise_for_status = mocker.MagicMock()
    mock_response.read = mocker.MagicMock(return_value=b"some data")
    mock_response.status = 200
    mock_response.__aenter__.return_value = mock_response
    mock_response.__aexit__.return_value = None

    # Mocking the session
    mock_session = MagicMock()
    mock_session.get.return_value = mock_response
    mocker.patch("aiohttp.ClientSession", return_value=mock_session)

    # Mocking credentials file
    credentials_file = tmp_path / "client_credentials.json"
    with Path(credentials_file).open("w") as f:
        json.dump(example_creds_dict, f)
    creds = FusionCredentials.from_file(credentials_file)

    # Creating the FusionHTTPFileSystem instance
    http_fs_instance = FusionHTTPFileSystem(credentials=creds)
    http_fs_instance.kwargs = {}

    # Run the function
    await http_fs_instance._fetch_range(mock_session, url, start, end, output_file)

    # Assertions
    output_file.seek.assert_called_once_with(0)
    output_file.write.assert_called_once_with(b"some data")
    mock_response.raise_for_status.assert_not_called()
    mock_session.get.assert_called_once_with(url + f"?downloadRange=bytes={start}-{end-1}", **http_fs_instance.kwargs)