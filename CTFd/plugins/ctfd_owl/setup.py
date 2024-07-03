from CTFd.utils import set_config

from .db_utils import DBUtils

def setup_default_configs():
    config=[
        ['owl_setup', 'yes'],
        ['docker_api_url', 'unix:///var/run/docker.sock'],
        ['docker_flag_prefix', 'flag'],
        ['docker_max_container_count', '100'],
        ['docker_max_renew_count', '5'],
        ['docker_timeout', '3600'],
        ['frp_direct_ip_address', 'direct.hongy.online'],
        ['frp_direct_port_maximum', '10200'],
        ['frp_direct_port_minimum', '10101'],
        ['frp_http_domain_suffix', 'dynamic.hongy.online'],
        ['frpc_config_template',
         '[common]\r\ntoken = 4e7edff6-753a-4b87-a42c-a037a0c68f64\r\nserver_addr = frps\r\nserver_port = 7000\r\nadmin_addr = 0.0.0.0\r\nadmin_port = 7400']
    ]
    DBUtils.save_all_configs(config)