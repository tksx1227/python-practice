import yaml


# 書き込み
with open("config.yaml", "w") as yaml_file:
    # default_flow_style を False にするとブロックスタイルで書き込まれる
    yaml.dump({
        "web_server": {
            "host": "127.0.0.1",
            "port": 80,
        },
        "db_server": {
            "host": "127.0.0.1",
            "port": 3306
        }
    }, yaml_file, default_flow_style=False)

# 読み込み
# Loader の種類はこちらで確認 => https://github.com/yaml/pyyaml/wiki/PyYAML-yaml.load(input)-Deprecation
with open("config.yaml", "r") as yaml_file:
    data = yaml.load(yaml_file, Loader=yaml.SafeLoader)
    print(data, type(data))
    print(data["web_server"]["host"])
    print(data["web_server"]["port"])
    print(data["db_server"]["host"])
    print(data["db_server"]["port"])
