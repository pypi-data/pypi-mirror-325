

build: clean
	./build.sh

clean:
	rm -rf src/pyric.egg-info/ dist
# from gemini
	rm -rf dist/ .egg-info build/

push: upload

upload: build
	./upload.sh
