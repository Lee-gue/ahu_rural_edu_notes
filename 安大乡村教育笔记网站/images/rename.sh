#!/bin/bash

# 活动剪影图片 - 按文件名排序
idx=1
for f in $(ls 微信图片_20260421232*.jpg 2>/dev/null | sort); do
    printf -v new "photo-%02d.jpg" $idx
    mv "$f" "$new" 2>/dev/null
    echo "$f -> $new"
    ((idx++))
done

# 投稿图片
mv 微信图片_20260422005026_1482_78.jpg post-01.jpg 2>/dev/null
mv 微信图片_20260422005028_1483_78.jpg post-02.jpg 2>/dev/null
mv 微信图片_20260422005030_1484_78.jpg post-03.jpg 2>/dev/null
mv 微信图片_20260422005032_1485_78.jpg post-04.jpg 2>/dev/null

# 其他图片
mv 投稿封面1.jpg cover-01.jpg 2>/dev/null
mv 投稿封面2.jpg cover-02.jpg 2>/dev/null
mv 投稿封面3.jpg cover-03.jpg 2>/dev/null
mv 活动封面1.jpg activity-01.jpg 2>/dev/null
mv 活动封面2.jpg activity-02.jpg 2>/dev/null
mv 抖音新照片.jpg douyin-qrcode.jpg 2>/dev/null
mv 赞助新照片.jpg sponsor-qrcode.jpg 2>/dev/null
mv 微信二维码.png wechat-qrcode.png 2>/dev/null
mv 抖音二维码.png douyin-icon.png 2>/dev/null
mv 赞助码.jpg sponsor-old.jpg 2>/dev/null

echo "Done!"
