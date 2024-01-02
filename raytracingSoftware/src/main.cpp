#include <iostream>
#include <fstream> 
#include <string>
#include "polygonData.h"


using namespace std;
bool useDebug = true; // shows debug prints.
					  // disable if releasing for non-programmers

void printd(string x, bool isDebug=false) // provides support for debug-only prints
{
	if (!(isDebug) || (useDebug && isDebug))
	{
		cout << x << endl; 
	}
}

int main()
{
	printd("revving up the engine");
	printd("STARTING STARTUP", true);

	// things that happen only at the start of the scene
	struct
	{
		int cameraFOV = 70;// in degrees
		float cameraPos[] = {0, .5, -10}; // X Y Z, as mentioned in the polygonData
		float cameraAngle[] = {0, 0, 0}; // 0,0,0 = upright pointing forward
	} scene;

	// TODO ADD ALL THE MATH LOGIC

	return 0;
}