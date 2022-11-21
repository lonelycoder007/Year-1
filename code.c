#include <stdio.h>
int main(){	
int num1, num2, choice, add, sub, multi, div;
printf("Enter your choice for the Desired Operation:- \n 1==> Addition \n 2==> Subtraction \n 3==> Multiplication \n 4==> Division ");
printf("\nEnter your choice:- ");
scanf("%d",&choice);
// FOR ADDITION
if(choice==1)
	{
		printf("Enter Two numbers:-  ");
		scanf("%d %d", &num1,&num2);
		printf("The addition is %d",num1+num2);
	}
//FOR SUBTRACTION	
else if(choice==2)
	{
		printf("Enter Two numbers:-  ");
		scanf("%d %d", &num1,&num2);
		printf("The subtraction is %d",num1-num2);
	}
//FOR MULTIPLICATION	
else if(choice==3)
	{
        printf("Enter Two numbers:-  ");
		scanf("%d %d", &num1,&num2);
		printf("The multiplication is %d",num1*num2);
	}
//FOR DIVISION
else if(choice==4)
	{
		printf("Enter Two numbers:-  ");
		scanf("%d %d", &num1,&num2);
		printf("The division is %d",num1/num2);
	}
//FOR INVALID CHOICE
else
	{

		printf("INVALID OPTION");
		
	}
return 0;
}
