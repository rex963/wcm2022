# 畫紅框
# 導入 doc
from browser import document as doc
# 以下將利用 html 產生所需的繪圖畫布
from browser import html
# 利用 math 函式庫執行三角函數運算
import math
canvas = html.CANVAS(width = 600, height = 400)
#canvas.style = {"width": "100%"}
canvas.id = "taiwan_flag"
# 將圖畫至 id 為 brython_div 的 cnavas 標註
brython_div = doc["brython_div"]
brython_div <= canvas
# 準備繪圖畫布
canvas = doc["taiwan_flag"]
ctx = canvas.getContext("2d")
# 進行座標轉換, x 軸不變, y 軸反向且移動 canvas.height 單位光點
# ctx.setTransform(1, 0, 0, -1, 0, canvas.height)
# 以下採用 canvas 原始座標繪圖
flag_w = canvas.width
flag_h = canvas.height
circle_x = flag_w/4
circle_y = flag_h/4
# 先畫滿地紅
ctx.fillStyle='rgb(255, 0, 0)'
ctx.fillRect(200,100,flag_w,flag_h)
# 再畫白
ctx.fillStyle='#fff'
ctx.fillRect(250,150,flag_w/2,flag_h/2)
