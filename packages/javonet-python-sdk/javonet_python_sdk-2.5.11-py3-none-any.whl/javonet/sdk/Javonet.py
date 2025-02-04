"""
The Javonet module is a singleton module that serves as the entry point for interacting with Javonet.
It provides functions to activate and initialize the Javonet SDK.
It supports both in-memory and TCP connections.
Refer to this `article on Javonet Guides <https://www.javonet.com/guides/v2/python/foundations/javonet-static-class>`_ for more information.
"""

from javonet.core.transmitter.Transmitter import Transmitter
from javonet.sdk.tools.ActivationHelper import ActivationHelper
from javonet.sdk.tools.SdkMessageHelper import SdkMessageHelper
from javonet.sdk.RuntimeFactory import RuntimeFactory
from javonet.sdk.ConfigRuntimeFactory import ConfigRuntimeFactory
from javonet.utils.RuntimeLogger import RuntimeLogger
from javonet.utils.connectionData.InMemoryConnectionData import InMemoryConnectionData
from javonet.utils.connectionData.TcpConnectionData import TcpConnectionData
from javonet.utils.connectionData.WsConnectionData import WsConnectionData
import os

SdkMessageHelper.send_message_to_app_insights("SdkMessage", "Javonet SDK initialized")

def in_memory():
    """
    Initializes Javonet using an in-memory channel on the same machine.

    Returns:
        RuntimeFactory: An instance configured for an in-memory connection.
    Refer to this `article on Javonet Guides <https://www.javonet.com/guides/v2/python/foundations/in-memory-channel>`_ for more information.
    """
    return RuntimeFactory(InMemoryConnectionData())


def tcp(tcp_connection_data: TcpConnectionData):
    """
    Initializes Javonet with a TCP connection to a remote machine.

    Args:
        tcp_connection_data (str): The address of the remote machine.

    Returns:
        RuntimeFactory: An instance configured for a TCP connection.
    Refer to this `article on Javonet Guides <https://www.javonet.com/guides/v2/python/foundations/tcp-channel>`_ for more information.
    """
    return RuntimeFactory(tcp_connection_data)


def ws(ws_connection_data: WsConnectionData):
    """
    Initializes Javonet with a WebSocket connection to a remote machine.

    Args:
        ws_connection_data (str): The address of the remote machine.

    Returns:
        RuntimeFactory: An instance configured for a WebSocket connection.
    Refer to this `article on Javonet Guides <https://www.javonet.com/guides/v2/python/foundations/websocket-channel>`_ for more information.
    """
    return RuntimeFactory(ws_connection_data)


def with_config(path):
    """
    Initializes Javonet with a configuration taken from external source.
    Currently supported: Configuration file in JSON format

    Args:
        path (str): Path to a configuration file.

    Returns:
        ConfigRuntimeFactory: An instance configured with configuration data.
    Refer to this `article on Javonet Guides <https://www.javonet.com/guides/v2/python/foundations/configure-channel>`_ for more information.
    """
    try:
        return ConfigRuntimeFactory(path)
    except Exception as e:
        SdkMessageHelper.send_message_to_app_insights("SdkException",  str(e))
        raise e


def activate(license_key):
    """
    Activates Javonet with the provided license key.

    Args:
        license_key (str): The license key to activate Javonet.

    Returns:
        int: The activation status code.
    Refer to this `article on Javonet Guides <https://www.javonet.com/guides/v2/python/getting-started/activating-javonet>`_ for more information.
    """
    try:
        if license_key != ActivationHelper.get_temporary_license_key():
            ActivationHelper.set_temporary_license_key(license_key)
            SdkMessageHelper.send_message_to_app_insights("SdkMessage", "Activation")

        ActivationHelper.set_temporary_license_key(license_key)
        return Transmitter.activate(license_key)
    except Exception as e:
        SdkMessageHelper.send_message_to_app_insights("SdkException", str(e))
        raise e



def set_config_source(config_source):
    """
    Sets the configuration source for the Javonet SDK.

    Args:
        config_source (str): The configuration source.
    """
    try:
        Transmitter.set_config_source(config_source)
    except Exception as e:
        SdkMessageHelper.send_message_to_app_insights("SdkException", str(e))
        raise e

def set_javonet_working_directory(path):
    """
    Sets the working directory for the Javonet SDK.

    Args:
        path (str): The working directory.
    """
    try:
        path = path.replace('\\', '/')
        if not path.endswith('/'):
            path += "/"

        if not os.path.exists(path):
            os.makedirs(path)
            os.chmod(path, 0o700)

        ActivationHelper.set_working_directory(path)
        Transmitter.set_javonet_working_directory(path)
    except Exception as e:
        SdkMessageHelper.send_message_to_app_insights("SdkException", str(e))
        raise e

def get_runtime_info():
    """
    Gets information about the current runtime.

    Returns:
        str: Information about the current runtime.
    """
    return RuntimeLogger.get_runtime_info()