#include<iostream>
#include<cstring>
#include<cstdio>
 
using namespace std;
 
int main(void){

	char s[50];
	memset(s, '\0', 50);
	int vow=0,cons=0,i;
	cout<<"Enter phrase: "; cin>>s;
	i=0;
	while(s!=0 && i<strlen(s)){
		switch (s[i]){
				case 'a':
				case 'e':
				case 'i':
				case 'o':
				case 'u':
				case 'A':
				case 'E':
				case 'I':
				case 'O':
				case 'U':
				{
					vow++;
					break;
				}
				default:
					cons++;
		}
		i++;
	}
	cout<<"The total number of vowels inputted were: "<<vow<<endl;
	cout<<"The total number of consonants inputted were: "<<cons<<endl;
}
