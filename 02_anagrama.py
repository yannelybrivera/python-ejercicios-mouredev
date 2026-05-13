def anagrama(word1, word2):
    w1 = word1.replace(" ", "").lower()
    w2 = word2.replace(" ", "").lower()

    if sorted(w1) == sorted(w2):
        print("Es un anagrama")
    else:
        print("No es un anagrama")
        
anagrama("amor", "roma")