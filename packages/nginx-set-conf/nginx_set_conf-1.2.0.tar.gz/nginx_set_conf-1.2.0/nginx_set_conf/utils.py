"""
Utility functions for Nginx configuration management.

This module provides helper functions for managing Nginx configurations,
including YAML parsing, configuration deployment, and input validation.
All functions are designed to work with the nginx_set_conf package.

Typical usage example:
    yaml_config = parse_yaml('config.yaml')
    execute_commands(yaml_config['template'], yaml_config['domain'], ...)
"""

# -*- coding: utf-8 -*-
# Copyright 2014-now Equitania Software GmbH - Pforzheim - Germany
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import os
import yaml
from .config_templates import get_config_template


def fire_all_functions(function_list: list) -> None:
    """Executes a list of functions in sequence.

    Args:
        function_list: A list of callable functions to be executed.
    """
    for func in function_list:
        func()


def self_clean(input_dictionary: dict) -> dict:
    """Removes duplicate values from dictionary values while preserving keys.

    Args:
        input_dictionary: Dictionary to clean.

    Returns:
        A new dictionary with duplicate values removed from each key's value list.
    """
    return_dict = input_dictionary.copy()
    for key, value in input_dictionary.items():
        return_dict[key] = list(dict.fromkeys(value))
    return return_dict


def parse_yaml(yaml_file: str) -> dict:
    """Parses a YAML file into a Python dictionary.

    Args:
        yaml_file: Path to the YAML file to parse.

    Returns:
        Dictionary containing the parsed YAML data.
        Returns False if parsing fails.

    Raises:
        yaml.YAMLError: If the YAML file is malformed.
    """
    with open(yaml_file, "r") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
            return False


def parse_yaml_folder(path: str) -> list:
    """Parses all YAML files in a directory.

    Searches for files with .yaml or .yml extensions in the specified directory
    and parses each one into a Python object.

    Args:
        path: Directory path containing YAML files.

    Returns:
        List of parsed YAML objects.
    """
    yaml_objects = []
    for file in os.listdir(path):
        if file.endswith(".yaml") or file.endswith(".yml"):
            yaml_object = parse_yaml(os.path.join(path, file))
            if yaml_object:
                yaml_objects.append(yaml_object)
    return yaml_objects


def get_default_vars() -> dict:
    """Returns default variables for Nginx configuration.

    Returns:
        Dictionary containing default values for Nginx configuration variables
        including server paths, domains, ports, and certificate locations.
    """
    return {
        "server_path": "/etc/nginx/conf.d",
        "old_domain": "server.domain.de",
        "old_ip": "ip.ip.ip.ip",
        "old_port": "oldport",
        "old_pollport": "oldpollport",
        "old_crt": "zertifikat.crt",
        "old_key": "zertifikat.key",
        "old_self_crt": "/etc/letsencrypt/live/zertifikat.crt/fullchain.pem",
        "old_self_key": "/etc/letsencrypt/live/zertifikat.key/privkey.pem",
        "old_redirect_domain": "target.domain.de",
        "old_auth_file": "authfile",
    }


def retrieve_valid_input(message: str) -> str:
    """Prompts user for input until non-empty input is provided.

    Args:
        message: Prompt message to display to user.

    Returns:
        User's non-empty input string.
    """
    user_input = input(message)
    if user_input:
        return user_input
    else:
        return retrieve_valid_input(message)


def execute_commands(
    config_template, domain, ip, cert_name, cert_key, port, pollport, redirect_domain, auth_file
):
    """Generates and deploys Nginx config files based on input parameters.

    Args:
        config_template: Template name for Nginx configuration.
        domain: Domain name for Nginx configuration.
        ip: IP address for Nginx configuration.
        cert_name: Certificate name for Nginx configuration.
        cert_key: Certificate key for Nginx configuration.
        port: Port number for Nginx configuration.
        pollport: Polling port number for Nginx configuration (optional).
        redirect_domain: Redirect domain for Nginx configuration (optional).
        auth_file: Authentication file for Nginx configuration (optional).
    """
    # Get default vars
    default_vars = get_default_vars()
    server_path = default_vars["server_path"]
    old_domain = default_vars["old_domain"]
    old_ip = default_vars["old_ip"]
    old_crt = default_vars["old_crt"]
    old_key = default_vars["old_key"]
    old_self_crt = default_vars["old_self_crt"]
    old_self_key = default_vars["old_self_key"]
    old_port = default_vars["old_port"]
    old_pollport = default_vars["old_pollport"]
    old_redirect_domain = default_vars["old_redirect_domain"]
    # Get config templates
    config_template_content = get_config_template(config_template)
    if config_template_content:
        current_path = os.path.dirname(os.path.realpath(__file__))
        file_path = current_path + "/" + config_template + ".conf"
        with open(file_path, "w") as f:
            f.write(config_template_content)
        # copy command
        eq_display_message = (
            "Copy " + file_path + " " + server_path + "/" + domain + ".conf"
        )
        eq_copy_command = "cp " + file_path + " " + server_path + "/" + domain + ".conf"
        print(eq_display_message.rstrip("\n"))
        os.system(eq_copy_command)
        print(eq_copy_command.rstrip("\n"))
        os.remove(file_path)
    else:
        print("No valid config template")

    # send command - domain
    eq_display_message = "Set domain name in conf to " + domain
    eq_set_domain_cmd = (
        "sed -i 's|"
        + old_domain
        + "|"
        + domain
        + "|g' "
        + server_path
        + "/"
        + domain
        + ".conf"
    )
    print(eq_display_message.rstrip("\n"))
    os.system(eq_set_domain_cmd)
    print(eq_set_domain_cmd.rstrip("\n"))

    # send command - ip
    eq_display_message = "Set ip in conf to " + ip
    eq_set_ip_cmd = (
        "sed -i 's|" + old_ip + "|" + ip + "|g' " + server_path + "/" + domain + ".conf"
    )
    print(eq_display_message.rstrip("\n"))
    os.system(eq_set_ip_cmd)
    print(eq_set_ip_cmd.rstrip("\n"))

    if cert_key != "":
        old_crt = old_self_crt
        old_key = old_self_key
    else:
        cert_key = cert_name

    # send command - cert, key
    eq_display_message = "Set cert name in conf to " + cert_name
    eq_set_cert_cmd = (
        "sed -i 's|"
        + old_crt
        + "|"
        + cert_name
        + "|g' "
        + server_path
        + "/"
        + domain
        + ".conf"
    )
    eq_set_key_cmd = (
        "sed -i 's|"
        + old_key
        + "|"
        + cert_key
        + "|g' "
        + server_path
        + "/"
        + domain
        + ".conf"
    )
    print(eq_display_message.rstrip("\n"))
    os.system(eq_set_cert_cmd)
    print(eq_set_cert_cmd.rstrip("\n"))
    os.system(eq_set_key_cmd)
    print(eq_set_key_cmd.rstrip("\n"))

    # Letsencrypt
    if cert_key == cert_name:
        # Search for certificate and create it when it does not exist
        cert_exists = os.path.isfile(
            "/etc/letsencrypt/live/" + cert_name + "/fullchain.pem"
        ) and os.path.isfile("/etc/letsencrypt/live/" + cert_name + "/privkey.pem")
        if not cert_exists:
            os.system("systemctl stop nginx.service")
            eq_create_cert = (
                "certbot certonly --standalone --agree-tos --register-unsafely-without-email -d "
                + cert_name
            )
            os.system(eq_create_cert)
            print(eq_create_cert.rstrip("\n"))

    # send command - port
    eq_display_message = "Set port in conf to " + port
    eq_set_port_cmd = (
        "sed -i 's|"
        + old_port
        + "|"
        + port
        + "|g' "
        + server_path
        + "/"
        + domain
        + ".conf"
    )
    print(eq_display_message.rstrip("\n"))
    os.system(eq_set_port_cmd)
    print(eq_set_port_cmd.rstrip("\n"))

    # Odoo polling port
    if "odoo" in config_template and pollport:
        # send command - polling port
        eq_display_message = "Set polling port in conf to " + pollport
        eq_set_port_cmd = (
            "sed -i 's|"
            + old_pollport
            + "|"
            + pollport
            + "|g' "
            + server_path
            + "/"
            + domain
            + ".conf"
        )
        print(eq_display_message.rstrip("\n"))
        os.system(eq_set_port_cmd)
        print(eq_set_port_cmd.rstrip("\n"))

    # authentication
    eq_display_message = "Try set auth file to " + auth_file
    print(eq_display_message.rstrip("\n"))
    if auth_file:
        eq_display_message = "Set auth file to " + auth_file
        print(eq_display_message.rstrip("\n"))
        _filename = server_path + "/" + domain + ".conf"
    
        with open(_filename, "r", encoding="utf-8") as _file:
            _data = _file.readlines()
    
        # Find the index of the line containing #authentication and add 1 to insert after this line
        insertion_index = None
        for i, line in enumerate(_data):
            if '#authentication' in line:  # Check if this is the line we're looking for
                insertion_index = i + 1
                break
    
        # If the marker was found, insert the authentication lines after it
        if insertion_index is not None:
            _data.insert(insertion_index, '        auth_basic       "Restricted Area";' + "\n")
            _data.insert(insertion_index + 1, "        auth_basic_user_file  " + auth_file + ";" + "\n")
    
        with open(_filename, "w", encoding="utf-8") as _file:
            _file.writelines(_data)


    if "redirect" in config_template and redirect_domain:
        # send command - redirect domain
        eq_display_message = "Set redirect domain in conf to " + redirect_domain
        eq_set_redirect_cmd = (
            "sed -i 's|"
            + old_redirect_domain
            + "|"
            + redirect_domain
            + "|g' "
            + server_path
            + "/"
            + domain
            + ".conf"
        )
        print(eq_display_message.rstrip("\n"))
        os.system(eq_set_redirect_cmd)
        print(eq_set_redirect_cmd.rstrip("\n"))

    # Search for certificate and create it when it does not exist
    if "redirect_ssl" in config_template and redirect_domain:
        cert_exists = os.path.isfile(
            "/etc/letsencrypt/live/" + redirect_domain + "/fullchain.pem"
        ) and os.path.isfile(
            "/etc/letsencrypt/live/" + redirect_domain + "/privkey.pem"
        )
        if not cert_exists:
            os.system("systemctl stop nginx.service")
            eq_create_cert = (
                "certbot certonly --standalone --agree-tos --register-unsafely-without-email -d "
                + redirect_domain
            )
            os.system(eq_create_cert)
            print(eq_create_cert.rstrip("\n"))
