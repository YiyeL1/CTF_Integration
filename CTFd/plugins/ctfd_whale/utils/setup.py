from CTFd.utils import set_config

from ..models import WhaleRedirectTemplate, db


def setup_default_configs():
    for key, val in {
        'setup': 'true',
        'docker_api_url': 'unix:///var/run/docker.sock',
        'docker_credentials': '',
        'docker_dns': '127.0.0.1',
        'docker_max_container_count': '100',
        'docker_max_renew_count': '5',
        'docker_subnet': '174.1.0.0/16',
        'docker_subnet_new_prefix': '24',
        'docker_swarm_nodes': 'linux-1',
        'docker_timeout': '3600',
        'docker_auto_connect_network': 'ctfd_containers',
        'docker_auto_connect_containers': 'ctfd-frpc-1',
        'frp_api_url': 'http://frpc:7400',
        'frp_http_port': '80',
        'frp_http_domain_suffix': 'dynamic.hongy.online',
        'frp_direct_ip_address': 'direct.hongy.online',
        'frp_direct_port_maximum': '10100',
        'frp_direct_port_minimum': '10001',
        'template_http_subdomain': '{{ container.uuid }}',
        'template_chall_flag': '{{ "flag{"+uuid.uuid4()|string+"}" }}',
        'frp_config_template': '[common]\r\ntoken = 4e7edff6-753a-4b87-a42c-a037a0c68f64\r\nserver_addr = frps\r\nserver_port = 7000\r\nadmin_addr = 0.0.0.0\r\nadmin_port = 7400'
    }.items():
        set_config('whale:' + key, val)
    db.session.add(WhaleRedirectTemplate(
        'http',
        'http://{{ container.http_subdomain }}.'
        '{{ get_config("whale:frp_http_domain_suffix", "") }}'
        '{% if get_config("whale:frp_http_port", "80") != 80 %}:{{ get_config("whale:frp_http_port") }}{% endif %}/',
        '''
[http_{{ container.user_id|string }}-{{ container.uuid }}]
type = http
local_ip = {{ container.user_id|string }}-{{ container.uuid }}
local_port = {{ container.challenge.redirect_port }}
subdomain = {{ container.http_subdomain }}
use_compression = true
'''
    ))
    db.session.add(WhaleRedirectTemplate(
        'direct',
        'nc {{ get_config("whale:frp_direct_ip_address", "127.0.0.1") }} {{ container.port }}',
        '''
[direct_{{ container.user_id|string }}-{{ container.uuid }}]
type = tcp
local_ip = {{ container.user_id|string }}-{{ container.uuid }}
local_port = {{ container.challenge.redirect_port }}
remote_port = {{ container.port }}
use_compression = true

[direct_{{ container.user_id|string }}-{{ container.uuid }}_udp]
type = udp
local_ip = {{ container.user_id|string }}-{{ container.uuid }}
local_port = {{ container.challenge.redirect_port }}
remote_port = {{ container.port }}
use_compression = true
'''
    ))
    db.session.commit()
