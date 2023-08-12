%{
#include <stdio.h>
#include <stdlib.h>
%}

DIGIT [0-9]
NUMBER {DIGIT}+(\.{DIGIT}+)?

%%
"exit"  return 0;
"quit"  return 0;
"q"     return 0;
"add"   { printf("Operation: ADD\n"); return '+'; }
"sub"   { printf("Operation: SUBTRACT\n"); return '-'; }
"mul"   { printf("Operation: MULTIPLY\n"); return '*'; }
"div"   { printf("Operation: DIVIDE\n"); return '/'; }
{NUMBER} { printf("Operand: %s\n", yytext); return 'N'; }
[ \t\n]  /* Ignore whitespace */
.        { printf("Invalid character: %s\n", yytext); return yytext[0]; }
%%

int yywrap() {
    return 1; // Indicate the end of input
}

int main() {
    printf("Simple Calculator\n");
    int token;
    double result = 0;
    double operand = 0;
    char operator = '+';
    int hasOperand = 0;

    while (1) {
        token = yylex();
        if (token == 0) {
            break; // Exit the loop on "exit", "quit", or "q" command
        } else if (token == 'N') {
            operand = atof(yytext);

            // Perform the calculation
            switch (operator) {
                case '+':
                    result += operand;
                    break;
                case '-':
                    result -= operand;
                    break;
                case '*':
                    result *= operand;
                    break;
                case '/':
                    result /= operand;
                    break;
            }

            hasOperand = 1;
        } else {
            if (hasOperand) {
                printf("Result so far: %f\n", result);
                hasOperand = 0;
            }
            operator = token;
        }
    }

    printf("Final Result: %f\n", result);

    return 0;
}
