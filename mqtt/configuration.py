import dataclasses

@dataclasses.dataclass
class Configuration:
    broker_ip_address: str
    broker_publish_topic: str
    broker_port: int = 1883
    broker_subscribe_topics: list = dataclasses.field(default_factory=list)

