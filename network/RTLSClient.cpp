#include "RTLSClient.h"
#include <math.h>

RTLSClient::RTLSClient(vec3d anchor_0, vec3d anchor_1, vec3d anchor_2, vec3d anchor_3)
{
    // 初始化基站坐标
    _ancArray[0].x = anchor_0.x;
    _ancArray[0].y = anchor_0.y;
    _ancArray[0].z = anchor_0.z;

    _ancArray[1].x = anchor_1.x;
    _ancArray[1].y = anchor_1.y;
    _ancArray[1].z = anchor_1.z;

    _ancArray[2].x = anchor_2.x;
    _ancArray[2].y = anchor_2.y;
    _ancArray[2].z = anchor_2.z;

    _ancArray[3].x = anchor_3.x;
    _ancArray[3].y = anchor_3.y;
    _ancArray[3].z = anchor_3.z;

    cout << "initialize RTLSClient !" << endl;
}

RTLSClient::~RTLSClient()
{
    cout << "~RTLSClient" << endl;
}

int RTLSClient::calculateTagLocation(vec3d *report, int count, int *ranges)
{
    int result = 0;
    vec3d anchorArray[4];

    anchorArray[0].x = _ancArray[0].x;
    anchorArray[0].y = _ancArray[0].y;
    anchorArray[0].z = _ancArray[0].z;

    anchorArray[1].x = _ancArray[1].x;
    anchorArray[1].y = _ancArray[1].y;
    anchorArray[1].z = _ancArray[1].z;

    anchorArray[2].x = _ancArray[2].x;
    anchorArray[2].y = _ancArray[2].y;
    anchorArray[2].z = _ancArray[2].z;

    anchorArray[3].x = _ancArray[3].x;
    anchorArray[3].y = _ancArray[3].y;
    anchorArray[3].z = _ancArray[3].z;

    result = GetLocation(report, ((count == 4) ? 1 : 0), &anchorArray[0], ranges);

    return result;
}

vec3d RTLSClient::trilaterateTag(int range_0, int range_1, int range_2, int range_3, int count)
{
    // cout << "function trilaterateTag" << endl;

    int result; //whether is TRIL_3SPHERES or TRIL_4SPHERES
    vec3d report; //tag position

    int rangeValue[1][4];
    rangeValue[0][0] = range_0;
    rangeValue[0][1] = range_1;
    rangeValue[0][2] = range_2;
    rangeValue[0][3] = range_3;
    
    result = calculateTagLocation(&report, count, &rangeValue[0][0]);

    cout << "result: " << result << endl;
    cout<<"[ "<<report.x<< ", " <<report.y <<", "<<report.z<<"]"<<endl;

    return report;

}