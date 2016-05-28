#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <malloc.h>

#include "linked_list.h"
#include "key_info.h"

struct key_info* find_period(char* string);
char* prepare_ciphertext(char* string);
char* caesar(char* str, int shift);
char* calculate_key(struct key_info* ki);
char* vig_decrypt(char* ciphertext, char* key);
float calc_ic_from_linked_list(struct linked_list* ll);
float chi_squared(char* str);


int main(int argc, char **argv){

	if(argc != 3){ // that is, hintfile and file to be applied to
		printf("Usage: %s hintfile cipherfile\n", argv[0]); // always given
		return EXIT_FAILURE;
	}

	FILE *fp;
	int i, filesize;

	struct key_info* ki;
	struct linked_list* ptr;

	char *hinttext, *ciphertext, *final_key, *final_text;

	char **contents = malloc(2 * sizeof(char*) );

	for(i = 1; i < argc; i++){
		fp = fopen(argv[i], "r");

		if(!fp){
			printf("File \"%s\" could not be opened;\n", argv[i]);
			return EXIT_FAILURE;
		}
		fseek(fp, 0, SEEK_END);
		filesize = ftell(fp);
		fseek(fp, 0, SEEK_SET);

		contents[i - 1] = calloc(filesize, sizeof(char));
		fgets(contents[i - 1], filesize, fp);
		fclose(fp);
	}
	hinttext = contents[0], ciphertext = contents[1]; // apparently I can't do that before I allocate...oh...of course.
	free(contents);

	hinttext = prepare_ciphertext(hinttext);
	ciphertext = prepare_ciphertext(ciphertext);

	ki = find_period(hinttext);
	final_key = calculate_key(ki);

	final_text = vig_decrypt(ciphertext, final_key);
	printf("%s\n", final_text);

	return EXIT_SUCCESS;
}

char* vig_decrypt(char* ciphertext, char* final_key){

	int i;
	char c;

	size_t c_len = strlen(ciphertext);
	size_t k_len = strlen(final_key);
	char* plaintext = calloc(c_len, sizeof(char));
	
	for(i = 0; i < c_len; i++){
		c = ciphertext[i] - 0x41;
		c = (c + ( 26 - final_key[i % k_len])) % 26;
		plaintext[i] = c + 0x41;
	}
	return plaintext;
}

char* prepare_ciphertext(char* string){
	
	int i, list_length;
	char c;
	struct linked_list* head = NULL;
	struct linked_list* tail = NULL;
	
	for(i = 0; string[i]; i++){
		if(isalpha(string[i])){
			c = string[i];
			if(islower(c)) c -= 0x20;

			if (head == NULL){
				head = ll_create(c);
				tail = head;
				list_length = 1;
			}
			else{
				tail = ll_insert(tail, c);
				list_length += 1;
			}
		}
	}
	
	char *retval = ll_to_char(head);
	destroy_linked_list(head);
	return retval;
}

struct key_info* find_period(char* string){

	int i, j, sequence, max_sequence = 15, len = strlen(string);
	int period_length;

	char indexes[max_sequence];
	float avg_ic_collection[max_sequence];
	struct linked_list **heads;

	struct key_info *ki = malloc( sizeof(struct key_info*) );

	for(i = 1; i < max_sequence; i++)
		indexes[i] = i;

	for(sequence = 2; sequence < max_sequence; sequence++){

		float avg_ic = 0;
		float sequence_ic[sequence];

		heads = generate_sequences(string, sequence);

		for(i = 0; i < sequence; i++){
			sequence_ic[i] = calc_ic_from_linked_list(heads[i]);
			avg_ic += sequence_ic[i];
			destroy_linked_list(heads[i]);
		}
		
		avg_ic /= sequence;
		avg_ic_collection[sequence] = avg_ic;
	}

	// Now something to sort them low to high...wish me luck
	for(i = 0; i < max_sequence - 1; i++){
		for(j = 0; j < max_sequence - 1 - i; j++){
			if(avg_ic_collection[j] > avg_ic_collection[j + 1]){
				float f_tmp = avg_ic_collection[j];
				avg_ic_collection[j] = avg_ic_collection[j + 1];
				avg_ic_collection[j + 1] = f_tmp;

				int c_tmp = indexes[j];
				indexes[j] = indexes[j + 1];
				indexes[j + 1] = c_tmp;
			}
		}
	}

	int index_in_loop, input, selection[4];
	printf("Statistics detected unusual properties; please choose a period length:\n");

	for(i = 0; i < 4; i++){
		index_in_loop = indexes[max_sequence - 4 + i];
		selection[i] = index_in_loop;

		printf("%i)  %i => %f\n", i + 1, index_in_loop, avg_ic_collection[index_in_loop]);
	}
	while(1){
		printf("Enter a number now: ");
		scanf("%i", &input);
		if(input > 0 && input <= 4){
			period_length = selection[input - 1];
			break;
		}
		else{ while(getchar() != '\n'){} continue; }
	}
	printf("%i\n", period_length);
	ki->key_length = period_length;
	ki->heads = generate_sequences(string, period_length);
	
	return ki;
}


char* caesar(char* string, int shift){

	int i;
	char c;
	size_t len = strlen(string);
	char* new_str = calloc(len, sizeof(char));

	shift = 26 - shift;

	for(i = 0; i < len; i++){
		c = string[i] - 0x41;
		c = (c + shift) % 26;
		new_str[i] = c + 0x41;
	}
	return new_str;

}

char* calculate_key(struct key_info* ki){
	int i, j;

	char i_min = 0;
	char *ces = NULL, *c_ptr;	
	char input[8], format_string[8];
	char *final_key = malloc(sizeof(char) * ki->key_length);

	float min = 0;
	float chi_squares[26];
	
	for(i = 0; i < ki->key_length; i++){

		c_ptr = ll_to_char(ki->heads[i]);
	
		for(j = 0; j < 26; j++){
			ces = caesar(c_ptr, j);
			chi_squares[j] = chi_squared(ces);
			free(ces);
		}
	
		min = chi_squares[0];
		for(j = 1; j < 26; j++){
			if(chi_squares[j] < min) { min = chi_squares[j]; i_min = j; }
		}
		final_key[i] = i_min;
	}
	printf("Statistically generated key: \"");

	for(i = 0; i < ki->key_length; i++){
		printf("%c", final_key[i] + 0x41);
	}
	printf("\"\n");

	printf("Would you like to make corrections to that key? (y/n) ");
	scanf("%3s", input);
	
	if(strcmp(input, "y") == 0 || strcmp(input, "yes") == 0){
		snprintf( format_string, 7, "%%%is", ki->key_length );
		printf("Please enter the key in uppercase characters (%i max): ", ki->key_length);
		scanf(format_string, input);	

		for(i = 0; i < ki->key_length; i++){
			final_key[i] = input[i] - 0x41;
		}
	}
	printf("Using key \"");
	for(i = 0; i < ki->key_length; i++){
		printf("%c", final_key[i] + 0x41);
	}
	printf("\"\n");
	return final_key;
}

float chi_squared(char* str){

	int i, len = strlen(str);
	int counts[26] = {0};

	float chi_square, dummy;

	for(i = 0; i < len; i++){
		counts[str[i] - 0x41]++;
	}

	for(i = 0; i < 26; i++){
		
		dummy = pow((counts[i] - len * freqs[i]), 2);
		dummy /= (len * freqs[i]);
		chi_square += dummy;
	}

	return chi_square;
}

float calc_ic_from_linked_list(struct linked_list* ll){

	char c;
	int i = 0;
	int f_sum = 0, f_spec_sum = 0;

	float final_ic;

	int f[26] = {0};
	struct linked_list* ptr = ll;

	while(1){
		c = ptr->val;
		//if(c >= 0x61 && c <= 0x7a){ // lets not count lowercase, cakital letters only
		if(islower(c)){ // lets not count lowercase, cakital letters only
			c -= 0x20; // add difference from 'A' to 'a'
		}
		if(isupper(c)){ // is our character in the uppercase ascii range?
			f[c - 0x41]++; // if so, lets increase its counter in "absolute" mode
		}
		if(ptr->next == NULL) break;
		ptr = ptr->next;
	}
	for(c = 0; c < 26; c++){
		f_sum += f[c];
		f_spec_sum += f[c] * (f[c] - 1); // lets get to f'
	}

	final_ic = f_spec_sum;
	final_ic /= (f_sum * (f_sum - 1)); // calculate final ic


	return final_ic;
}
