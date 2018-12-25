# include "opencv.hpp"

using namespace cv;
using namespace std;

void main()
{
	String ipath = "D:/openCV/opencv/sources/samples/data/lena.jpg";
	//读入图片
	Mat src_image;
	src_image = imread(ipath);
	imshow("原始图像", src_image);
	waitKey();

	//均值滤波
	Mat avg_image;
	blur(src_image, avg_image, Size(5, 5));
	imshow("均值滤波", avg_image);
	waitKey();

	//高斯滤波（加权滤波）
	Mat gauss_image;
	GaussianBlur(src_image, gauss_image, Size(5, 5), 0, 0);
	imshow("高斯滤波",gauss_image);
	waitKey();

	//中值滤波
	Mat median_image;
	medianBlur(src_image, median_image, 7);
	imshow("中值滤波", median_image);
	waitKey();

	//图像形态学滤波
	Mat o_image,element,c_image,oc_image;
	// 构造结构元素,使用方形结构元素
	element = getStructuringElement(MORPH_RECT, Size(5, 5));
	// 调用滤波器先进行开运算
	morphologyEx(src_image, o_image, MORPH_OPEN, element);
	imshow("开运算", o_image);
	waitKey();
	// 进行闭运算
	morphologyEx(src_image, c_image, MORPH_CLOSE, element);
	imshow("闭运算", c_image);
	waitKey();
	// 进行先开后闭运算
	morphologyEx(o_image, oc_image, MORPH_CLOSE, element);
	imshow("先开后闭运算", oc_image);
	waitKey();

}
