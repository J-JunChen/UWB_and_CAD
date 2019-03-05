%module RTLSClient 

%{
#include "RTLSClient.h"    
%}

%include "typemaps.i"


typedef struct vec3d {
	double	x;
	double	y;
	double	z;
};

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