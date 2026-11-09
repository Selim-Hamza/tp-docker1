# tp-docker1

### Manipulation de base des conteneurs
- Vérification de la version de Docker
```
docker -- version
Docker version 29.9.2-2, build a82e528901260c8df6073311379eac65f92db204
```

- Liste des images disponible (J'ai déjà installer hello-world)
```
 $ docker images
                                                                                                        i Info →   U  In Use
IMAGE                ID             DISK USAGE   CONTENT SIZE   EXTRA
hello-world:latest   c567b231f656       25.9kB         9.49kB    U   
```

- Télécharger l'image "hello-world"
```
 $ docker pull hello-world
Using default tag: latest
latest: Pulling from library/hello-world
4f55086f7dd0: Pull complete 
d5e71e642bf5: Download complete 
Digest: sha256:c567b231f65614688711a75f31518a064258a51d442117a3e771a3a8fdba78ef
Status: Downloaded newer image for hello-world:latest
docker.io/library/hello-world:latest
```




