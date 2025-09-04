import ssl
import Utils.sparkUtils as spark
import websocket


def main(appid, api_key, api_secret, domain, spark_url, query):
    wsParam = spark.Ws_Param(appid, api_key, api_secret, spark_url)
    websocket.enableTrace(False)
    wsUrl = wsParam.create_url()

    ws = websocket.WebSocketApp(wsUrl, on_message=spark.on_message, on_error=spark.on_error, on_close=spark.on_close, on_open=spark.on_open)
    ws.appid = appid
    ws.query = query
    ws.domain = domain
    while True:
        query = input()
        while (query=="" or query==' '):
            query = input()
        ws.query = query
        ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
    # ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})


if __name__ == "__main__":
    main(
        appid="3478bc6e",
        api_key="1837c9739aa156e657ec50d72eda6c33",
        api_secret="YmE4MjgxOWEyZTc1Y2RhNTAxYzZkYzY1",
        domain="generalv3.5",
        spark_url="wss://spark-api.xf-yun.com/v3.5/chat",
        query='das bier ist gut'
    )
