# -*- coding: utf-8 -*-
"""
設定ファイル
現場に合わせてここだけ書き換えれば動くようにしてあります。
"""

# ====== カメラ設定 ======
CAMERA_INDEX = 0          # USBカメラ番号。産業用カメラの場合はSDK側の設定に差し替え
FRAME_WIDTH = 640
FRAME_HEIGHT = 480

# ====== 学習データ ======
NORMAL_IMAGE_DIR = "./normal_images"   # 正常品の画像だけを入れるフォルダ
MEMORY_BANK_PATH = "./memory_bank.pkl" # 学習結果(正常品の特徴量)の保存先

# ====== 異常検知の閾値 ======
# スコアが高いほど「正常品から遠い=傷/欠陥の可能性が高い」
ANOMALY_THRESHOLD = 12.0   # まずは仮値。運用しながらチューニングする
CONSECUTIVE_NG_COUNT = 3   # 何フレーム連続でNGだったら本当にNGと判断するか(誤停止防止)

# ====== ログ・画像保存 ======
LOG_DIR = "./logs"
SAVE_NG_IMAGES = True
NG_IMAGE_DIR = "./ng_images"

# ====== PLC通信設定 (Modbus TCP) ======
PLC_ENABLED = True
PLC_IP = "192.168.1.10"    # PLCのIPアドレスに変更してください
PLC_PORT = 502              # Modbus TCPの標準ポート
PLC_COIL_ADDRESS = 0         # 停止信号を出力するコイル番号(PLC側の割付に合わせる)

# ====== 監視ループ設定 ======
CHECK_INTERVAL_SEC = 0.5   # 何秒おきに1枚判定するか
