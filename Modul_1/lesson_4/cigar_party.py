def cigar_party (cigars, is_weekend):
    result = False
    if is_weekend and cigars >= 40:
        result = True
    elif cigars >= 40 and cigars <= 60 and not is_weekend:
        result = True
    return result

print(cigar_party(200, True))