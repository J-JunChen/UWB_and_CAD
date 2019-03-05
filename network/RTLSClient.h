#ifndef RTLSCLIENT_H
#define RTLSCLIENT_H

#include "trilateration.h"
#include <stdint.h>
#include <iostream>
#include <list>

using namespace std;

#define MAX_NUM_TAGS (8)
#define MAX_NUM_ANCS (4)
#define HIS_LENGTH 50

typedef struct
{
    double x, y, z;
    uint64_t id;
    int tagRangeCorection[MAX_NUM_TAGS];
} anc_struct_t;


typedef struct
{
    double x_arr[HIS_LENGTH];
    double y_arr[HIS_LENGTH];
    double z_arr[HIS_LENGTH];
    double av_x, av_y, av_z; //average
    double fx, fy, fz; //filter average
    double sqx_arr[HIS_LENGTH]; //square x
    double sqy_arr[HIS_LENGTH];
    double sqz_arr[HIS_LENGTH];
    double avsq_x, avsq_y, avsq_z; //average of squares
    double errx_arr[HIS_LENGTH]; //error x (x-av_x)
    double erry_arr[HIS_LENGTH];
    double errz_arr[HIS_LENGTH];
    double averr_x, averr_y, averr_z; //avearge error
    double variancex, variancey, variancez;
    double std_x, std_y, std_z;
    double r95;
    int id;
    int arr_idx;
    int count;
    int numberOfLEs;
    int filterReady;
    bool ready;
    int rangeSeq;
    int rangeCount[256];
    int rangeValue[256][4]; //(mm) each tag ranges to 4 anchors - it has a range number which is modulo 256
} tag_reports_t;

class RTLSClient
{
  private:
    anc_struct_t _ancArray[MAX_NUM_ANCS];
    // list <tag_reports_t> _tagList;

  public:
    RTLSClient(vec3d anchor_0, vec3d anchor_1, vec3d anchor_2, vec3d anchor_3);
    ~RTLSClient();

    int calculateTagLocation(vec3d *report, int count, int *ranges);
    vec3d trilaterateTag(int range_0, int range_1, int range_2, int range_3, int count);
};

#endif