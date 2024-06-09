# linebot_doraemon_flyio
# LINE Notify 機器人

## 項目簡介
這個項目是一個基於 Flask 的 LINE 機器人，它能夠接收訊息，並根據訊息內容使用 LINE Notify 發送相應的回應。如果訊息包含特定關鍵詞（如「哆啦」），則隨機發送一個預定義的圖片鏈接；否則，它將重複發送接收到的訊息。

## 功能
- 接收 LINE 訊息
- 判斷訊息內容是否包含特定關鍵詞
- 通過 LINE Notify 發送圖片或重複訊息

## 技術棧
- Python
- Flask
- LINE Messaging API
- LINE Notify API

## 如何運行
1. 克隆此倉庫到本地
   ```bash
   git clone https://your-github-repo-url-here.git
