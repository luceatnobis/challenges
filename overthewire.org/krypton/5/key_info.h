struct key_info{  
  
    int key_length;  
    struct linked_list** heads;  
}; 
 
struct linked_list** generate_sequences(char* string, int sequence){ 
 
    int i; 
    size_t len = strlen(string); 
 
    struct linked_list **heads = malloc(sizeof(struct linked_list*) * sequence); 
    struct linked_list **sequences = malloc(sizeof(struct linked_list*) * sequence); 
 
    for(i = 0; i < sequence; i++){ 
        heads[i] = ll_create(string[i]); 
        sequences[i] = heads[i]; 
    } 
 
    for(i = sequence; i < len; i++){ 
        sequences[i % sequence] = ll_insert(sequences[i % sequence], string[i]); 
    } 
 
    return heads; 
}

