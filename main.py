import ssl
import Utils.sparkUtils as Spark
import websocket
import Utils.tesserocrUtil as Ocr
import OCRresult.OCR_post_processing
import Utils.pyauto_util

def main(appid, api_key, api_secret, domain, spark_url, query):
    wsParam = Spark.Ws_Param(appid, api_key, api_secret, spark_url)
    websocket.enableTrace(False)
    wsUrl = wsParam.create_url()

    ws = websocket.WebSocketApp(wsUrl, on_message=Spark.on_message, on_error=Spark.on_error, on_close=Spark.on_close, on_open=Spark.on_open)
    ws.appid = appid
    ws.query = query
    ws.domain = domain

    while True:
        flag1 = 0
        flag1 = int(input())
        if flag1 == 1:
            Utils.pyauto_util.get_screenshot()
            lines = OCRresult.OCR_post_processing.get_post_line()
            lines = lines.replace("\n\n", "\n")
            lines = lines.splitlines()
            for line in lines:
                query = line
                ws.query = query
                ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})

    # while True:
    #     query = input()
    #     while (query=="" or query==' '):
    #         query = input()
    #     ws.query = query
    #     ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
    # ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})


if __name__ == "__main__":
    main(
        appid="appid",
        api_key="api_key",
        api_secret="api_secret",
        domain="generalv3.5",
        spark_url="wss://spark-api.xf-yun.com/v3.5/chat",
        query='das bier ist gut'
    )
