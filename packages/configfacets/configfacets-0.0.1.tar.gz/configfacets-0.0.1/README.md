# python

Configfacets python client library

## Usage

```
from configfacets.configuration import Configuration

config = Configuration(
    apiUrl="https://configfacets.com/apis/repos/configfacets/core-concepts/applications-0.0.1/resources/collections/api-configurations/exec?format=json",
    apiKey="<your_api_key>",
    postBody={"facets": ["env:nonprod", "cluster:internal"]},
)
config.fetch()
resp = config.get_resp()

rabbitMQHost = config.get_value("rabbitmq.host")
rabbitMQPort = config.get_value("rabbitmq.port")

print("RabbitMQ Host:{}, Port:{}".format(rabbitMQHost, rabbitMQPort))


```
