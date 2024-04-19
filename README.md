1. Run docker-compose:
```shell
docker-compose up -d
```
2. Connect to [Zabbix Web UI](http://localhost:8080)
- Login: 
  - username: Admin
  - password: zabbix
3. Connect to [Grafana](http://localhost:3000)
- Login:
  - username: admin
  - password: 12345

4. Enable Zabbix 
- Plugins and data 
  - Plugins
    - Add Zabbix
5. Add data source
- Connections 
  - Data sources
    - Add data source
      - Zabbix

# Debug
```shell
docker-compose logs --tail=1 -f
```

Sources
[Zabbix-docker](https://github.com/akmalovaa/zabbix-docker/blob/main/README.md)
[Zabbix,Nginx,Postgresql,Docker-Compose](https://gist.github.com/mtrimarchi/d75f921308cf7e0882f87cc501faaa93)
https://www.alibabacloud.com/help/en/grafana/user-guide/add-and-use-a-zabbix-data-source