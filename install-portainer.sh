#!bash
curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh
sudo groupadd docker
sudo gpasswd -a $USER docker
sudo docker run -d --restart always \
  -e PUID=1000 -e PGID=1000 -e TZ=Europe/Sofia \
  -p 9000:9000 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v portainer_data:/data \
  --name portainer \
  portainer/portainer -H unix:///var/run/docker.sock
