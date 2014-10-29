def decode_input(text_in):
    
    return u' '.join(text_in)
    if type(text_in) == list:
        text_out = u' '.join([t.decode('utf-8') for t in text_in])
    else:
        text_out = text_in.decode('utf-8')
    return text_out