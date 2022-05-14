import serial  # 引用 pySerial 模組

import LineNotify

if __name__ == '__main__':
    COM_PORT = 'COM5'  # 指定通訊埠
    BAUD_RATE = 9600  # 設定傳輸速率(鮑率)
    ser = None
    try:
        ser = serial.Serial(COM_PORT, BAUD_RATE)  # 初始化
        # 循環接收資料
        while True:
            while ser.in_waiting:  # 若有收到資料
                data_row = ser.readline()  # 讀一行原始資料
                data = data_row.decode()  # 將原始資料轉碼, 預設編碼是 UTF-8
                data = data.strip("\r").strip("\n")  # 去除換行符號
                print(data)
                # 過濾出驗證成功數值並顯示
                # 例如:
                # 收到 : Found ID #3 with confidence of 120
                # 顯示 : 120
                if 'Found ID' in data:
                    uid = data.split(' ')[-1]
                    # print(uid , type(uid))
                    uid = int(uid)  # 字串轉型成int
                    print(uid, type(uid))
                    if uid > 100:
                        print('開門')
                        # 傳送 1# 給 arduino 進行開燈(門), # 表示約定結尾符號
                        send_data = '1'
                        # LineNotify.sendMessage("開門")
                        LineNotify.sendMessageAndImageFile('開門', 'door_open.jpg')
                        # time.sleep(0.5)  # 休息時間 0.5 秒
                    if uid < 100:
                        print('驗證失敗')
                        send_data = '0'

                    send_data = send_data.encode()
                    ser.write(send_data)
                    print('傳送', send_data, '給 Arduino')

    except serial.SerialException:
        print('通訊埠', COM_PORT, '無法建立')
        print('請確認 Arduino IDE 的序列埠通訊視窗是否有關閉')
    except KeyboardInterrupt:
        if ser is not None:
            ser.close()  # 關閉通訊埠

