# include "opencv.hpp"

using namespace cv;

void main()
{
	char *ipath = "D:/openCV/opencv/sources/samples/data/lena.jpg";

	// 图像显示
	Mat image = imread(ipath);
	imshow("Source image", image);
	waitKey();

	// 图像放缩
	Mat image1, image2;
	// 将image中的图像尺寸缩小后放入image1中，缩小的大小为长宽各为原来的一半
	resize(image, image1, Size(image.cols / 2, image.rows / 2));
	// 直接使用pyrDown将图像缩小为原来的一半
	pyrDown(image1, image2);
	// 显示图像
	imshow("Halfsize",image1);
	imshow("Quartersize",image2);
	// 等待用户按键
	waitKey();

	// 图像灰度转换
	Mat grey, grey1;
	// 将图片从bgr三通道图像转化为灰度图像(从一个颜色空间转换到另一个颜色空间)
	cvtColor(image, grey, COLOR_BGR2GRAY);
	// 通过二值化的方式将阈值120以上的图像点颜色设置为以十六进制表示的0xff最高亮度---白色
	threshold(grey, grey1, 120, 0xff, THRESH_BINARY);
	// 图像显示
	imshow("Grey", grey);
	imshow("Threshold 120", grey1);
	waitKey();

	// 高斯平滑处理
	Mat imageGauss;
	// 使用高斯滤波器的大小为5*5，高斯滤波器宽度自动选取（最后一个0参数）的滤波器
	GaussianBlur(image, imageGauss, Size(5, 5), 0);
	// 图像显示
	imshow("GaussianBlur image", imageGauss);
	waitKey();
}
