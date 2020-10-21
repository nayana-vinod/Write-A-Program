# include <iostream>
using namespace std;

int main()
{
    char op;
    int num1, num2;
    
    cout << "Enter two operands: ";
    cin >> num1 >> num2;
    cout << "Enter the operator: ";
    cin >> op;
    
    switch(op)// For comapring the character op
    {
        case '+':
            cout <<num1<<" "<<op<<" "<<num2<<" = "<<num1+num2;
            break;

        case '-':
            cout <<num1<<" "<<op<<" "<<num2<<" = "<< num1-num2;
            break;

        case '*':
            cout <<num1<<" "<<op<<" "<<num2<<" = "<< num1*num2;
            break;

        case '/':
            cout <<num1<<" "<<op<<" "<<num2<<" = "<< num1/num2;
            break;

        default:
            cout << "\nInvalid Operator!";
            break;
    }

    return 0;
}
