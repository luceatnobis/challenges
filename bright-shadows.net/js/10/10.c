#include <stdio.h>
#include <string.h>

int main(){
	int ax2 = 1;
	int aNum = 0;
	int i = 0;

	char some_input [] = "no";
	char pass_val[] = "\"eHgMYUn_MWW[SLZ!kKOiM\\SX[Uif'GcaO]YU`eWPJIv|g`YTVTlrUPQT`R_T MgIO~pcM[QHaQVrYI^u'f,ueHgMYU,";

	for(i=0; i < strlen(some_input) ;i++){
		char cx = some_input[i];
		aNum = aNum + (int) cx;
		ax2 = ( ax2 * (int) cx % 65537 );
	}
}
