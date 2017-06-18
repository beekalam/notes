all:
	$(shell for file in *md; do \
		rm $$file.html; \
		echo "making file..."; \
		echo $$file; \
		touch $$file.html; \
		echo "<html>" >> $$file.html; \
		echo "<body>" >> $$file.html; \
		markdown $$file  >> $$file.html; \
		echo "</body>" >> $$file.html; \
		echo "</html>" >> $$file.html; \
		done)

clean:
	$(shell for file in *html; do rm $$file; done)
