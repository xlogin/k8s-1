# 使用前要先启动zookeeper和kafka服务
# 启动zookeeper要cd /home/lp/soft/kafka_2.11-1.1.0,然后 bin/zookeeper-server-start.sh config/zookeeper.properties
# 启动kafka要cd /home/lp/soft/kafka_2.11-1.1.0,然后bin/kafka-server-start.sh config/server.properties


from kafka import KafkaProducer
import time,json
producer = KafkaProducer(bootstrap_servers=['192.168.2.177:30946'])  #此处ip可以是多个['0.0.0.1:9092','0.0.0.2:9092','0.0.0.3:9092' ]


i=0
while True:
    i+=1
    msg = {'userid':i,'name':'lp'+str(i),'age':i}
    print(msg)
    producer.send('device', json.dumps(msg).encode('utf-8'))  # 参数为主题和bytes数据
    time.sleep(1)

producer.close()