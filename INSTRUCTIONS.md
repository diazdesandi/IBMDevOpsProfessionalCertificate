1. Build docker image
```
docker build -t theia-devcontainer .
```

2. Run container using the JSON values
```
docker run -it --rm \
  -p 8080:8080 \
  -v $(pwd):/project \
  -e FLASK_DEBUG=true \
  -e FLASK_APP=counter:app \
  -e PORT=8080 \
  -e PYTHONIOENCODING=utf-8 \
  --name theia-container \
  theia-devcontainer
```
3. Install requeriments
```
sudo pip install -r requirements.txt 
```