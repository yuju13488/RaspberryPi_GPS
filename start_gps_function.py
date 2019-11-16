import gps_function as gps
# 樹莓派運行中執行
try:
    # 無法將在try中to_kafka_png()所return值設為except也能使用的變數（return list or tuple for upload_png()）
    # global功能僅使用於function中
    # 將繪圖功能定義在to_kafka_png()中，每跑一次迴圈製造繪圖x, y軸的list並繪圖存檔，下一次迴圈將覆蓋此存檔，upload_png()僅上傳此存檔。
    gps.to_kafka_png()

#樹莓派停止時執行
except KeyboardInterrupt:
    gps.to_gpx()
    gps.to_html()
    gps.upload_png()
    quit()
