struct linked_list{

	char val;
	struct linked_list* next;

};


struct linked_list* ll_create(char c){
	struct linked_list* new_list = malloc(sizeof(struct linked_list));

	new_list->val = c;
	new_list->next = NULL;

	return new_list;
}

struct linked_list* ll_insert(struct linked_list* ll, char chr){
	struct linked_list* new_node = malloc(sizeof(struct linked_list));

	new_node->val = chr;
	ll->next = new_node;
	new_node->next = NULL;

	return new_node;
}

char* ll_to_char(struct linked_list* ll){

	char* str;
	size_t len = 0, i;
	struct linked_list* ptr = ll;

	while(1){
		len++;
		if(ptr->next == NULL) break;
		ptr = ptr->next;
	}
	str = calloc(sizeof(char), len);
	ptr = ll;

	for(i = 0; i < len; i++){
		str[i] = ptr->val;

		if(ptr->next == NULL) break;
		ptr = ptr->next;
	}
	return str;
}

size_t ll_length(struct linked_list* ll){

	size_t len = 0;
	struct linked_list *ptr = ll;

	while(1){
		if(ptr->next == NULL) break;
		len++;
		ptr = ptr->next;
	}
	return len;
}

void destroy_linked_list(struct linked_list *ll){
	struct linked_list *ptr = ll;
	while(1){
		ptr = ll->next;
		free(ll);
		if(ptr == NULL) break;
		ll = ptr;
	}
}
double freqs[] = 	{ 	0.08167,0.01492,0.02782,0.04253,0.12702,0.02228,0.02015,0.06094,0.06966,0.00153,0.00772,
						0.04025,0.02406,0.06749,0.07507,0.01929,0.00095,0.05987,0.06327,0.09056,0.02758,0.00978,
						0.02360,0.00150,0.01974,0.00074
					};
