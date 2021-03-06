// rice.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
//


#include <iostream>
#include<opencv.hpp>

using namespace cv;
using namespace std;


int main()
{
	//读入图片
	String ipath = "C:\\Users\\gdhao\\Desktop\\rice.png";
	//显示图片
	Mat rice,rice_bl;
	rice = imread(ipath);
	imshow("Rice", rice);
	waitKey();

	//高斯滤波,可以去除一定的噪点
	GaussianBlur(rice, rice_bl, Size(3, 3), 0, 0);

	//先对图像进行灰度转换
	Mat gray;
	cvtColor(rice_bl, gray, COLOR_BGR2GRAY);

	//对灰度图像通过全局阈值区域划分方法--大津算法来进行区域划分,生成二值图像
	Mat gray_dj;
	threshold(gray, gray_dj, 0, 0xff, THRESH_OTSU);
	//显示一下区域划分后的图像
	imshow("OTSU", gray_dj);
	waitKey();

	//有些小的白色区域我们,使用形态学滤波的腐蚀运算方法来处理
	Mat bx,element = getStructuringElement(MORPH_CROSS, Size(3, 3));
	morphologyEx(gray_dj, bx, MORPH_ERODE, element);
	//显示腐蚀后的图像
	imshow("morphology", bx);
	waitKey();

	//利用划分好的二值图像来提取边界的contour
	//复制一份图像
	Mat seg = bx.clone();
	//调用findcontours函数来寻找边界等值线
	//生成存储等值线上点的信息的变量
	vector<vector<Point>> cnts;
	//调用findcontours函数,RETR_EXTERNAL,只检测最外层的轮廓
	findContours(seg, cnts, RETR_EXTERNAL, CHAIN_APPROX_SIMPLE);

	//从contours中提取每一条轮廓进行处理
	int count = 0; //统计米粒个数
	for (auto &contour : cnts)
	{
		//计算每个区域的面积
		auto area = contourArea(contour);
		if (area < 10) //去除面积过小的分割结果
			continue;
		count++;
		//绘制包围矩形
		auto rect = boundingRect(contour);
		//在原始图像上绘制出这些矩形
		rectangle(rice, rect, Scalar(0, 0, 0xff), 1);

		//为每个方格绘制标注
		char strCount[100];
		sprintf_s(strCount, 100,"blog %d:%.2f", count, area);
		putText(rice, strCount, Point(rect.x, rect.y), FONT_HERSHEY_PLAIN, 0.5, Scalar(0, 0xff, 0));
	}
	//显示标注后的图像
	imshow("p_rice", rice);
	waitKey();
}

// 运行程序: Ctrl + F5 或调试 >“开始执行(不调试)”菜单
// 调试程序: F5 或调试 >“开始调试”菜单

// 入门提示: 
//   1. 使用解决方案资源管理器窗口添加/管理文件
//   2. 使用团队资源管理器窗口连接到源代码管理
//   3. 使用输出窗口查看生成输出和其他消息
//   4. 使用错误列表窗口查看错误
//   5. 转到“项目”>“添加新项”以创建新的代码文件，或转到“项目”>“添加现有项”以将现有代码文件添加到项目
//   6. 将来，若要再次打开此项目，请转到“文件”>“打开”>“项目”并选择 .sln 文件
