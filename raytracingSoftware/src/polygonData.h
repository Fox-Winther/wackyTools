// an example of how the 3d part works, using a prism


// coordinates follow the global axis
// {X, Y, Z}, where positives values would lead to:
// {right, up, front}

float vertexCoordinates[4][3] = {
	{0, 0, 1}, //  here im using accurate coordinates based on trigonometry, 
	{0.87, 0, -0.5}, //  so some numbers may look funky but theyre right
	{-0.87, 0, -0.5}, //  360/3 = 120 ; sin(120) = 0.87 ; cos(120) = -0.5 ; 
	{0, 2.09, 0} //  arcLenght(120) = 2.09
};


// the faces are interconnected via the vertexes
// unlike coordinates, the connections doesnt need to be ordered
// for convention and readability, order from smaller to bigger

float faceConnections[4][3] = {
	{0,1,2},
	{0,1,3},
	{1,2,3},
	{0,2,3}

};