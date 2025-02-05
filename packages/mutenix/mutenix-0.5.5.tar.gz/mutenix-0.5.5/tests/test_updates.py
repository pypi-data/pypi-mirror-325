# SPDX-License-Identifier: MIT
# Copyright (c) 2025 Matthias Bilger matthias@bilger.info
from __future__ import annotations

import os
import pathlib
import unittest
from unittest.mock import MagicMock
from unittest.mock import mock_open
from unittest.mock import patch

import requests
from mutenix.hid_commands import HardwareTypes
from mutenix.updates import check_for_device_update
from mutenix.updates import check_for_self_update
from mutenix.updates import VersionInfo
from mutenix.updates.chunks import Chunk
from mutenix.updates.chunks import FileChunk
from mutenix.updates.chunks import FileDelete
from mutenix.updates.chunks import FileEnd
from mutenix.updates.chunks import FileStart
from mutenix.updates.constants import MAX_CHUNK_SIZE
from mutenix.updates.device_messages import ChunkAck
from mutenix.updates.device_messages import UpdateError
from mutenix.updates.device_update import perform_hid_upgrade
from mutenix.updates.device_update import TransferFile


class TestUpdates(unittest.TestCase):
    @patch("mutenix.updates.requests.get")
    @patch("mutenix.updates.semver.compare")
    def test_check_for_device_update_up_to_date(self, mock_compare, mock_get):
        mock_compare.return_value = 0
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"tag_name": "v1.0.0"}
        device_version = VersionInfo(
            buffer=bytes([1, 0, 0, HardwareTypes.UNKNOWN.value, 0, 0, 0, 0]),
        )
        mock_device = MagicMock()
        check_for_device_update(mock_device, device_version)

        mock_get.assert_called_once()

    @patch("mutenix.updates.requests.get")
    @patch("mutenix.updates.semver.compare")
    @patch("mutenix.updates.device_update.perform_hid_upgrade")
    def test_check_for_device_update_needs_update(
        self,
        mock_upgrade,
        mock_compare,
        mock_get,
    ):
        mock_compare.return_value = -1
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "tag_name": "v2.0.0",
            "assets": [
                {
                    "name": "v2.0.0.tar.gz",
                    "browser_download_url": "http://example.com/update.tar.gz",
                },
            ],
        }

        mock_update_response = MagicMock()
        mock_update_response.status_code = 200
        mock_update_response.content = b"fake content"
        mock_get.side_effect = [mock_get.return_value, mock_update_response]

        device_version = VersionInfo(
            buffer=bytes([1, 0, 0, HardwareTypes.UNKNOWN.value, 0, 0, 0, 0]),
        )
        with patch("tarfile.open") as mock_tarfile:
            mock_tarfile.return_value.__enter__.return_value.extractall = MagicMock()
            mock_device = MagicMock()
            check_for_device_update(mock_device, device_version)

        mock_get.assert_called()
        mock_upgrade.assert_called_once()

    @patch("mutenix.updates.requests.get")
    def test_check_for_device_update_no_response(self, mock_get):
        mock_get.return_value.status_code = 500
        mock_get.return_value.json.return_value = None
        device_version = VersionInfo(
            buffer=bytes([1, 0, 0, HardwareTypes.UNKNOWN.value, 0, 0, 0, 0]),
        )
        mock_device = MagicMock()
        check_for_device_update(mock_device, device_version)

        mock_get.assert_called_once()

    @patch("mutenix.updates.requests.get")
    @patch("mutenix.updates.semver.compare")
    @patch("mutenix.updates.device_update.perform_hid_upgrade")
    def test_check_for_device_update_needs_update_but_fails(
        self,
        mock_upgrade,
        mock_compare,
        mock_get,
    ):
        mock_compare.return_value = -1
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "tag_name": "v2.0.0",
            "assets": [
                {
                    "name": "v2.0.0",
                    "browser_download_url": "http://example.com/update.tar.gz",
                },
            ],
        }

        mock_update_response = MagicMock()
        mock_update_response.side_effect = requests.RequestException("Network error")
        mock_get.side_effect = [
            mock_get.return_value,
            requests.RequestException("Network error"),
        ]

        device_version = VersionInfo(
            buffer=bytes([1, 0, 0, HardwareTypes.UNKNOWN.value, 0, 0, 0, 0]),
        )

        mock_device = MagicMock()
        check_for_device_update(mock_device, device_version)

        mock_get.assert_called()
        mock_upgrade.assert_not_called()

    @patch("mutenix.updates.requests.get")
    @patch("mutenix.updates.semver.compare")
    def test_check_for_self_update_up_to_date(self, mock_compare, mock_get):
        mock_compare.return_value = 0
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"tag_name": "v1.0.0"}

        check_for_self_update(1, 0, 0)

        mock_get.assert_called_once()

    @patch("mutenix.updates.requests.get")
    def test_check_for_device_update_request_exception(self, mock_get):
        mock_get.side_effect = requests.RequestException("Network error")
        device_version = VersionInfo(
            buffer=bytes([1, 0, 0, HardwareTypes.UNKNOWN.value, 0, 0, 0, 0]),
        )
        mock_device = MagicMock()

        with self.assertLogs("mutenix.updates", level="ERROR") as log:
            check_for_device_update(mock_device, device_version)

        mock_get.assert_called_once()
        self.assertIn("Failed to check for device update availability", log.output[0])

    @patch("mutenix.updates.requests.get")
    @patch("mutenix.updates.semver.compare")
    def test_check_for_self_update_needs_update(self, mock_compare, mock_get):
        mock_compare.return_value = -1
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "tag_name": "v2.0.0",
            "html_url": "http://example.com",
        }

        mock_update_response = MagicMock()
        mock_update_response.status_code = 200
        mock_update_response.content = b"fake content"
        mock_get.side_effect = [mock_get.return_value, mock_update_response]

        with patch("webbrowser.open"):
            check_for_self_update(1, 0, 0)

        mock_get.assert_called()

    @patch("mutenix.updates.device_update.hid.device")
    @patch("python_minifier.minify", side_effect=lambda x, *args, **kwargs: str(x))
    def test_perform_hid_upgrade_success(self, mock_device, mock_minify):
        mock_device_instance = MagicMock()
        mock_device.return_value = mock_device_instance

        mock_device_instance.read.side_effect = [
            bytes(),
            bytes([2, 65, 75, 0, 0, 0, 0, 1, 0, 0]),  # Acknowledge for first file
            bytes([2, 65, 75, 0, 0, 0, 0, 2, 0, 0]),  # Acknowledge for first file
            bytes([2, 65, 75, 0, 0, 0, 0, 3, 0, 0]),  # Acknowledge for first file
            bytes([2, 65, 75, 1, 0, 0, 0, 1, 0, 0]),  # Acknowledge for first file
            bytes([2, 65, 75, 1, 0, 0, 0, 2, 0, 0]),  # Acknowledge for first file
            bytes([2, 65, 75, 1, 0, 0, 0, 3, 0, 0]),  # Acknowledge for first file
            bytes([2, 65, 75, 2, 0, 0, 0, 1, 0, 0]),  # Acknowledge for first file
            bytes([2, 65, 75, 2, 0, 0, 0, 2, 0, 0]),  # Acknowledge for first file
            bytes([2, 65, 75, 2, 0, 0, 0, 3, 0, 0]),  # Acknowledge for first file
            bytes(),
            bytes(),
            bytes(),
            bytes(),
            bytes(),
            bytes(),
        ]

        with patch("mutenix.updates.constants.DATA_TRANSFER_SLEEP_TIME", 0.0001):
            with patch("mutenix.updates.constants.STATE_CHANGE_SLEEP_TIME", 0.0001):
                with patch("builtins.open", mock_open(read_data=b"fake content")):
                    with patch("pathlib.Path.is_file", return_value=True):
                        with patch(
                            "pathlib.Path.open",
                            mock_open(read_data=b"fake content"),
                        ):
                            perform_hid_upgrade(
                                mock_device_instance,
                                ["file1.py", "file2.py", "file3.py"],
                            )

        self.assertEqual(
            mock_device_instance.write.call_count,
            10,
        )  # 3 files * 3 chunks each + 1 state change commands

    @patch("mutenix.updates.device_update.hid.device")
    @patch("python_minifier.minify", side_effect=lambda x, *args, **kwargs: str(x))
    def test_perform_hid_upgrade_ack(self, mock_device, mock_minify):
        mock_device_instance = MagicMock()
        mock_device.return_value = mock_device_instance

        mock_device_instance.read.side_effect = [
            bytes(),  # No more requests
            bytes([2, 65, 75, 0, 0, 0, 0, 1, 0, 0]),  # Acknowledge for first file
            bytes([2, 65, 75, 0, 0, 0, 0, 2, 0, 0]),  # Acknowledge for first file
            bytes([2, 65, 75, 0, 0, 0, 0, 3, 0, 0]),  # Acknowledge for first file
            bytes(),  # No more requests
            bytes(),  # No more requests
            bytes(),  # No more requests
            bytes(),  # No more requests
            bytes(),  # No more requests
            bytes(),  # No more requests
        ]

        with patch("mutenix.updates.constants.DATA_TRANSFER_SLEEP_TIME", 0.0001):
            with patch("mutenix.updates.constants.STATE_CHANGE_SLEEP_TIME", 0.0001):
                with patch("builtins.open", mock_open(read_data=b"fake content")):
                    with patch("pathlib.Path.is_file", return_value=True):
                        with patch(
                            "pathlib.Path.open",
                            mock_open(read_data=b"fake content"),
                        ):
                            perform_hid_upgrade(mock_device_instance, ["file1.py"])

    @patch("mutenix.updates.requests.get")
    def test_check_for_self_update_request_error(self, mock_get):
        mock_get.side_effect = requests.RequestException("Network error")

        with self.assertLogs("mutenix.updates", level="ERROR") as log:
            check_for_self_update(1, 0, 0)

        self.assertIn(
            "Failed to check for application update availability",
            log.output[0],
        )

    @patch("mutenix.updates.requests.get")
    def test_check_for_self_update_status_code_error(self, mock_get):
        mock_get.return_value.status_code = 500

        with self.assertLogs("mutenix.updates", level="ERROR") as log:
            check_for_self_update(1, 0, 0)

        self.assertIn(
            "Failed to fetch latest release info, status code: 500",
            log.output[0],
        )


class TestFileChunk(unittest.TestCase):
    def test_file_chunk_packet(self):
        chunk = FileChunk(1, 2, 3, b"content")
        packet = chunk.packet()
        self.assertEqual(packet[:2], (2).to_bytes(2, "little"))
        self.assertEqual(packet[2:4], (1).to_bytes(2, "little"))
        self.assertEqual(packet[4:6], (3).to_bytes(2, "little"))
        self.assertEqual(packet[6:8], (2).to_bytes(2, "little"))
        self.assertEqual(packet[8:16], b"content" + b"\0")


class TestFileStart(unittest.TestCase):
    def test_file_start_packet(self):
        start = FileStart(1, 0, 3, "test.py", 100)
        packet = start.packet()
        self.assertEqual(packet[:2], (1).to_bytes(2, "little"))
        self.assertEqual(packet[2:4], (1).to_bytes(2, "little"))
        self.assertEqual(packet[4:6], (3).to_bytes(2, "little"))
        self.assertEqual(packet[6:8], (0).to_bytes(2, "little"))
        self.assertEqual(packet[8:9], bytes((7,)))
        self.assertEqual(
            packet[9:19],
            b"test.py" + bytes((2,)) + (100).to_bytes(2, "little"),
        )


class TestFileEnd(unittest.TestCase):
    def test_file_end_packet(self):
        end = FileEnd(1)
        packet = end.packet()
        self.assertEqual(packet[:2], (3).to_bytes(2, "little"))
        self.assertEqual(packet[2:4], (1).to_bytes(2, "little"))
        self.assertEqual(packet[4:], b"\0" * (MAX_CHUNK_SIZE + 4))


class TestTransferFile(unittest.TestCase):
    def setUp(self):
        self.file_content = b"fake content" * 10
        self.file_path = "test_file.py"
        with open(self.file_path, "wb") as f:
            f.write(self.file_content)

    def tearDown(self):
        os.remove(self.file_path)

    @patch("python_minifier.minify", side_effect=lambda x, *args, **kwargs: str(x))
    def test_transfer_file_chunks(self, mock_minify):
        transfer_file = TransferFile(1, self.file_path)
        self.assertEqual(transfer_file.size, len(self.file_content))
        self.assertEqual(len(transfer_file._chunks), transfer_file.chunks)

    @patch("python_minifier.minify", side_effect=lambda x, *args, **kwargs: str(x))
    def test_transfer_file_get_next_chunk(self, mock_minify):
        transfer_file = TransferFile(1, self.file_path)
        chunk = transfer_file.get_next_chunk()
        self.assertIsInstance(chunk, Chunk)

    @patch("python_minifier.minify", side_effect=lambda x, *args, **kwargs: str(x))
    def test_transfer_file_is_complete(self, mock_minify):
        transfer_file = TransferFile(1, self.file_path)
        while not transfer_file.is_complete():
            chunk = transfer_file.get_next_chunk()
            if chunk:
                dfc = ChunkAck(
                    b"AK"
                    + (chunk.id).to_bytes(2, "little")
                    + (chunk.package).to_bytes(2, "little")
                    + (chunk.type_).to_bytes(1, "little")
                    + b"\0" * 2,
                )
                dfc.type_ = chunk.type_
                dfc.package = chunk.package
                transfer_file.acknowledge_chunk(dfc)
        self.assertTrue(transfer_file.is_complete())

    @patch("python_minifier.minify", side_effect=lambda x, *args, **kwargs: str(x))
    def test_transfer_file_from_path(self, mock_minify):
        transfer_file = TransferFile(1, pathlib.Path(self.file_path))
        self.assertEqual(transfer_file.filename, "test_file.py")
        self.assertEqual(transfer_file.size, len(self.file_content))


class TestPerformHidUpgradeError(unittest.TestCase):
    @patch("mutenix.updates.hid.device")
    @patch("python_minifier.minify", side_effect=lambda x, *args, **kwargs: str(x))
    def test_perform_hid_upgrade_error(self, mock_device, mock_minify):
        mock_device_instance = MagicMock()
        mock_device.return_value = mock_device_instance

        mock_device_instance.read.side_effect = [
            bytes([2, 69, 82, 5, 69, 114, 114, 111, 114]),  # Error
        ]

        with patch("mutenix.updates.constants.DATA_TRANSFER_SLEEP_TIME", 0.0001):
            with patch("mutenix.updates.constants.STATE_CHANGE_SLEEP_TIME", 0.0001):
                with patch("builtins.open", mock_open(read_data=b"fake content")):
                    with patch("pathlib.Path.is_file", return_value=True):
                        with patch(
                            "pathlib.Path.open",
                            mock_open(read_data=b"fake content"),
                        ):
                            with self.assertLogs(
                                "mutenix.updates",
                                level="ERROR",
                            ) as log:
                                perform_hid_upgrade(mock_device_instance, ["file1.py"])

        self.assertIn("Error received from device: Error", log.output[0])


class TestTransferFileInit(unittest.TestCase):
    def setUp(self):
        self.file_content = b"fake content" * 10
        self.file_path = "test_file.py"
        with open(self.file_path, "wb") as f:
            f.write(self.file_content)

    def tearDown(self):
        os.remove(self.file_path)

    @patch("python_minifier.minify", side_effect=lambda x, *args, **kwargs: str(x))
    def test_transfer_file_init(self, mock_minify):
        transfer_file = TransferFile(1, self.file_path)
        self.assertEqual(transfer_file.id, 1)
        self.assertEqual(transfer_file.filename, "test_file.py")
        self.assertEqual(transfer_file.size, len(self.file_content))
        self.assertEqual(len(transfer_file._chunks), transfer_file.chunks)

    def test_transfer_file_init_delete(self):
        delete_file_path = "test_file.py.delete"
        with open(delete_file_path, "wb") as f:
            f.write(self.file_content)
        transfer_file = TransferFile(1, delete_file_path)
        self.assertEqual(transfer_file.id, 1)
        self.assertEqual(transfer_file.filename, "test_file.py")
        self.assertEqual(len(transfer_file._chunks), 1)
        self.assertIsInstance(transfer_file._chunks[0], FileDelete)
        os.remove(delete_file_path)


class TestChunkAck(unittest.TestCase):
    def test_chunk_ack_str_valid(self):
        data = (
            b"AK"
            + (1).to_bytes(2, "little")
            + (2).to_bytes(2, "little")
            + (3).to_bytes(1, "little")
        )
        chunk_ack = ChunkAck(data)
        self.assertTrue(chunk_ack.is_valid)
        self.assertEqual(str(chunk_ack), "File: 1, Type: 3, Package: 2")

    def test_chunk_ack_str_invalid(self):
        data = (
            b"XX"
            + (1).to_bytes(2, "little")
            + (2).to_bytes(2, "little")
            + (3).to_bytes(1, "little")
        )
        chunk_ack = ChunkAck(data)
        self.assertFalse(chunk_ack.is_valid)
        self.assertEqual(str(chunk_ack), "Invalid Request")
        self.assertEqual(str(chunk_ack), "Invalid Request")


class TestUpdateError(unittest.TestCase):
    def test_update_error_str_valid(self):
        data = b"ER" + (5).to_bytes(1, "little") + b"Error"
        update_error = UpdateError(data)
        self.assertTrue(update_error.is_valid)
        self.assertEqual(str(update_error), "Error: Error")

    def test_update_error_str_invalid(self):
        data = b"XX" + (5).to_bytes(1, "little") + b"Error"
        update_error = UpdateError(data)
        self.assertFalse(update_error.is_valid)
        self.assertEqual(str(update_error), "Invalid Request")
