# LINE_doraemon_flyio

## 目的
由於LINE Bot發送訊息的免費額度甚少(200則/月)，因此本專案示範由LINE Bot接收訊息並透過LINE Notify回應，大大提升發送訊息免費額度(1000/hr)

## 項目簡介
這個項目是一個基於 Flask 的 LINE 機器人，部屬在fly.io，它能夠接收訊息，並根據訊息內容使用 LINE Notify 發送相應的回應。如果訊息包含特定關鍵詞（如「哆啦」），則隨機發送一個預定義的圖片鏈接。

## 如何運行
### 1. Clone此repo到本地
   ```bash
   git clone https://github.com/mrsanderz/linebot_doraemon_flyio.git
   ```
### 2. LINE Bot & LINE Notify設定
> 1. 進入
https://developers.line.biz/en/services/messaging-api/
> 2. 建立一個Bot，Channel Secret就是程式中'YOUR Channel Secret'
本專案不用Line bot respond所以不需要issue "Channel access token"
   ![image](https://github.com/mrsanderz/linebot_doraemon_flyio/assets/37920668/82ed84a9-6f2d-4640-afee-024e37e0e4ee)
> 3. 輸入webhook(需先在fly.io create app(fly launch)得到hostname)
   ![image](https://github.com/mrsanderz/linebot_doraemon_flyio/assets/37920668/e7c00832-8cd5-4612-acc1-de4df3f4a13b)

### 3. LINE Notify
> 進入https://notify-bot.line.me/my/
右上角頭像->個人頁面->發行存取權杖 (測試用，只測試發行個人權杖，也就是不給其他人訂閱)
發行後可以複製權杖，也就是程式中'YOUR line_notify_token'
   <img src="https://github.com/mrsanderz/linebot_doraemon_flyio/assets/37920668/0db894b8-5229-49e4-abb6-4f95c5c99ead" width="300" height="300">
### 4. LINE 測試群組
> 把LINE Notify跟LINT Bot拉入群組
   <img src="https://github.com/mrsanderz/linebot_doraemon_flyio/assets/37920668/03853132-9124-45e7-8363-0b2754c374c5" width="300" height="300">

### 5 fly.io部屬
> fly.io部屬
可以參考這篇部屬方式: https://hackmd.io/@littlehsun/linechatbot
> LINE 群組進行對話
(確定fly.io以部屬完成且成功運行 p.s. fly.io已經不能說完全免費了，註冊帳號後提示帳號不安全，花了10美金unlock...，網上也有被誤收費的案例，慎用)
   <img src="https://github.com/mrsanderz/linebot_doraemon_flyio/assets/37920668/8767559d-cb60-48b5-afad-44a654bd44cf" width="300" height="500">

## 功能
- 接收 LINE 訊息
- 判斷訊息內容是否包含特定關鍵詞
- 通過 LINE Notify 發送圖片或重複訊息

## 技術棧
- Python
- Flask
- LINE Messaging API
- LINE Notify API
- fly.io
