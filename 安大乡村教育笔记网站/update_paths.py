import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 活动剪影图片（按顺序对应）
carousel_old = [
    '微信图片_20260421232839_1441_78.jpg',
    '微信图片_20260421232840_1442_78.jpg',
    '微信图片_20260421232841_1443_78.jpg',
    '微信图片_20260421232841_1444_78.jpg',
    '微信图片_20260421232842_1445_78.jpg',
    '微信图片_20260421232843_1446_78.jpg',
    '微信图片_20260421232845_1447_78.jpg',
    '微信图片_20260421232847_1448_78.jpg',
    '微信图片_20260421232848_1449_78.jpg',
    '微信图片_20260421232849_1450_78.jpg',
    '微信图片_20260421232850_1451_78.jpg',
    '微信图片_20260421232851_1452_78.jpg',
    '微信图片_20260421232851_1453_78.jpg',
    '微信图片_20260421232852_1454_78.jpg',
    '微信图片_20260421232853_1455_78.jpg',
    '微信图片_20260421232854_1456_78.jpg',
    '微信图片_20260421232854_1457_78.jpg',
    '微信图片_20260421232855_1458_78.jpg',
    '微信图片_20260421232856_1459_78.jpg',
    '微信图片_20260421232940_1460_78.jpg',
    '微信图片_20260421232944_1461_78.jpg',
    '微信图片_20260421232949_1462_78.jpg',
    '微信图片_20260421232955_1463_78.jpg',
    '微信图片_20260421233038_1464_78.jpg',
    '微信图片_20260421233123_1465_78.jpg',
    '微信图片_20260421233149_1466_78.jpg',
    '微信图片_20260421233151_1467_78.jpg',
    '微信图片_20260421233153_1468_78.jpg',
    '微信图片_20260421233155_1469_78.jpg',
    '微信图片_20260421233157_1470_78.jpg',
    '微信图片_20260421233200_1471_78.jpg',
    '微信图片_20260421233203_1472_78.jpg',
    '微信图片_20260421233207_1473_78.jpg',
    '微信图片_20260421233210_1474_78.jpg',
]

for i, old in enumerate(carousel_old, 1):
    content = content.replace(f'images/{old}', f'images/photo-{i:02d}.jpg')

# 投稿图片
for i in range(1, 5):
    content = content.replace(f'images/微信图片_202604220050{26+(i-1)*2}_148{i+1}_78.jpg', f'images/post-0{i}.jpg')

# 投稿封面
content = content.replace('images/投稿封面1.jpg', 'images/cover-01.jpg')
content = content.replace('images/投稿封面2.jpg', 'images/cover-02.jpg')
content = content.replace('images/投稿封面3.jpg', 'images/cover-03.jpg')

# 活动封面
content = content.replace('images/活动封面1.jpg', 'images/activity-01.jpg')
content = content.replace('images/活动封面2.jpg', 'images/activity-02.jpg')

# 其他图片
content = content.replace('images/抖音新照片.jpg', 'images/douyin-qrcode.jpg')
content = content.replace('images/赞助新照片.jpg', 'images/sponsor-qrcode.jpg')
content = content.replace('images/微信二维码.png', 'images/wechat-qrcode.png')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Paths updated!")
