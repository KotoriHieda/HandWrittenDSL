#sucoding:utf-8
import cv2
import numpy as np
if __name__ == '__main__':
#画像をグレースケールで読み込む
	img = cv2.imread('/Users/hieda/Desktop/class_1.jpg', 1)
	temp = cv2.imread('/Users/hieda/Desktop/class_temp.jpg', 1)
	gray1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	gray2 = cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)
 # 二値変換
    	thresh = 100
    	max_pixel = 255
    	ret, img1 = cv2.threshold(gray1,
                                 thresh,
                                 max_pixel,
                                 cv2.THRESH_BINARY)
     # 二値変換
    	thresh = 100
    	max_pixel = 255
    	ret, temp1 = cv2.threshold(gray2,
                                 thresh,
                                 max_pixel,
                                 cv2.THRESH_BINARY)

        cv2.imwrite('niti_temp_color2.jpg', temp1)


	#マッチングテンプレートを実行
	#比較方法はcv2.TM_CCOEFF_NORMEDを選択
	result = cv2.matchTemplate(img1, temp1, cv2.TM_CCOEFF_NORMED)
	#検出結果から検出領域の位置を取得
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
	top_left = max_loc
	w, h = temp.shape[:-1]
	bottom_right = (top_left[0] + w, top_left[1] + h)
	#検出領域を四角で囲んで保存
	result = cv2.imread('/Users/hieda/Desktop/niti_temp_color.jpg')
	cv2.rectangle(result,top_left, bottom_right, (255, 0, 0), 2)
	cv2.imwrite('niti_temp_class1_result5.jpg', result)

