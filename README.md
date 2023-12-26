# rp2040_circuitpython_hid_keyboard_gamepad
rp2040_circuitpython_hid_keyboard_gamepad

使用方法：
1. 去circuit python官網下載pico專屬核心uf2檔
2. 或者使用thonny也可以安裝circuit python核心uf2
3. 透過thonny確認安裝成功（可看到終端視窗出現circuit python提示訊息）
4. 到circuit python官網下載circuitpython-bundle
5. 解開後將adafruit_hid資料夾上傳到板子上的lib資料夾中
6. 將這裡的py檔透過thonny上傳到板子的根目錄
7. 修改檔名為main.py可以讓circuitPython自動執行
8. 使用鍵盤檢查程式確認動作正常
9. 開始遊玩

## pinmap
```
core: circuitPython-8.2.9
dependency: adafruit-circuitpython-bundle-8.x-mpy-20231224
                    __
              GP0--|  |--VBUS
              GP1        VSYS
              GND        GND
    Z |---/ --GP2        3V3EN
    X |---/ --GP3        3V3OUT
ENTER |---/ --GP4        VREF
 DOWN |---/ --GP5        GP28 --/ ---| SPACE
              GND  ____  GND
RIGHT |---/ --GP6 | RP | GP27
              GP7 |2040| GP26
 LEFT |---/ --GP8  ----  RUN
   UP |---/ --GP9        GP22
```
