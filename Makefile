CONTAINER_NAME := llm_slide_demo
TARGET_IMAGE := llm_slide_demo_env

echo:
	echo ${TARGET_IMAGE}

build:
	docker build -f Dockerfile -t ${TARGET_IMAGE}:latest --label "llm_slide" .
	docker image prune --force --filter='label=llm_slide' 

run_app:
	docker run 													\
	--name ${CONTAINER_NAME}										\
	-p 4321:4321 \
	${TARGET_IMAGE}											\

logs:
	docker logs -n 20 ${CONTAINER_NAME} -f

clean:
	docker rm ${CONTAINER_NAME}

stop:
	docker stop ${CONTAINER_NAME}