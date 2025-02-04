import os
import xml.etree.ElementTree as ET

class ActivationHelper:
    _temporary_license_key = "License key not set"
    _working_directory = ""

    @staticmethod
    def set_temporary_license_key(value):
        ActivationHelper._temporary_license_key = value

    @staticmethod
    def get_temporary_license_key():
        return ActivationHelper._temporary_license_key

    @staticmethod
    def set_working_directory(value):
        ActivationHelper._working_directory = value

    @staticmethod
    def get_working_directory():
        return ActivationHelper._working_directory

    @staticmethod
    def get_license_key():
        try:
            return ActivationHelper._get_license_key_from_file()
        except Exception:
            return ActivationHelper._temporary_license_key

    @staticmethod
    def _get_license_key_from_file():
        try:
            file_path = ActivationHelper.get_working_directory() + "javonet.lic"
            if not os.path.exists(file_path):
                raise FileNotFoundError("License file not found.")

            tree = ET.parse(file_path)
            root = tree.getroot()

            ns = {'ns': 'https://ssl2.hostedwindows.pl/sdncenter-com/'}
            activate_result_element = root.find('.//ns:ActivateResult', ns)
            if activate_result_element is None:
                raise ValueError("ActivateResult element not found in the SOAP response.")

            inner_tree = ET.ElementTree(ET.fromstring(activate_result_element.text))
            license_key_element = inner_tree.find('.//ns:licenceKey', ns)
            if license_key_element is None:
                raise ValueError("License key not found in the ActivateResult.")

            return license_key_element.text
        except Exception as e:
            raise e