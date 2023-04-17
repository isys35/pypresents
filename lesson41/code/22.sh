docker run \
		--name my-nginx \
		-v ${PWD}:/usr/share/nginx/html \
		-p 8888:80 \
		-d \
		--rm \
		nginx