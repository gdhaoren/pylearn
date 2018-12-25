# include "opencv.hpp"

using namespace cv;
using namespace std;

void main()
{
	String ipath = "D:/openCV/opencv/sources/samples/data/lena.jpg";
	//����ͼƬ
	Mat src_image;
	src_image = imread(ipath);
	imshow("ԭʼͼ��", src_image);
	waitKey();

	//��ֵ�˲�
	Mat avg_image;
	blur(src_image, avg_image, Size(5, 5));
	imshow("��ֵ�˲�", avg_image);
	waitKey();

	//��˹�˲�����Ȩ�˲���
	Mat gauss_image;
	GaussianBlur(src_image, gauss_image, Size(5, 5), 0, 0);
	imshow("��˹�˲�",gauss_image);
	waitKey();

	//��ֵ�˲�
	Mat median_image;
	medianBlur(src_image, median_image, 7);
	imshow("��ֵ�˲�", median_image);
	waitKey();

	//ͼ����̬ѧ�˲�
	Mat o_image,element,c_image,oc_image;
	// ����ṹԪ��,ʹ�÷��νṹԪ��
	element = getStructuringElement(MORPH_RECT, Size(5, 5));
	// �����˲����Ƚ��п�����
	morphologyEx(src_image, o_image, MORPH_OPEN, element);
	imshow("������", o_image);
	waitKey();
	// ���б�����
	morphologyEx(src_image, c_image, MORPH_CLOSE, element);
	imshow("������", c_image);
	waitKey();
	// �����ȿ��������
	morphologyEx(o_image, oc_image, MORPH_CLOSE, element);
	imshow("�ȿ��������", oc_image);
	waitKey();

}
