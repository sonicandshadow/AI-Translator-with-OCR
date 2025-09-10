import ssl
import os
import Utils.sparkUtils as Spark
import websocket
import OCRresult.OCR_post_processing
import Utils.pyauto_util
import tkinter as tk
from threading import Timer
import keyboard
import config.spark_config as spark_config
# 在config/spark_config中配置星火api
root = tk.Tk()
selectArea=(0, 0, 0, 0)
capture_flag=True


def button_clicked_select_zone():
    # 点击选择区域按钮事件，选择区域进行屏幕截图
    # 选择截图区域比如游戏字幕，之后通过热键shift+ctrl对选定区域进行截图并翻译
    root.iconify()
    # Utils.pyauto_util.get_screenshot()
    global selectArea
    selectArea= Utils.pyauto_util.get_screen_zone()


def screen_capture():
    # 截屏
    Utils.pyauto_util.get_screenshot(selectArea)


def bstart_capture():
    # 用于开始截屏按钮
    start_capture()
    return 0

def start_capture():
    # 开始截屏，每秒截屏一次，在完成自动处理图像文字变化之前无用，当前版本使用shift+ctrl热键手动触发翻译
    global capture_flag
    if capture_flag == False:
        return 0
    screen_capture()
    capture_thread = Timer(1, start_capture)
    capture_thread.start()


def keyboard_capture(ws):
    # 通过shift+ctrl热键手动触发截图翻译，下一步自定义热键
    screen_capture()
    # 执行OCR获得原始文本
    lines = OCRresult.OCR_post_processing.get_post_line()
    # 去掉多余的换行节省token
    lines = lines.replace("\n\n", "\n")
    f = open("result.txt", "a", encoding='utf-8')
    f.write("原始文本:"+lines+"\n翻译后:")
    f.close()
    # 将每行文本依次交予AI进行翻译
    lines = lines.splitlines()
    for line in lines:
        query = line
        ws.query = query
        ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})

def main():
    # 从spark_config获取配置
    appid = spark_config.appid
    api_key = spark_config.api_key
    api_secret = spark_config.api_secret
    spark_url = spark_config.spark_url
    query = spark_config.query
    domain = spark_config.domain
    if(os.path.exists("result.txt")==False):
        f = open('result.txt', 'w', encoding='utf-8')
        f.close()
    wsParam = Spark.Ws_Param(appid, api_key, api_secret, spark_url)
    websocket.enableTrace(False)
    wsUrl = wsParam.create_url()
    ws = websocket.WebSocketApp(wsUrl, on_message=Spark.on_message, on_error=Spark.on_error, on_close=Spark.on_close, on_open=Spark.on_open)
    ws.appid = appid
    ws.query = query
    ws.domain = domain
    # tk窗口，在当前版本只有选择区域有实际作用
    root.title("翻译控制台")
    label = tk.Label(root, text="功能")
    label.pack(pady=5)
    button_Select_Zone = tk.Button(root, text="选择区域",command=button_clicked_select_zone)
    button_Select_Zone.pack(pady=5)
    button_start_capture = tk.Button(root, text="开始截屏",command=bstart_capture)
    button_start_capture.pack(pady=6)
    # root.bind("<Control-Shift_L>", keyboard_capture)
    # keyboard_listener = keyboard.Listener(on_press=)
    keyboard.add_hotkey('shift+caps lock',keyboard_capture,args=(ws,))
    root.mainloop()
    # while True:
    #     flag1 = 0
    #     flag1 = int(input())
    #     if flag1 == 1:
    #         lines = OCRresult.OCR_post_processing.get_post_line()
    #         lines = lines.replace("\n\n", "\n")
    #         lines = lines.splitlines()
    #         for line in lines:
    #             query = line
    #             ws.query = query
    #             ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})

    # while True:
    #     query = input()
    #     while (query=="" or query==' '):
    #         query = input()
    #     ws.query = query
    #     ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
    # ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})


if __name__ == "__main__":
    main(
        # appid="",
        # api_key="",
        # api_secret="",
        # domain="generalv3.5",
        # spark_url="wss://spark-api.xf-yun.com/v3.5/chat",
        # 测试文本
        # query='das bier ist gut'
    )
