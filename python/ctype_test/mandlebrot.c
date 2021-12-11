#include <stdio.h>

int square_number(int number) {
		return number*number;
}

// z_0 = 0 + 0i every time
// a^2 + 2ab + c^2
// Re_n+1 = a^2 - c^2
// Im_n+1 = 2ab
// z_n+1 = (Re_n+1+Im_n+1) + (C_Re + C_Im)
int mandlebrot(double c_real, double c_imaginary, int iterations) {
		double z_real = 0;
		double z_imaginary = 0;
		int max_iterations = iterations;
		int current_iteration = 0;
		double z_real_squared = z_real * z_real;
		double z_imaginary_squared = z_imaginary * z_imaginary;
		while (z_real_squared + z_imaginary_squared < 4 && current_iteration < max_iterations) {
				// compute new z values
				z_imaginary = 2 * z_real * z_imaginary + c_imaginary;
				z_real = z_real_squared - z_imaginary_squared + c_real;
				// setup next iteration
				z_real_squared = z_real * z_real;
				z_imaginary_squared = z_imaginary * z_imaginary;
				current_iteration++;
		}
		return current_iteration;
}



		

