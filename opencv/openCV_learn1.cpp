# include "opencv.hpp"

using namespace cv;

void main()
{
	char *ipath = "D:/openCV/opencv/sources/samples/data/lena.jpg";

	// ͼ����ʾ
	Mat image = imread(ipath);
	imshow("Source image", image);
	waitKey();

	// ͼ�����
	Mat image1, image2;
	// ��image�е�ͼ��ߴ���С�����image1�У���С�Ĵ�СΪ�����Ϊԭ����һ��
	resize(image, image1, Size(image.cols / 2, image.rows / 2));
	// ֱ��ʹ��pyrDown��ͼ����СΪԭ����һ��
	pyrDown(image1, image2);
	// ��ʾͼ��
	imshow("Halfsize",image1);
	imshow("Quartersize",image2);
	// �ȴ��û�����
	waitKey();

	// ͼ��Ҷ�ת��
	Mat grey, grey1;
	// ��ͼƬ��bgr��ͨ��ͼ��ת��Ϊ�Ҷ�ͼ��(��һ����ɫ�ռ�ת������һ����ɫ�ռ�)
	cvtColor(image, grey, COLOR_BGR2GRAY);
	// ͨ����ֵ���ķ�ʽ����ֵ120���ϵ�ͼ�����ɫ����Ϊ��ʮ�����Ʊ�ʾ��0xff�������---��ɫ
	threshold(grey, grey1, 120, 0xff, THRESH_BINARY);
	// ͼ����ʾ
	imshow("Grey", grey);
	imshow("Threshold 120", grey1);
	waitKey();

	// ��˹ƽ������
	Mat imageGauss;
	// ʹ�ø�˹�˲����Ĵ�СΪ5*5����˹�˲�������Զ�ѡȡ�����һ��0���������˲���
	GaussianBlur(image, imageGauss, Size(5, 5), 0);
	// ͼ����ʾ
	imshow("GaussianBlur image", imageGauss);
	waitKey();
}
