serve:
	mdbook serve

deploy:
	mdbook build
	scp -r book/* root@vps:/var/www/html/
