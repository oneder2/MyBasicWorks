#include <iostream>

using namespace std;
int main()
{
	int a, b, c, d, e;
	e = 0;
	for (a = 1; a <= 100; a++) {
		c = a % 2;//排除偶数
		
		if (c != 0) 
        {//如果不是偶数
			for (b = 1; b <= a; b = b + 2) 
            {//除以所有小于它的奇数
				d = a % b;//取余数
				if (d != 0) 
                {//有余数
					e = 0;
				}
				else 
                {//没有余数，e就+1
					e++;
				}
			}
			if (e == 0) 
            {//循环结束后，如果e还为0
				cout << a << endl;//输出这个质数
			}
		}
	}
}
