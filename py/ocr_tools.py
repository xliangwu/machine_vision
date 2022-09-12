from PIL import Image
from paddleocr import PaddleOCR, draw_ocr
import os
from os import listdir
from os.path import isfile, join


def process(image_dir, result_dir):
    print("{} => {}".format(image_dir, result_dir))

    onlyfiles = [f for f in listdir(image_dir) if isfile(join(image_dir, f))]
    for item in onlyfiles:
        fileName = os.path.basename(item)
        name = os.path.splitext(fileName)[0]
        img_path = join(image_dir, item)
        output_path = join(result_dir, name+"_res.jpg")
        print("process {}".format(img_path))
        imageOcr(img_path,output_path)


def imageOcr(img_path, output_path):
    ocr = PaddleOCR(use_angle_cls=True, lang="ch")
    result = ocr.ocr(img_path, cls=True)

    # 显示结果
    image = Image.open(img_path).convert('RGB')
    boxes = [line[0] for line in result]
    txts = [line[1][0] for line in result]
    scores = [line[1][1] for line in result]
    im_show = draw_ocr(image, boxes, txts, scores)
    im_show = Image.fromarray(im_show)
    im_show.save(output_path)


if __name__ == "__main__":
    process(r'D:\ocr\test_images\src', r'D:\ocr\test_images\result')
