# URL
![test](https://github.com/daikiiiiy/ros2_ws/actions/workflows/test.yml/badge.svg)

# 概要
このソフトはros2を用いり基本的なパブリッシャ・サブスクライバ通信を学習するためのサンプルコードである。 mypkg パッケージ内に含ま
れる talker ノードと listener ノードを実行することで、ROS2 におけるトピック通信の基本的な仕組みを確認できる。

# ダウンロード
- 1.最初に"Clone or download"を選択します. 
- 2.選択したら"Download ZIP"を押します. 
- 3.URLをコピーしてもらうとダウンロードが完了します
- 4.インストールはgit clone https://github.com/daikiiiiy/ros2_ws.git を打ち込むと完了します

# ノード
## talkerノード
　ランダムに数値を生成し、listenerに数値を出力させる
## listenerノード
　talkerから出力された数値を読み取り特定の数値より大きくったら
　警告文を表示する。（今回は数値が80になると警告します）以上特定の数値以下になったらNomal Valueと表示する

# 実行例・実行結果
## 実行例
### 1.talkerの実行の仕方
　ターミナルで以下のコードを打ち実行させる
```
 ros2 run mypkg talker
```
### 2.listenerの実行の仕方
　別のターミナルを立ち上げ以下のコードを打ち実行させる
```
 ros2 run mypkg listener
```
## 実行結果
### talkerの場合
```
[INFO] [1767148462.640015353] [sensor_talker]: Sensor value: 28
[INFO] [1767148463.640128919] [sensor_talker]: Sensor value: 49
[INFO] [1767148464.640304584] [sensor_talker]: Sensor value: 64
[INFO] [1767148465.640761696] [sensor_talker]: Sensor value: 0
[INFO] [1767148466.639853841] [sensor_talker]: Sensor value: 93
[INFO] [1767148468.669810007] [sensor_talker]: Sensor value: 23
[INFO] [1767148469.639453981] [sensor_talker]: Sensor value: 32
```

### listenerの場合
```
[INFO] [1767148463.641010674] [monitor_listener]: Normal value: 49
[INFO] [1767148464.641034652] [monitor_listener]: Normal value: 64
[INFO] [1767148465.641670720] [monitor_listener]: Normal value: 0
[WARN] [1767148466.640519384] [monitor_listener]: WARNING: Abnormal value detected! (93)
[INFO] [1767148468.671377122] [monitor_listener]: Normal value: 23
[INFO] [1767148469.640511831] [monitor_listener]: Normal value: 32
```
# どんな環境で使えるか
- Python3
- ros2 Jazzy
- python 3.12
# テスト環境
- Ubuntu 24.04 LTS
# 権利関係・謝辞
- このソフトハードウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます.
- このパッケージのコードは、上田隆一教授由来のコード（© 2025 Ryuichi Ueda)を利用しています.
- このパッケージのコードは、下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを、本人の許可を得て自身の著者としたものです
    -[ryuichueda/slides_marp robosys2025](https://github.com/ryuichiueda/slides_marp/tree/master/robosys2025)
- © 2025 Daiki Okamoto

参考したアプリ
Chat GPT（コードの提案やREADMEの添削に使用した）
