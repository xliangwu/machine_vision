from PIL import Image
from paddleocr import PaddleOCR, draw_ocr

# Paddleocr目前支持的多语言语种可以通过修改lang参数进行切换
# 例如`ch`, `en`, `fr`, `german`, `korean`, `japan`
# need to run only once to download and load model into memory
ocr = PaddleOCR(use_angle_cls=True, lang="ch")
img_path = r'D:\资料归类\朋友公司\首坤科技\机器视觉\日期照片\日期照片\生产日期照片\IMG_20220323_155413.jpg'
result = ocr.ocr(img_path, cls=True)
for line in result:
    print(line)

# 显示结果
image = Image.open(img_path).convert('RGB')
boxes = [line[0] for line in result]
txts = [line[1][0] for line in result]
scores = [line[1][1] for line in result]
im_show = draw_ocr(image, boxes, txts, scores)
im_show = Image.fromarray(im_show)
im_show.save('result.jpg')
