from kafka import KafkaConsumer
from kafka import TopicPartition
from kafka.structs import OffsetAndMetadata

topic = 'topic_wechat_push_template'
partition = 0
tp = TopicPartition(topic,partition)
kafkaConsumer = KafkaConsumer(config)
kafkaConsumer.assign([tp])
offset = 15394125
kafkaConsumer.commit({
    tp: OffsetAndMetadata(offset, None)
})

meta = consumer.partitions_for_topic(topic)
options = {}
options[partition] = OffsetAndMetadata(message.offset, meta)
consumer.commit(options)




curl -v -d "" "http://localhost:8080/schedule/hour/2018-09-10%2010:00:00/task"