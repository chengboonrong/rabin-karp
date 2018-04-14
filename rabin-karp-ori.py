d = 256
def rabin_karp(text, pattern ,q):
	n = len(text)
	m = len(pattern)

	i = 0
	j = 0
	p = 0 # hash value of text
	t = 0 # hash value of pattern
	h = 1

	for i in range(m-1):
		h = (h*d)%q 

	for i in range(m):
		p = (d*p + ord(pattern[i])) % q # for pattern 
		t = (d*t + ord(text[i])) % q # for text of 1st box

	for i in range(n-m+1):
		if p==t:

			for j in range(m):
				if text[i+j] != pattern[j]:
					break

			j += 1
			if j == m:
				print("Pattern Found at index " + str(i))


		if i < n-m:
			t = (d*(t-ord(txt[i])*h) + ord(txt[i+m]))%q # text for next box

			if t < 0:
				t = t+q

txt = "GEEKS FOR GEEKS"
ptn = "GEEK"
q = 101
rabin_karp(txt, ptn, q)
